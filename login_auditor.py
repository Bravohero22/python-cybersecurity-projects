# Resilient login attempt Auditor

def is_weak_password(pwd, bad_passwords):
    return len(pwd) < 8 or pwd in bad_passwords

def audit_logins(records, bad_passwords):
    weak_count = 0
    ok_count = 0
    skipped_count = 0

    for record in records:
        try:
            pwd = record["password"]
        except KeyError:
            print(f"Skipping {record["username"]} - no password recorded")
            skipped_count +=1
            continue
        if is_weak_password(pwd, bad_passwords):
            print(f"{record["username"]} - Weak")
            weak_count +=1
        else:
            print(f"{record["username"]} - Ok")
            ok_count +=1

    print(f"Weak: {weak_count}")
    print(f"OK: {ok_count}")
    print(f"Skipped: {skipped_count}")


records = [
    {"username" : "admin", "password" : "1234"},
    {"username" : "user", "password" : "12349056868"},
    {"username" : "sec", "password" : "wisdomhero"},
    {"username" : "hod"},
    {"username" : "student", "password" : "secure"}
]


bad_passwords = {"1234","secure","password"}

audit_logins(records, bad_passwords)