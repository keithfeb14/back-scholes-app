import streamlit as st

def introduction():
    st.title('Introduction to Black-Scholes and the Greeks')

    st.header('Black-Scholes Model')
    st.write('''
    The Black-Scholes model, developed by Fischer Black, Myron Scholes, and Robert Merton in the early 1970s, 
    is a widely-used mathematical model to calculate the theoretical value of European-style options. 
    It is based on a number of factors, including the current stock price, the option strike price, 
    time until expiration, implied volatility, and the risk-free interest rate.
    ''')

    st.header('The Greeks')
    st.write('''
    The Greeks are mathematical tools that help us measure the sensitivity of an option's price to various factors. 
    They include:
    - **Delta**: Measures the rate of change of the option's price with respect to changes in the underlying stock's price.
    - **Gamma**: Measures the rate of change of Delta with respect to changes in the underlying stock's price.
    - **Theta**: Represents the rate of change of the option's price with respect to time.
    - **Vega**: Indicates how much the option's price is expected to change for a 1% change in the underlying stock's volatility.
    - **Rho**: Measures the sensitivity of the option's price to a change in the risk-free interest rate.
    ''')

    st.write('''
    By understanding these Greeks, traders can better anticipate how changes in market conditions can impact 
    the price of the option.
    ''')
