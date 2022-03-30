import streamlit as st
from PIL import Image

logo = Image.open("assets/favicon.png")
def main():
    st.set_page_config(
        layout="wide", page_title="Survey System", page_icon = logo)
    
    st.markdown("# Survey Dashboard")


if __name__ == '__main__':
    main()


