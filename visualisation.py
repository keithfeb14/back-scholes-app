import numpy as np 
import matplotlib.pyplot as plt
import bs


def plot_delta_sensitivity(r, K, T, sigma, option_type):
    stock_prices = np.linspace(0.5 * K, 1.5 * K, 100)
    deltas = [bs.delta_calc(r, S, K, T, sigma, type=option_type) for S in stock_prices]

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, deltas, '-b', label='Delta')
    plt.title('Delta Sensitivity to Stock Price')
    plt.xlabel('Stock Price')
    plt.ylabel('Delta')
    plt.legend()
    plt.grid(True)
    return plt

def plot_gamma_sensitivity(r, K, T, sigma, option_type):
    stock_prices = np.linspace(0.5 * K, 1.5 * K, 100)
    gammas = [bs.gamma_calc(r, S, K, T, sigma, type=option_type) for S in stock_prices]

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, gammas, '-g', label='Gamma')
    plt.title('Gamma Sensitivity to Stock Price')
    plt.xlabel('Stock Price')
    plt.ylabel('Gamma')
    plt.legend()
    plt.grid(True)
    return plt



def plot_vega_sensitivity_to_time_and_vol(r, S, K, current_sigma, sigma_range, current_T, T_range, option_type):
    vega_time = [bs.vega_calc(r, S, K, T, current_sigma, type=option_type) for T in T_range]
    vega_vol = [bs.vega_calc(r, S, K, current_T, sigma, type=option_type) for sigma in sigma_range]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

    ax1.plot(T_range, vega_time, '-b', label='Vega')
    ax1.set_title('Vega Sensitivity to Time to Expiry')
    ax1.set_xlabel('Time to Expiry')
    ax1.set_ylabel('Vega')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(sigma_range, vega_vol, '-r', label='Vega')
    ax2.set_title('Vega Sensitivity to Volatility')
    ax2.set_xlabel('Volatility (sigma)')
    ax2.set_ylabel('Vega')
    ax2.legend()
    ax2.grid(True)

    return plt


def plot_theta_sensitivity_to_time_and_vol(r, S, K, sigma_range, T_range, option_type):

    # Calculate Theta for varying time to expiration
    theta_time = [bs.theta_calc(r, S, K, T, sigma_range[0], type=option_type) for T in T_range]
    
    # Calculate Theta for varying volatilities
    theta_vol = [bs.theta_calc(r, S, K, T_range[0], sigma, type=option_type) for sigma in sigma_range]
    
    # Create a new figure and set of subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Theta vs. Time to Expiration
    axs[0].plot(T_range, theta_time, 'b-')
    axs[0].set_title("Theta vs. Time to Expiration")
    axs[0].set_xlabel("Time to Expiration")
    axs[0].set_ylabel("Theta")

    # Theta vs. Volatility
    axs[1].plot(sigma_range, theta_vol, 'r-')
    axs[1].set_title("Theta vs. Volatility")
    axs[1].set_xlabel("Volatility (sigma)")
    axs[1].set_ylabel("Theta")

    plt.tight_layout()
    
    return fig  


def plot_rho_sensitivity_to_time_and_vol(r, S, K, sigma_range, T_range, option_type):

    # Calculate Rho for varying time to expiration
    rho_time = [bs.rho_calc(r, S, K, T, sigma_range[0], type=option_type) for T in T_range]
    
    # Calculate Rho for varying volatilities
    rho_vol = [bs.rho_calc(r, S, K, T_range[0], sigma, type=option_type) for sigma in sigma_range]
    
    # Create a new figure and set of subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Rho vs. Time to Expiration
    axs[0].plot(T_range, rho_time, 'b-')
    axs[0].set_title("Rho vs. Time to Expiration")
    axs[0].set_xlabel("Time to Expiration")
    axs[0].set_ylabel("Rho")

    # Rho vs. Volatility
    axs[1].plot(sigma_range, rho_vol, 'r-')
    axs[1].set_title("Rho vs. Volatility")
    axs[1].set_xlabel("Volatility (sigma)")
    axs[1].set_ylabel("Rho")

    plt.tight_layout()
    
    return fig  # Return the figure