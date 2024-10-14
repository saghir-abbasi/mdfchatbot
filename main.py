import streamlit as st
from chains import Chain

def create_streamlit_app(llm):
    st.title("My ChatGPT")
    text_input = st.text_input("Enter message:")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            res = llm.write_res(text_input)
            st.write(res)
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="My ChatGPT")
    create_streamlit_app(chain)