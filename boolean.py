done=0 #0 is false value and all number is true
#string are always false when it is empty
#list,tuple,dic,false when it is empty
h=" "
if h:
    print("yes")
else:
    print("no")    


h=True
b=False
j=any([h,b])    #any fuction is return true when any one is true
i=all([h,b])#it is  return true all value is true