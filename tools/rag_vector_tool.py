import os
import pandas as pd
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

class RAGVectorTool:
    def __init__(self, csv_path='data/knowledge_base.csv', faiss_dir='vector_store/faiss_index'):
        self.csv_path = csv_path
        self.faiss_dir = faiss_dir
        self.embedding = OpenAIEmbeddings()
        self.vectorstore = self._load_or_create_faiss()

    def _load_or_create_faiss(self):
        # ✅ Safe load if FAISS index exists
        if os.path.exists(self.faiss_dir):
            return FAISS.load_local(
                folder_path=self.faiss_dir,
                embeddings=self.embedding,
                allow_dangerous_deserialization=True  # ✅ Allow if you trust the file
            )
        else:
            # ✅ Load from CSV and create FAISS index
            df = pd.read_csv(self.csv_path)

            # ✅ Validate expected columns
            if 'description' not in df.columns:
                raise ValueError("❌ 'description' column is required in the CSV file.")
            
            documents = []
            for _, row in df.iterrows():
                text = ''
                if 'company' in row:
                    text += f"{row['company']}: "
                text += str(row['description'])
                documents.append(Document(page_content=text))

            vectorstore = FAISS.from_documents(documents, self.embedding)
            vectorstore.save_local(self.faiss_dir)
            return vectorstore

    def query(self, query_text, k=3):
        results = self.vectorstore.similarity_search(query_text, k=k)
        return [doc.page_content for doc in results]

from langchain.tools import Tool

rag_tool_instance = RAGVectorTool()

rag_tool = Tool(
    name="RAG Vector Search Tool",
    func=lambda q: "\n".join(rag_tool_instance.query(q)),
    description="Use this tool to retrieve knowledge from the embedded CSV using vector similarity. Input should be a user query string."
)
