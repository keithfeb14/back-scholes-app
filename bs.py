#implementing the black-scholes formula
import numpy as np
from scipy.stats import norm

'''
#define variables 
r = 0.01 #interest rate (1%) 
S = 30 #underlying ($30)
K = 40 #strike ($40)
T = 240/365 #240 days out 365
sigma = 0.30 #volatility (30%)
'''

def blackScholes(r, S, K, T, sigma, type="c"):
    "Calculate BS optioin price for a call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            price = S*norm.cdf(d1, 0, 1) - K *np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return round(price,2)
    except: 
        print("Please confirm all option parameters")

#print("Option price is: ", blackScholes(r, S, K, T, sigma, type="C"))


'''

Delta measures the rate of change of the theoretical option value with respect to changes in the underlying asset's price.

'''

def delta_calc(r, S, K, T, sigma, type="c"):
    "Calculate delta of an option"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    try:
        if type == "c":
            delta_calc = norm.cdf(d1, 0, 1)
        elif type == "p":
            delta_calc = -norm.cdf(-d1, 0, 1)
        return delta_calc
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
        

        
	

'''
Gamma measures the rate of change in the delta with respect to changes in the underlying price.

'''

def gamma_calc(r, S, K, T, sigma, type="c"):
    "Calculate gamma of a option"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        gamma_calc = norm.pdf(d1, 0, 1)/(S*sigma*np.sqrt(T))
        return gamma_calc
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
        



'''
Vega measures sensitivity to volatility. Vega is the derivative of the option value with respect 
to the volatility of the underlying asset.

'''

def vega_calc(r, S, K, T, sigma, type="c"):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        vega_calc = S*norm.pdf(d1, 0, 1)*np.sqrt(T)
        return vega_calc*0.01
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
        

        
'''
Theta measures the sensitivity of the value of the derivative to the passage of time - time decay.

'''

def theta_calc(r, S, K, T, sigma, type="c"):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            theta_calc = -S*norm.pdf(d1, 0, 1)*sigma/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            theta_calc = -S*norm.pdf(d1, 0, 1)*sigma/(2*np.sqrt(T)) + r*K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return theta_calc/365
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
        

        

'''
Rho measures the sensitivity to the interest rate.

'''

def rho_calc(r, S, K, T, sigma, type="c"):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "c":
            rho_calc = K*T*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "p":
            rho_calc = -K*T*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return rho_calc*0.01
    except:
        print("Please confirm option type, either 'c' for Call or 'p' for Put!")
        


def probability_exceedance(r, S, K, T, sigma, type="c"):
    """
    Calculate the probability of exceedance, i.e., the option expiring in the money.
    This is a simplified approach that doesn't account for changes in volatility or interest rates.
    """
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # For a call option, this is the probability that the underlying asset
    # will exceed the strike price at expiration.
    # For a put option, it's the probability that the asset's price will fall below the strike price.
    if type == "c":
        prob_exceed = norm.cdf(d2, 0, 1)  # For call option
    elif type == "p":
        prob_exceed = norm.cdf(-d2, 0, 1)  # For put option
    else:
        raise ValueError("Please specify correct option type, 'c' for Call or 'p' for Put!")

    return round(prob_exceed, 2)
