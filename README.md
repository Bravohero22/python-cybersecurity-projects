# Python Cybersecurity Projects

Small Python tools I'm building while learning Python for cybersecurity. I'm following a 60-day roadmap that leads into ethical hacking, and every project here was written by me as I learned each concept.

## Projects

| Project | What it does | Concepts used |
|---|---|---|
| [Login Attempt Limiter](login_limiter.py) | Gives a user 3 tries to log in, then locks the account | `while` loops, counters, conditionals, `input()` |
| [Firewall Rule Checker](firewall_checker.py) | Checks connection attempts against a set of allowed ports and reports what is blocked | Sets, lists of dictionaries, counters, percentage formatting |
| [Password Policy Auditor](password_auditor.py) | Flags passwords that are too short or on a common-password list | Loops, dictionaries, `len()`, `in` |
| [Network Scan Summary](scan_summary.py) | Labels hosts as private or public and ports as risky or safe | Functions, `return`, `try/except KeyError`, `continue` |
| [Login Auditor](login_auditor.py) | Audits login records, skips malformed ones safely, and prints a summary | Functions, error handling, counters |

> Rename the links above to match the actual file names in this repo.

## How to run a project

1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repo:
   ```
   git clone https://github.com/<your-username>/python-cybersecurity-projects.git
   ```
3. Run any script:
   ```
   python login_auditor.py
   ```

## Example output (Login Auditor)

```
admin - Weak
user - Ok
sec - Ok
Skipping hod - no password recorded
student - Weak
Weak: 2
OK: 2
Skipped: 1
```

## What I've learned so far

- Variables, data types, conditionals, and loops
- Lists, dictionaries, tuples, and sets
- Writing reusable functions
- Handling errors so a script doesn't crash on bad data
- Using Git and GitHub to track my work

## What's next

- [ ] File handling: reading and writing log files
- [ ] Networking with Python sockets
- [ ] Building a port scanner
- [ ] Packet sniffing with Scapy
- [ ] Ethical hacking labs (in my own virtual machines and legal practice platforms only)

## A note on safety

All projects here use sample data or systems I own. I only test security tools on my own machines or on platforms built for practice, such as TryHackMe.
