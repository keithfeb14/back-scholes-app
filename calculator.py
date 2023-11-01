import streamlit as st
import bs
from scipy.stats import norm
import numpy as np
import visualisation as vz
import time

        

# Main function for your Streamlit app
def calculator():
    st.title('Option Pricing Calculator')

    # Input fields
    st.sidebar.header('Input Parameters')
    S = st.sidebar.number_input('Stock Price', 1, 10000, 100)  
    K = st.sidebar.number_input('Strike Price', 1, 10000, 100)  
    sigma = st.sidebar.slider('Volatility (%)', 0, 100, 30)  / 100
    T = st.sidebar.number_input('Time to Maturity (in days)', 1, 365, 30) / 365.0
    r = st.sidebar.number_input('Risk-Free rate (%)', 0, 100, 5) / 100
    option = st.sidebar.selectbox('Option Type', ['Call', 'Put'])


    # perform calculation
    calculate = st.sidebar.button('Calculate')

    # Output section

    
    if calculate:
        if option == 'Call':
            option_type = "c"
        else:
            option_type = "p"
        
        with st.spinner('Computing option pricing metrics...'):
          time.sleep(2)
        st.success('Completed')

        st.header('Output')
        
        price = bs.blackScholes(r, S, K, T, sigma, type=option_type)
        delta = bs.delta_calc(r, S, K, T, sigma, type=option_type)
        gamma = bs.gamma_calc(r, S, K, T, sigma, type=option_type)
        vega = bs.vega_calc(r, S, K, T, sigma, type=option_type)
        theta = bs.theta_calc(r, S, K, T, sigma, type=option_type)
        rho = bs.rho_calc(r, S, K, T, sigma, type=option_type)
        excedence = bs.probability_exceedance(r, S, K, T, sigma, type=option_type)

        price = round(price, 5)
        delta = round(delta, 5)
        gamma = round(gamma, 5)
        vega = round(vega, 5)
        theta = round(theta, 5)
        rho = round(rho, 5)


        # Displaying results
        st.subheader('Option Price')
        st.write(f"Option price: ${price} with the probability of exceedance of {excedence}%")

        st.subheader('Greeks')

        st.write(f"**Delta:** {delta}")
        st.info("""
        Delta measures the sensitivity of the option's price to changes in the underlying asset's price. 
        A Delta of 0.5 means the option's price will move approximately \$0.50 for a \$1 move in the underlying asset.
        """)

        st.write(f'Gamma: {gamma}')
        st.info("""
        **Gamma**: Measures the rate of change of the option's Delta with respect to changes in the underlying asset's price.
        A Gamma of 0.05 indicates that for a \$1 move in the underlying asset, the Delta will change by 0.05.
        """)

        st.write(f'Vega: {vega}')
        st.info("""
        **Vega**: Measures the sensitivity of the option's price to changes in volatility.
        A Vega of 0.20 means the option's price will move approximately \$0.20 for a 1% increase in volatility.
        """)

        st.write(f'Theta: {theta}')
        st.info("""
        **Theta**: Indicates how much the option's price will decrease for a one-day reduction in time to expiration, all else being equal.
        A Theta of -0.05 means the option's price will decrease by approximately \$0.05 for every day that passes.
        """)

        st.write(f'Rho: {rho}')
        st.info("""
        **Rho**: Measures the sensitivity of the option's price to changes in the interest rate.
        A Rho of 0.25 indicates that the option's price will move approximately \$0.25 for a 1% increase in interest rates.
        """)


        # Plotting the sensitivity grpahs 

        st.header('Greek sensitivity')
        st.subheader('Delta')
        delta_plot = vz.plot_delta_sensitivity(r, K, T, sigma, option_type.lower())
        st.pyplot(delta_plot)

        st.subheader('Gamma')
        gamma_plot = vz.plot_gamma_sensitivity(r, K, T, sigma, option_type.lower())
        st.pyplot(gamma_plot)

        st.subheader('Vega')
        sigma_range = np.linspace(0.1, 0.5, 100)
        T_range = np.linspace(1/365, 3, 100)
        vega_plot = vz.plot_vega_sensitivity_to_time_and_vol(r, S, K, sigma, sigma_range, T, T_range, option_type.lower())
        st.pyplot(vega_plot)

        st.subheader('Theta')
        theta_plot = vz.plot_theta_sensitivity_to_time_and_vol(r, S, K, sigma_range=sigma_range, T_range=T_range, option_type=option_type.lower())
        st.pyplot(theta_plot)

        st.subheader('Rho')
        rho_plot = vz.plot_rho_sensitivity_to_time_and_vol(r, S, K, sigma_range=sigma_range, T_range=T_range, option_type=option_type.lower())
        st.pyplot(rho_plot)

        
        