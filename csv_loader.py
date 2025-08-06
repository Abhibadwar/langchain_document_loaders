from langchain_community.document_loaders import CSVLoader


loader = CSVLoader(file_path="RAG\Document Loader\Social_Network_Ads.csv", encoding="utf-8")

documents = loader.load()

print(len(documents))
print(documents[1])