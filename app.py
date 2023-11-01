import streamlit as st
import introduction as intro
import calculator as cal

def main():

    page_selection = st.sidebar.radio("Choose a Page", ["Introduction", "Option Pricing Calculator"])

    if page_selection == "Introduction":
        intro.introduction()
    else:
        cal.calculator()

if __name__ == "__main__":
    main()
