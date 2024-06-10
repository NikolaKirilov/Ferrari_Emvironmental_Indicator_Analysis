import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Constants
GHP_W = 0.026315  # Greenhouse gas emissions per capita
CDA_W = 0.36317  # Adjusted emissions growth rate for carbon dioxide
GHN_W = 0.36317  # Projected GHG emissions in 2040

weights = {"GHP_W": GHP_W, "CDA_W": CDA_W, "GHN_W": GHN_W}

def calculate_indicator_score(x, w, b):
    """
    Calculate an indicator score based on the given company score (x), weight (w), and panel (b).

    This function calculates an indicator score using the formula: (x - w) / (b - w) / 100.

    Parameters:
    x (float): The company score.
    w (float): The weight. 
    b (float): The panel. 

    Returns:
    float: The calculated indicator score.
    """
    return ((x - w) / (b - w) / 100)

def exponential_fit(x, a, b, c):
    """
    This function performs an exponential fit on the given data.

    The function uses the formula: y = a * exp(-b * x) + c.

    Parameters:
    x (array-like): The independent variable. 
    a (float): The coefficient of the exponential term.
    b (float): The rate of decay or growth.
    c (float): The coefficient of the constant term. 

    Returns:
    float: The fitted value of y for the given value of x.
    """
    return a * np.exp(-b * x) + c

def project_ghg_emissions(x, y, num_future_steps):
    """
    This function projects greenhouse gas (GHG).

    The function uses an exponential fit to project the GHG emissions.

    Parameters:
    x (array-like): The independent variable (time). 
    y (array-like): The dependent variable (GHG emissions). 
    num_future_steps (int): The number of time steps to project into the future. 

    Returns:
    array-like: The projected GHG emissions for the given number of time steps.
    """
    fitting_parameters, covariance = curve_fit(exponential_fit, x, y)
    a, b, c = fitting_parameters
    future_x = np.arange(x[-1] + 1, x[-1] + num_future_steps + 1)
    future_y = exponential_fit(future_x, a, b, c)
    return future_y

def calculate_ghn_score(y, future_y, num_steps):
    """
    This function calculates the GHN score.

    The GHN score is calculated as: (y[0] / future_y[-1]) ** (1/num_steps) - 1.

    Parameters:
    y (array-like): The historical GHG emissions.
    future_y (array-like): The projected GHG emissions.
    num_steps (int): The difference in steps between y and future_y.

    Returns:
    float: The calculated GHN score.
    """
    return (y[0] / future_y[-1]) ** (1/num_steps) - 1

def calculate_epi(scores, weights=15.9997, N_weights=54):
    """
    This function calculates the adjusted Environmental Performance Index (EPI).

    The EPI is calculated as: score_sum * (weights / N_weights) / (score_sum / N_score).

    Parameters:
    scores (dict): A dictionary containing the scores for each indicator. 
    weights (float): The total weight of all indicators. The default is 15.9997.
    N_weights (int): The number of indicators. The defualt is 54.

    Returns:
    float: The calculated EPI.
    """
    score_sum = sum(scores.values())
    N_score = len(scores)
    return score_sum * (weights / N_weights) / (score_sum / N_score)

def main():
    # GHP
    GHP_B = 29480000 / 548565
    GHP_X = 598000 / 13221
    GHP = calculate_indicator_score(GHP_X, GHP_W, GHP_B)

    # CDA
    CDA_B = ((74030000 / 29480000) ** (1/30) - 1)
    CDA_X = ((93243 / 78059) ** (1/6) - 1)
    CDA = calculate_indicator_score(CDA_X, CDA_W, CDA_B)

    # GHN
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([95514, 88242, 93789, 91001, 91789, 92319])
    future_y = project_ghg_emissions(x, y, 18)
    num_steps = 24
    GHN = calculate_ghn_score(y, future_y, num_steps)

    # Create a DataFrame
    scores = {"GHP": GHP, "CDA": CDA, "GHN": GHN}
    df = pd.DataFrame(list(scores.items()), columns=["index", "score"])
    df.set_index("index", inplace=True)

    # Calculate EPI
    epi = calculate_epi(scores, weights=15.9997, N_weights=54)
    print(f"EPI: {round(epi * 100, 2)}")

    # Plot
    plt.plot(y)
    plt.plot(np.append(y, future_y), 'ro')
    plt.show()
    #plt.savefig("CO2Predicted2040.png")

if __name__ == "__main__":
    main()