import copy

d = {
    'a1': 1,
    'a2': 2,
    'l1': [0, 1, 2]
}

# d2 = copy.copy(d)  # Shallow copy
d2 = copy.deepcopy(d)  # Deep copy

d2['a1'] = 'banana'
d2['l1'][1] = 'banana'

print(d)
print(d2)
