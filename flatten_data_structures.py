## Method to flatten a nested dictionary
def dflatten(dd, paren_k='', sep='-'):
    res = []
    for key, val in dd.items():
        if paren_k:
            new_key = paren_k + sep + key
        else:
            new_key = key

        if type(val) == dict:
            res.extend(dflatten(val, new_key, '-').items())
        else:
            res.append((new_key, val))
    return dict(res)


## Method to flatten a nested list
def lflatten(ll, result):
    for item in ll:
        if type(item) == list:
            lflatten(item, result)
        else:
            result.append(item)


## Calling the method to flatten a nested list
ll = [2, 3, [5, 6, [7, 8], 9 ], 1 ]
result = []
lflatten(ll, result)
print(result)

## Calling the method to flatten a nested dict
dd = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': 3}
print(dflatten(dd))

