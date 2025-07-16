def longtime(func):
    def wrap():
        print("before")
        val=fun()
        print("after")
        return val
    return wrapper



#decorator basically kissi bhi  function say phale baad may chale waala code hai


@longtime
def heloo():
    print("helo ")

heloo()