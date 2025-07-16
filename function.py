 

    #why the function calling each other means because tehy had constant argument 
#if you cahbge itenger to string simply str(variable name)



def heloo(name="hello buddy"):
     print("hi. " + name)
heloo()#if you dont passing argument default value print which is given by parmeter


#if integer variabl decalre inside fuction  they do not cahge out side integer varable but
#in mutable data type it is possible dictionary

def hello(name):
    if not name:
        return
    print(name)
hello(False)
#class with false they return nothing, if given name they return name

j="haryy"
def ok(name):
    
    print("hi. " + name)
    return 8,9,7
print(ok(j))
#if ypu want you to return  VALUE IN FUCTION  you want print fuction because they store the value in caller 
#function if you want see redult you  wnat print
