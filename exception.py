# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
# except ZeroDivisionError:
#     print("❌ You can't divide by zero.")
# except ValueError:
#     print("❌ Please enter valid numbers.")
# else:
#     print("✅ Result is:", result)
# finally:
#     print("🔚 Program ended.")


# Simulated user data
# Simulated user data
users = {"admin": "1234", "user": "abcd"}

try:
    username = input("Enter username: ")

    if username not in users:
        raise ValueError("❌ User does not exist.")

    password = input("Enter password: ")

    if users[username] != password:
        raise PermissionError("❌ Incorrect password.")

except ValueError as ve:
    print(ve)

except PermissionError as pe:
    print(pe)

else:
    print("✅ Login successful!")

finally:
    print("🔚 Login attempt finished.")



class dogeshbahiException(Exception):
    print("inside")
    pass
try:
    raise dogeshbahiException()
except dogeshbahiException:
    print("dogesh bahi kho gaye")