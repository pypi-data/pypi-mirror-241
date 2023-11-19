import openai
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory

from mmon.tools import load_tools


class Engine:
    def __init__(self, llm, verbose_level=0):
        tools = load_tools(llm)
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        if verbose_level > 2:
            openai.log = "debug"

        self.executor = initialize_agent(
            tools,
            llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=verbose_level > 1,
            memory=memory,
        )

    def run(self, prompt: str) -> str:
        response = self.executor.run(prompt)
        return response
