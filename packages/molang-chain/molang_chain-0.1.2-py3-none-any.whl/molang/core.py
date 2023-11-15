from typing import Callable
import openai
from molang.models import Memory, Message, BaseModel, OpenAIConfig, OpenAIChatModel, LLMOutputFunctionParser, OpenAIFunction, ChainFunc, PromptChain

# Core DSL primitive
# _do and _else should always return a promptchain object
def condition(func: Callable[[Memory], bool], _do, _else):
    """Closure to add a conditional branching. ran on last message"""
    def _inner(memory: Memory):
        if not isinstance(memory, Memory):
            actual_type = type(memory).__name__
            raise TypeError(f"Expected monadic input to be of type Memory, got {actual_type}")
        return _do(memory) if func(memory) else _else(memory)
    return _inner

def eqs(expected: str):
    """Closure to check the last message's content."""
    def _inner(memory: Memory):
        return memory.messages[-1].content == expected
    return _inner

def evaluate(instruction: Message, output: BaseModel, on_all_msgs = False):
    """take in a message that is supposed to be the statements instruction, cast result to pydantic output"""
    def _inner(memory: Memory) -> bool:
        config = OpenAIConfig(
            api_key=openai.api_key,
            organization="",
            model=OpenAIChatModel.GPT_4_0613,
            temperature=0.5,
            parser=LLMOutputFunctionParser(output),
        )
        oaf = OpenAIFunction(config)
        if on_all_msgs:
            for m in memory.messages:
                oaf.apply_msg(m)
        else:
            oaf.apply_msg(memory.messages[-1])
        oaf.apply_msg(instruction) # apply the last message
        truth = oaf.execute_and_parse()
        return truth.output
    return _inner

def stream(*funcs: ChainFunc):
    def _inner(memory: Memory):
        if memory is None:
            raise ValueError("The Promptchain memory does not exist")
        if not isinstance(memory, Memory):
                actual_type = type(memory).__name__
                raise TypeError(f"Expected monadic input to be of type Memory, got {actual_type}")
        new_chain = PromptChain(memory)
        for func in funcs:
            # short circuit on error
            if new_chain.error:
                return new_chain
            new_chain = new_chain | func
        return new_chain
    return _inner

def do_while(stream: ChainFunc, exit_on: Callable[[Memory], bool]):
    """break out of while loop on last message that evaluate to True"""
    def _inner(memory: Memory):
        if memory is None:
            raise ValueError("The Promptchain memory does not exist")
        if not isinstance(memory, Memory):
                actual_type = type(memory).__name__
                raise TypeError(f"Expected monadic input to be of type Memory, got {actual_type}")
        new_chain = PromptChain(memory)
        while not exit_on(memory):
            # short circuit on error
            if new_chain.error:
                return new_chain
            tc = stream(new_chain.memory)
            new_chain = PromptChain(memory=Memory(messages=tc.memory.messages, state=tc.memory.state), error= tc.error, stacktrace=tc.stacktrace)
        return new_chain
    return _inner

