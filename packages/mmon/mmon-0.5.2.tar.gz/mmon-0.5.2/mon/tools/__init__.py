from langchain.agents import Tool, initialize_agent
from langchain.chains import LLMMathChain
from langchain.llms import OpenAI


def load_tools(llm, verbose=False):
    return [
        Tool(
            name="Calculator",
            func=LLMMathChain.from_llm(llm=llm, verbose=verbose).run,
            description="useful for when you need to answer questions about math",
        ),
    ]
