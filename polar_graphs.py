
import numpy as np 
import matplotlib.pyplot as plt 
  
  
# Setting the projection of the axes as polar 
plt.axes(projection = 'polar') 

def plot_circle(radius):   
    # creating a list containing the 
    # radian values
    radians = np.arange(0, (2 * np.pi), 0.01) 
    
    # plotting the circle 
    for rad in radians: 
        plt.polar(rad, radius, 'r.') 
    
    # display the polar plot of a circle
    plt.show()

def plot_rhodonea(length, number_of_petals):
    # creating a list
    # containing the radian values 
    radians = np.arange(0, 2 * np.pi, 0.001)  
    
    # plotting the rose 
    for rad in radians: 
        r = length * np.cos(number_of_petals*rad) 
        plt.polar(rad, r, 'g.') 
    
    # display the polar of the rose
    plt.show() 


if __name__ == '__main__':
    # plot_circle(2)
    plot_rhodonea(1, 6)
