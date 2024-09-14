def shout():
    '''
    Print a string with three exclamation marks.
    '''
    shout_word = 'congratulations' + '!!!'
    print(shout_word)

shout()

def shout(word):
    '''
    Print shout with a parameter.
    '''
    shout_word = word + '!!!'
    print(shout_word)

shout('hello')

def shout(word):
    '''
    Print shout with a parameter and a word.
    '''
    shout_word = word + '!!!'
    return shout_word

yell = shout('hello')

print(yell)

def shout(word1, word2):
    '''
    Print shout with two parameters.
    '''
    shout_word = word1 + ' ' + word2 + '!!!'
    return shout_word

yell = shout('hello','there')

print(yell)

# Cluster Analysis 

from matplotlib import pyplot as plt

x = [9, 6, 2, 3, 1, 7, 1, 6, 1, 7, 23, 26, 25, 23, 21, 23, 23, 20, 30, 23]
y = [8, 4, 10, 6, 0, 4, 10, 10, 6, 1, 29, 25, 30, 29, 29, 30, 25, 27, 26, 30]

# create a scatter plot
plt.scatter(x , y)
plt.show

# OOP for linear regression 

import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionModel:
    '''
    Plot a linear regression model. 
    '''
    def __init__(self,slope, intercept):
        '''
        Define parameters of a simple linear regression. 
        '''
        self.slope = slope
        self.intercept = intercept

    def generate_dataset(self, x_values):
        '''
        Generate y values based on slope, intercept and noise.
        '''
        y_values = self.slope * x_values + self.intercept 
        return y_values
    
    def plot_dataset(self, x_values,y_values, noisy_y_values):
        '''
        Plot the original and noisy linear regression data.
        '''
        plt.scatter(x_values , y_values , color = 'blue' , label = 'Original Data')
        plt.scatter(x_values, noisy_y_values , color = 'green', label = 'Noisy Data')
        plt.plot(x_values , y_values , color = 'red')
        plt.xlabel('X values')
        plt.ylabel('Y values')
        plt.title('Linear Regression with Noise')
        plt.legend()
        plt.show()

model = LinearRegressionModel(slope=2, intercept=1)
x_values = np.array([1,2,3,4,5])
noise = np.array([2,3,0,-1,1])
y_values = model.generate_dataset(x_values)
noisy_y_values = y_values + noise
model.plot_dataset(x_values,y_values,noisy_y_values)

