
import streamlit as st
import openai
import os
import json

from langchain import OpenAI

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader ,GPTListIndex, ServiceContext, LLMPredictor
from llama_index import StorageContext, load_index_from_storage


openai.api_key = os.getenv("OPENAI_API_KEY")



but = st.button("Create Index")
if but:

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=3500))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    folder_name = "data"
    path = os.path.join(".", folder_name)

    documents = SimpleDirectoryReader(path).load_data()
    index = GPTListIndex.from_documents(documents,service_context=service_context)
    index.storage_context.persist()
    storage_context = StorageContext.from_defaults(persist_dir="./storage")


    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(f"Generate a Persona document for the following information, exclude names: {st.session_state.persona_prompt}")

    st.write(response)
