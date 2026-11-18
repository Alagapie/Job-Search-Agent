from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import  load_dotenv
from langchain_groq import ChatGroq
from tavily import TavilyClient
load_dotenv()
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field 
# tavily = TavilyClient()



# @tool
# def search(query: str) -> str:
#     """
#     args:
#         query: the user question to search forn
        
#     returns:
#         the answer to the user question"""
#     print(f"searching for {query}")
#     result = tavily.search(query)
#     return result
class Source(BaseModel):
    """ Scheme for a source used by the agent"""
    url: str = Field(description= "the URL of the source")
class AgentResponse(BaseModel):
    """Scheme for the agent response"""
    answer:str = Field(description="the answer to the user question")
    sources: List[Source] = Field(default_factory=list,description="the sources used to answer the user question")
llm = ChatGroq(model='openai/gpt-oss-120b')
tools= [TavilySearch()]
agent= create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    response = agent.invoke({'messages':[
        HumanMessage(content="I need you to search for 3 different AI roles currently open in Nigeria, and UAE")]
        })
    print(response)

if __name__ == "__main__":
    main()



    