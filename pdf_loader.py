from langchain_community.document_loaders import PyPDFLoader,PyMuPDFLoader,UnstructuredPDFLoader
loader = PyPDFLoader("RAG/Document Loader/Statistics Notes.pdf")


documents = loader.load()

print(documents)
print(type(documents))
print(len(documents))
print(documents[0])
print(documents[0].page_content)
print(documents[0].metadata)