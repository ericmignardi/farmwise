from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from .llm import get_llm


def get_vectorstore():
    # Local embeddings - no API rate limits!
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory="./chroma_db", embedding_function=embeddings)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_farm_context_chain():
    retriever = get_vectorstore().as_retriever(search_kwargs={"k": 5})
    llm = get_llm()

    template = """You are a helpful farming assistant for FarmWise.
    Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Keep the answer informative but structured (use bullet points).

    Context:
    {context}

    Question: {question}

    Helpful Answer:"""

    prompt = ChatPromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
