import copy
import json
import re
from typing import Callable, Optional, Type, TypeVar

from langchain.output_parsers.format_instructions import PYDANTIC_FORMAT_INSTRUCTIONS
from langchain.output_parsers.openai_functions import PydanticOutputFunctionsParser
from langchain.schema import ChatGeneration, Generation, OutputParserException
from langchain.schema.output_parser import BaseGenerationOutputParser, BaseOutputParser
from pydantic.v1 import BaseModel, ValidationError
from typing_extensions import Self

T = TypeVar("T")


class LambdaOutputParser(BaseOutputParser[T]):
    _parse: Optional[Callable[[str], T]] = None

    def parse(self, text: str) -> T:
        if self._parse is None:
            raise NotImplementedError(
                "LambdaOutputParser.lambda_parse() is not implemented"
            )
        return self._parse(text)

    @property
    def _type(self) -> str:
        return "lambda"


class BoolOutputParser(BaseOutputParser[bool]):
    def parse(self, text: str) -> bool:
        return text.strip()[:1].lower() == "y"

    def get_format_instructions(self) -> str:
        return "\nAnswer only with 'Yes' or 'No'."

    @property
    def _type(self) -> str:
        return "bool"


M = TypeVar("M", bound=BaseModel)


class MultiToolParser(BaseGenerationOutputParser[M]):
    output_types: list[Type[M]]

    def parse_result(self, result: list[Generation], *, partial: bool = False) -> M:
        function_call = self._pre_parse_function_call(result)

        output_type_names = [t.__name__.lower() for t in self.output_types]

        if function_call["name"] not in output_type_names:
            raise OutputParserException("Invalid function call")

        parser = self._get_parser_for(function_call["name"])

        return parser.parse_result(result)

    def _pre_parse_function_call(self, result: list[Generation]) -> dict:
        generation = result[0]
        if not isinstance(generation, ChatGeneration):
            raise OutputParserException(
                "This output parser can only be used with a chat generation."
            )
        message = generation.message
        try:
            func_call = copy.deepcopy(message.additional_kwargs["function_call"])
        except KeyError:
            raise OutputParserException(
                f"The model refused to respond with a function call:\n{message.content}\n\n"
            )

        return func_call

    def _get_parser_for(self, function_name: str) -> BaseGenerationOutputParser[M]:
        output_type_iter = filter(
            lambda t: t.__name__.lower() == function_name, self.output_types
        )
        if output_type_iter is None:
            raise OutputParserException(
                f"No parser found for function: {function_name}"
            )
        output_type: Type[M] = next(output_type_iter)

        return PydanticOutputFunctionsParser(pydantic_schema=output_type)


class ParserBaseModel(BaseModel):
    @classmethod
    def output_parser(cls) -> BaseOutputParser[Self]:
        return CustomPydanticOutputParser(pydantic_object=cls)

    @classmethod
    def parse(cls, text: str) -> Self:
        """Override for custom parsing."""
        match = re.search(
            r"\{.*\}", text.strip(), re.MULTILINE | re.IGNORECASE | re.DOTALL
        )
        json_str = ""
        if match:
            json_str = match.group()
        json_object = json.loads(json_str, strict=False)
        return cls.parse_obj(json_object)

    @staticmethod
    def format_instructions() -> str:
        return PYDANTIC_FORMAT_INSTRUCTIONS


P = TypeVar("P", bound=ParserBaseModel)


class CustomPydanticOutputParser(BaseOutputParser[P]):
    pydantic_object: Type[P]

    def parse(self, text: str) -> P:
        try:
            return self.pydantic_object.parse(text)
        except (json.JSONDecodeError, ValidationError) as e:
            raise OutputParserException(
                f"Failed to parse {self.pydantic_object.__name__} from completion {text}. Got: {e}",
                llm_output=text,
            )

    def get_format_instructions(self) -> str:
        reduced_schema = self.pydantic_object.schema()
        if "title" in reduced_schema:
            del reduced_schema["title"]
        if "type" in reduced_schema:
            del reduced_schema["type"]

        return self.pydantic_object.format_instructions().format(
            schema=json.dumps(reduced_schema),
        )

    @property
    def _type(self) -> str:
        return "pydantic"


class CodeBlock(ParserBaseModel):
    code: str
    language: Optional[str] = None

    @classmethod
    def parse(cls, text: str) -> "CodeBlock":
        matches = re.finditer(
            r"```(?P<language>\w+)?\n?(?P<code>.*?)```", text, re.DOTALL
        )
        for match in matches:
            groupdict = match.groupdict()
            groupdict["language"] = groupdict.get("language", None)

            # custom markdown fix
            if groupdict["language"] == "markdown":
                t = text.split("```markdown")[1]
                return cls(
                    language="markdown",
                    code=t[: -(len(t.split("```")[-1]) + 3)],
                )

            return cls(**groupdict)

        return cls(code=text)  # TODO: fix this hack
        raise OutputParserException("Invalid codeblock")

    @staticmethod
    def format_instructions() -> str:
        return "Answer with a codeblock."

    def __str__(self) -> str:
        return self.code
