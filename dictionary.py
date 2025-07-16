dog={"name":"harry","age":3,"color":"green"}
dog['name']="spider"
print(dog["name"])#it is mutable
print(dog.get("name"))
print(dog.get("color","brown"))#if color not key by default return brown 
#if color key present in dic they return the value of dic
print(dog.pop("name"))#it remove specific key and value
print(dog.popitem())#it remove end key value pair
dog["favorte food"]='daal roti'
print(list(dog.keys()))# same we can print value write values in place of key
print(list(dog.items()))
copydogs=dog.copy()