SE Lab 5: -
Static Code Analysis

📘 Overview

This project demonstrates the process of applying static code analysis to improve the security, quality, and maintainability of a Python program.
The original inventory_system.py script was analyzed and refined using Pylint, Flake8, and Bandit, addressing issues related to security vulnerabilities, coding style, and best practices.

🧩 Tools Used

Pylint – for detecting style, design, and logic issues.

Flake8 – for enforcing PEP 8 style compliance.

Bandit – for identifying potential security risks in Python code.

⚙️ How to Run

Clone or open the Codespace.

Run the following commands to analyze or verify the code:

pylint inventory_system.py
flake8 inventory_system.py
bandit -r inventory_system.py


Execute the script:

python3 inventory_system.py

🧠 Summary of Improvements

Replaced unsafe eval() usage.

Added explicit exception handling.

Implemented structured logging and input validation.

Used context managers and UTF-8 encoding for file I/O.

Added docstrings and followed snake_case naming conventions.

Final Results:

Pylint Score: 10.00 / 10

Bandit: No security issues identified

Flake8: Fully PEP 8–compliant

📄 Files Included
File	                Description
inventory_system.py	Final, cleaned, and secure version of the inventory management program.
pylint_report.txt	Final Pylint analysis output.
flake8_report.txt	Final Flake8 analysis output.
bandit_report.txt	Final Bandit security report.
reflection.md	    Developer reflection and insights on the improvement process.
README.md	        Project overview and usage guide.

👩‍💻 Author
Sneha Pandit (PES1UG23CS583)