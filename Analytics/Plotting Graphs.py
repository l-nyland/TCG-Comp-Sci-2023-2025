import random
import matplotlib.pyplot as plt

value = random.randint(1, 100)

data_set = []

for i in range(1, 100):
    value = str(random.randint(1, 100))
    data_set.append(value)
    
print(data_set)

plt.plot(data_set)
plt.show()

#this is a stupid graph to plot!
