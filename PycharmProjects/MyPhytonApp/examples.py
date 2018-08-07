#given a list of tuple search for value in it and return the value associated with the first element of the pair
def search_list(list_of_tuples, value):
    for element in list_of_tuples:
        if element[0] == value:
            return element[1]
    return 0


import datetime
datetime.time

print("------------------------")
d2 = datetime.datetime.now()
print(d2)

print("--Convert string into a datetime object ----")
data = '06-Aug-2018'
d1 = datetime.datetime.strptime(data,'%d-%b-%Y')
print(d1)

print("--Timedelta ----")
t1 = datetime.timedelta(seconds=-60)
t2 = datetime.datetime.now()
t3 = t2 +t1
print(t3)


print("------------------------")





prices = [['AAPL', 96.45], ['GS', 25.45],['IONS', 33.44]]
ticker = 'GS'
print(search_list(prices, ticker))

ticker = 'GSS'
print(search_list(prices, ticker))

mydic = {'a': 1, 'b': 2, 'c': 3}
print(mydic.keys())

dict1 = {"a":1, "b":2}
del dict1["a"]
print(dict1)

s = {1, 2, 4, 3}
print(max(s))


import json
data_string = '[{"b": [2,4], "c": 3.0, "a": "A"}]'
python_data = json.loads(data_string)
print(python_data)
print(type(python_data))