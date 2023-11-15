import traceback
import openai
import json
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Callable, Optional, NamedTuple, Protocol, Dict, Any, Iterator, Union
from dataclasses import dataclass, asdict
from dotenv import load_dotenv
import os

from abc import ABC, abstractmethod

def load_api_key():
    openai.api_key = os.getenv("openai_key")

class OpenAIChatModel(Enum):
    GPT_35_TURBO = "gpt-3.5-turbo"
    GPT_35_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT_4 = "gpt-4"
    GPT_4_0613 = "gpt-4-0613"
    GPT_4_0314 = "gpt-4-0314"
class Message(NamedTuple):
    """Message type containing role and content."""
    role: str
    content: str

Messages = List[Message]

class Memory:
    def __init__(self, messages: Messages = [], state: Union[BaseModel, None] = None):
        self.messages: Messages = messages
        self.state: Union[BaseModel, None] = state

    def __iter__(self) -> Iterator[Message]:
        return iter(self.messages)

class LLMOutputParser(Protocol):
    def parse(self, msg: Dict[str, Any]) -> BaseModel:
        ...

    def get_pydantic_model(self) -> BaseModel:
        ...


class LLMOutputFunctionParser:
    """
    generic parser for all openai function type definition with pydantic support
    accept any pydantic model input and enforce output data type
    """

    def __init__(self, output_class: BaseModel) -> None:
        self.output_class = output_class

    def get_pydantic_model(self) -> BaseModel:
        return self.output_class

    def parse(self, res: dict) -> BaseModel:
        """
        openai function will always return JSON doc string
        """
        escaped_json = res["function_call"]["arguments"].replace('\n\n', '\\n\\n')
        output_json = json.loads(escaped_json)
        return self.output_class(**output_json)


@dataclass
class OpenAIConfig:
    """
    Data class to store the configuration settings for an OpenAI API call.
    This includes the API key, the model to be used, an optional organization,
    and an optional temperature setting.

    parser accept a parser function that parses LLM response into pydantic data model
    """

    api_key: str
    model: OpenAIChatModel
    parser: LLMOutputParser
    organization: Optional[str] = None
    temperature: Optional[float] = None

class OpenAIHandler:
    """
    Abstract class to handle OpenAI API calls.
    """

    def __init__(self, config: OpenAIConfig):
        """
        Initializes OpenAI API key, model, messages list, temperature, and organization based on config.
        """
        openai.api_key = config.api_key
        self.model = config.model
        self.messages: Messages = []
        self.temperature = config.temperature
        self.parser = config.parser
        if config.organization:
            openai.organization = config.organization
        openai.api_key = config.api_key

    def apply_msg(self, message: Message):
        """
        Validates that the message is an instance of 'Message' class and adds it to the messages list.
        """
        if not isinstance(message, Message):
            raise TypeError(f"'message' must be an instance of 'Message' class. got {message}")
        self.messages.append(message)

    def get_msgs(self) -> Messages:
        """
        Returns the list of messages.
        """
        return self.messages

    @abstractmethod
    def execute(self):
        """
        Abstract execute method, required for performing inference
        """
        pass


@dataclass
class OpenAIFunctionAPI:
    """
    Data class to store the information about an OpenAI's Function API call.
    This includes the function name, a description, and a dictionary of parameters.
    """

    name: str
    description: str
    parameters: dict
    
class OpenAIFunction(OpenAIHandler):
    """
    Subclass of OpenAIHandler for handling OpenAI Function API calls.
    Automatically handles JSON serialization of LLM output into Pydantic data format
    Note: only accept a single function and taking OpenAI's function call's
    arguments as its final returned output
    """

    def execute(self) -> dict:
        schemas = self.parser.get_pydantic_model().model_json_schema()
        schemas_api = OpenAIFunctionAPI(
            name=schemas["title"],
            description=schemas["description"],
            parameters=schemas,
        )
        response = openai.ChatCompletion.create(
            model=self.model.value,
            messages=[message._asdict() for message in self.messages],
            temperature=self.temperature,
            functions=[asdict(schemas_api)],
        )
        return response

    def parse_response(self, response: dict) -> BaseModel:
        """
        Parses the response from an OpenAI Function API call into an output_class instance.
        """
        msg = response.choices[0].message
        output_parsed = self.parser.parse(msg)
        return output_parsed

    def execute_and_parse(self) -> BaseModel:
        """
        Executes an OpenAI Function API call, parses the response, and returns an output_class instance.
        will automatically perform retry attempt in case output parsing fails
        """
        response = self.execute()
        return self.parse_response(response)

class Boolean(BaseModel):
    """
    it simply takes the previous statement- the last message, and subjectively evaluates to true or false
    for example, if the previous answer is 'no I dont think so', then output is false, if the answer is 'Agree!' then apply output arg to True
    """

    output: bool = Field(
        description="evaluate to either True or False"
    )


class PromptChain:
    """Monadic structure for chaining prompts and responses."""
    def __init__(self, memory: Memory = Memory(), error: Optional[str] = None, stacktrace: Optional[str] = None):
        self.memory = memory
        self.error = error
        self.stacktrace = stacktrace
	
    def bind(self, func: Callable[[List[Message]], 'PromptChain']) -> 'PromptChain':
        """Bind a function to the prompt chain, short-circuiting on error."""
        if self.error:
            return self
        try:
            if self.memory is None:
                raise ValueError("The Promptchain memory does not exist")
            if not isinstance(self.memory, Memory):
                actual_type = type(self.memory).__name__
                raise TypeError(f"Expected monadic input to be of type Memory, got {actual_type}")
            return func(self.memory)
        except Exception as e:
            stacktrace = traceback.format_exc()
            return PromptChain(self.memory, error=str(e), stacktrace=stacktrace)

    def __or__(self, func):
        """Syntactic sugar for bind."""
        return self.bind(func)

ChainFunc = Callable[[Memory], PromptChain]
