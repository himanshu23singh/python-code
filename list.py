# in list you can store multiple data type
dogs=["spidy",1,True]
#we change value in list
dogs[0]= 29
print(dogs[0:2])##given range if not given starting by default used 0 
#and not given ending by default print till end also used length function
# dogs.append(34)
# dogs.extend([12])#adding two list
# dogs.remove(34)
# print(dogs.pop())
# print(dogs.insert(3,"fourtuner"))
# #if we used pop  they remove end of list

dogs[1:1]=[34,56,78]#multiple value given in same index af we given range chnage value that particular range
print(dogs)
items=[1,3,4,56,7,3]
items.sort()#convert into acending order in list upper case letter come first and lower case letter come after
#items.sort(key=str.lower)#if we used this no matter of upper case and lower case
print(items)
h=["boya","loya","khoya"]
print(sorted(h, key=str.lower))#if we used that we  creted new list 
print(h)