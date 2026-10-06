accounts = [
    {"username" : "admin", "password" : "secure@2424"},
    {"username" : "hero", "password" : "hero2424@@"},
    {"username" : "bravo", "password" : "12345678"},
    {"username" : "wisdom", "password" : "password"},
    {"username" : "big", "password" : "Xk9#"},
    {"username" : "notfound", "password" : "secure123"}

]

common_bad_password = {"12345678", "secure123", "password"}

weak_count = 0
strong_count = 0

for account in accounts:
    pwd = account["password"]
    if len(pwd) < 8:
        print(f"{account["username"]} : WEAK - password too short")
        weak_count +=1
    elif pwd in common_bad_password:
            print(f"{account["username"]}: WEAK - common password")
            weak_count +=1
    else:
        print(f"{account["username"]}: STRONG ")
        strong_count +=1
        pass

print(f"total Accounts : {len(accounts)}")
print(f"Weak pass: {weak_count}")
print(f"Strong pass: {strong_count}")