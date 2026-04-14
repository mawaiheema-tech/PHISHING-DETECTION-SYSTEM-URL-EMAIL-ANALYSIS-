import re

def check_url(url):
    phishing_keywords = ["login", "verify", "secure", "update", "free", "win"]
    suspicious_tlds = [".xyz", ".click", ".top", ".ru", ".cn"]
    
    score = 0

    if any(keyword in url.lower() for keyword in phishing_keywords):
        score += 1

    if any(url.lower().endswith(tld) for tld in suspicious_tlds):
        score += 1

    if re.search(r"\d", url):
        score += 1

    if re.match(r"http://\d+\.\d+\.\d+\.\d+", url):
        score += 2

    if "-" in url.split("//")[-1].split("/")[0]:
        score += 1

    if score == 0:
        return "SAFE"
    elif score <= 2:
        return "SUSPICIOUS"
    else:
        return "PHISHING"


def check_email(text):
    red_flags = [
        "urgent", "immediately", "verify", "password",
        "account suspended", "click here", "reward",
        "lottery", "win"
    ]

    score = 0

    if any(flag in text.lower() for flag in red_flags):
        score += 2

    if "http" in text:
        score += 1

    if "@" in text and ("gmail" in text or "outlook" in text):
        score += 1

    if score == 0:
        return "SAFE"
    elif score <= 2:
        return "SUSPICIOUS"
    else:
        return "PHISHING"


# MAIN PROGRAM
print("Enter 1 for URL analysis or 2 for Email analysis:")
choice = input("> ")

if choice == "1":
    url = input("Enter URL: ")
    print("Result:", check_url(url))

elif choice == "2":
    email = input("Enter email text: ")
    print("Result:", check_email(email))

else:
    print("Invalid choice")