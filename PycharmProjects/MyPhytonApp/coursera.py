#def replace(test_string, replace_string):
#    start = test_string.find(replace_string)
#    lenght_replace = len(replace_string)
#    replace = test_string[0:start] + "bodega" + test_string[start+lenght_replace:]
#    return replace

#print(replace("Hi how are you?", "you"))
#print(replace("", ""))

# Lists: Sequential ordered mutable collections
#
# Key properties
#   - collection of related objects
#   - ordered or sequential collection
#   - mutable. Lists can be modified
list_of_names = ["Renato", "Aline", "Murilo"]
list_of_natural_numbers = [1,2,3,4,5,6,7]
long_list = [ 1,['a',['b','c']], 55, "uma string qualquer"]  #no need of elements to be of the same type

print(long_list)

#some list manipulation
x = list() #create a list
print(x)
x.append('One')
print(x)
x.append('Two')
print(x)

y = list()
y.extend(list_of_names)
print(y)

y.pop(1)
print(y)
y.remove("Renato")
print(y)







