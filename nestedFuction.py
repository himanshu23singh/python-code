def talk(pharse):
    def say(word):
        print(word)
    words = pharse.split(" ")
    for word in words:
        say(word)

talk("hekko baby how are you ")



def count():
    Count=0#enclosed scope used to non local key word that we can 
    #use other fuction variable to diifernt fuction
    def increment():
        nonlocal Count
        Count=Count+1
        print(Count)
    increment()
count()
   




def coun():
    Count=0#enclosed scope used to non local key word that we can 
    #use other fuction variable to diifernt fuction
    def increment():
        nonlocal Count
        Count=Count+1
        return Count
    return increment
increment=coun()
print(increment())
print(increment())