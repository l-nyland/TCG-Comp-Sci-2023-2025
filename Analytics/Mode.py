#Finding the Mode = with strings

my_list = [3, 6, 1, 3, 7, 8, 3]

unique_values = []

freq = []

for x in my_list:
    if x not in unique_values:
        unique_values.append(x)

print(unique_values)

for i in unique_values:
    total = my_list.count(i)
    freq.append(total)

print('Frequency = ', freq)

max_freq = max(freq)
mode_index = freq.index(max_freq)
mode = unique_values[mode_index]

print('Mode', mode)

