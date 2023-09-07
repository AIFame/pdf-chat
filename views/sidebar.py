import streamlit as st
from icecream import ic

from utils.ai.open_ai import get_text_chunk, get_vectorstore_openAI
from utils.inputs import pdf


def sidebar():
    with st.sidebar:
        st.subheader('Your PDF documents')
        pdf_docs = st.file_uploader(
            "Upload your pdfs here and click on 'Proces'", accept_multiple_files=True, type=['pdf'],
        )
        # if the button is pressed
        if st.button('Process'):
            with st.spinner('Processing'):
                # get pdf text
                data = pdf.extract(pdf_docs)
                ic('pdfs have been reading into data')

                # Use loader and data splitter to make a documentlist
                doc = get_text_chunk(data)
                ic(f'text_chunks are generated and the total chucks are {len(doc)}')

                # create vector store
                vectorstore = get_vectorstore_openAI(doc)
