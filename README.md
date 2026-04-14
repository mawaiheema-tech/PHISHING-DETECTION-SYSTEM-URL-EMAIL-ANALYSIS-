# 🛡️ Phishing Detection System (URL & Email Analysis)

## 📌 Overview
This project is a **Phishing Detection System** developed using Python.  
It analyzes **URLs and email text** to detect potential phishing attempts and classifies them as:

- ✅ SAFE  
- ⚠️ SUSPICIOUS  
- 🚨 PHISHING  

The system is based on **rule-based detection techniques** commonly used in cybersecurity.

---

## 🎯 Objective
- Detect phishing attempts in URLs and emails  
- Identify suspicious patterns and keywords  
- Classify inputs into Safe, Suspicious, or Phishing  
- Understand real-world phishing techniques  

---

## 🧰 Technologies Used
- Python 3  
- Regular Expressions (Regex)  
- VS Code / Terminal  

---

## ⚙️ How It Works

### 🔹 URL Analysis
The system checks:
- Suspicious keywords (login, verify, secure, etc.)  
- Unusual domain extensions (.xyz, .top, etc.)  
- Presence of numbers or hyphens  
- IP-based URLs  

---

### 🔹 Email Analysis
The system detects:
- Urgent or threatening language  
- Suspicious links  
- Fake rewards or lottery messages  
- Requests for sensitive information  

---

## 🧠 Classification Logic
Based on detected indicators:

| Score | Result |
|------|--------|
| Low  | SAFE |
| Medium | SUSPICIOUS |
| High | PHISHING |

---

## 💻 Installation & Usage

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/phishing-detection-system.git
cd phishing-detection-system

###Step 2: Run the Program
python phishing_detection_system.py
Step 3: Choose Input Type
Enter 1 for URL analysis
Enter 2 for Email analysis

🔹 URL Analysis
Enter URL: https://www.youtube.com
Result: SAFE
Enter URL: http://secure-login-paypal.verify-user123.com
Result: PHISHING
🔹 Email Analysis
Enter email text: Urgent! Verify your account now...
Result: PHISHING
Enter email text: Internship update completed.
Result: SAFE


📂 Project Structure
phishing-detection-system/
│── phishing_detection_system.py
│── README.md


🚀 Future Improvements
Machine Learning-based detection
Real-time URL scanning APIs
GUI interface
Browser extension integration

👩‍💻 Author
Heema
Cybersecurity Intern

⭐ Acknowledgment
This project was developed as part of a Cybersecurity Internship Task to understand phishing detection techniques.

⚠️ Disclaimer
This project is for educational purposes only and demonstrates basic phishing detection logic.
