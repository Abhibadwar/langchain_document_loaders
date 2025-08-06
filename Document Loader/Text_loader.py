from langchain.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary fro following poem - \n {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()


loader = TextLoader("RAG/Document Loader/cricket.txt", encoding="utf-8")

documents = loader.load()

print(documents)
print(type(documents))
print(len(documents))
print(documents[0])
print(documents[0].page_content)
print(documents[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"poem": documents[0].page_content}))