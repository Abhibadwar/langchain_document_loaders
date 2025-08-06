from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader = DirectoryLoader(
    path="Book", 
    glob="*.pdf", 
    loader_cls=PyPDFLoader
)

documents = loader.lazy_load()

for doc in documents:
    print(documents.metadata)


