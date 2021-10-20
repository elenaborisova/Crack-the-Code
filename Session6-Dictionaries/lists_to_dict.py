# Exercise 1: Below are the two lists convert it into the dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
keys_values_dict = {}


for i in range(len(keys)):
    keys_values_dict[keys[i]] = values[i]


print(keys_values_dict)
