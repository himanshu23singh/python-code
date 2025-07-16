#multiple(), filter(),reduce()
# number=[1,2,3]
# double=lambda a: a  * 2
# iseven=lambda b:b%2==0
# # def double(a):
# #     return a*2
# result=list(map(double, number))#we put list name they automate iterated  means go each value of lis naumber

# result1=list(filter(iseven,result))
# print(result)
# print(result1)



# expenses=[('dinner',80),('car repair',120)
          

# ]
# sum=0
# for expense in expenses:
#     sum+=expense[1]
    #    print(expense)



from functools import reduce
expenses=[('dinner',80),('car repair',120)
          

 ]


sum=reduce(lambda a,b:a[1]+b[1],expenses)

print(sum)