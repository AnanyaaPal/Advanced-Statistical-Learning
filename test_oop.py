import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    """
    Plots a simple Linear Regression model.
    """
    def __init__(self, slope, intercept):
        """
        Define model parameters.
        """
        self.slope = slope
        self.intercept = intercept

    def generate_values(self, x_values):
        """
        Generate values to plot the model. 
        """
        y_values = self.slope * x_values + self.intercept
        return y_values
    
    def plotting_regression(self, x_values, y_values, y_values_noisy):
        """
        Plot the regression line, with noisy y_values to highlight noise in the data.
        """
        plt.figure(figsize=(10,8))
        if noise is not None:
            y_values_noisy += y_values 
        plt.scatter(x_values, y_values, color= 'Blue', label = 'Original Data')
        plt.scatter(x_values,y_values_noisy,color='Red', label = 'Noisy Data')
        plt.plot(x_values, y_values, color='green', label = 'Fitted Line')
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        plt.title('Linear Regression, with noisy data')
        plt.legend()
        plt.show()

model = LinearRegression(slope = 2, intercept = 3)

x_values = np.array ([13,29,31,41,40,10])

y_values = model.generate_values(x_values)

noise = np.array([10.9,-10,-20,2,1,2])

y_values_noisy = y_values + noise

plot = model.plotting_regression(x_values, y_values, y_values_noisy)

    