first = "     having hello.   "
last = "hi\" ho"#if you enter " in string uesd \ then use \is escape charcter 
#if not use backslah use '' used like 'hi i am" himanshu'..\n used to used create new line


full = first+" "+last
filter = f"{first} {last}"
# new concat method two string we also used len method
filter = f"{len(first)} {last}"
print(filter)
print("h" in first)
print("h" not in first)
h="""hello """#it use to multiple line string """ """ this is also used to mutiple line comment

print(h[3])#index value show charcter that place
print(h[0:2])#given range if not given starting by default used 0 
#and not given ending by default print till end






#this all function not modify the original strings you print string the original string printed
print(first.upper())
print (first.islower())#if we put islower aor isupper   they check string it is upper case or lower case
print(first.endswith("i"))
print(first.replace("i","h"))
print(first.split("i"))
print(first.strip())#it trim white space 
print("_".join(first))#it ued to adding charchter to a string 
print(first.find("h"))
print(first.startswith("")) 
print("i" in first) 