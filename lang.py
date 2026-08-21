from langchain_community import document_loaders
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM

#data ingestion
loader=PyPDFLoader("resume.pdf")
texts=loader.load()

#data extraction
split_text=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs=split_text.split_documents(texts)


#embeddings
embeddings=OllamaEmbeddings(model="nomic-embed-text")

#vector store db
db=Chroma.from_documents(docs,embeddings)


#llm
llm=OllamaLLM(model="llama3.2:1b")


#user query
query = "what is this pdf about"

#similarity search
result=db.similarity_search_with_score(query,k=2)


#context
context="\n\n".join(doc.page_content for doc,score in result)


#prompt
prompt=f'''
Answer the question using only the context below.

context:{context}

question:{query}

answer:
'''

response=llm.invoke(prompt)
print(response)