from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="answer the following question  \n {question}  from the following text - \n {text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()


url = "https://www.flipkart.com/apple-macbook-air-m2-8-gb-512-gb-ssd-mac-os-monterey-mlxx3hn-a/p/itmc2732c112aeb1?pid=COMGFB2GNWNN9DN8&lid=LSTCOMGFB2GNWNN9DN8OLT676&marketplace=FLIPKART&q=apple+macbook&store=6bo%2Fb5g&srno=s_1_2&otracker=AS_Query_OrganicAutoSuggest_7_9_na_pm_na&otracker1=AS_Query_OrganicAutoSuggest_7_9_na_pm_na&fm=organic&iid=bb6ea425-d78d-403c-8fc9-c215dff8d829.COMGFB2GNWNN9DN8.SEARCH&ppt=browse&ppn=browse&ssid=npqlw76yy80000001748097578188&qH=f9b17f2552f8c1a5"
loader = WebBaseLoader(url)

documents = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question': 'What is the product that we are talking about?' ,'text':documents[0].page_content})

print(result)