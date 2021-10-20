# Exercise 3: Delete set of keys from a dictionary

sample_dict = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New york'

}

keys = ['name', 'salary']

for key in keys:
    # value = sample_dict.pop(key, 'not found')  # pop returns value; del does not
    # print(value)
    del sample_dict[key]


print(sample_dict)

