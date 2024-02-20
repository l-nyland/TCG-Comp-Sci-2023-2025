import matplotlib.pyplot as plt

cars_colours = ['red', 'green', 'black', 'silver', 'white']

freq = [10, 1, 8, 4, 5]

plt.title('Cars in the Carpark')

plt.pie(freq, labels = cars_colours)

plt.show()

