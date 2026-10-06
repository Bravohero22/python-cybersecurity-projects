correct_username = "admin"
correct_password = "secure123"

max_attempts = 3
attempts = 0
Access_granted = False

while attempts < max_attempts and Access_granted == False:
    username = input("Enter your Username>>>")
    password = input("Enter your Password>>")

    if username == correct_username and password == correct_password:
        Access_granted = True
        print("Login successful!")
    else:
        attempts +=1
        remaining = max_attempts - attempts
        print(f"Wrong username or password. Attempts left: {remaining}")

if Access_granted:
    print('Access Granted')
else:
    print("Account Locked - too many failed attempts")