Math-Based CAPTCHA 🧮
Overview
This project is a Math-Based CAPTCHA system designed to prevent spam and bot activities. It generates random math expressions using operators (+, -, *, /) and verifies user input against the correct answer. The system features a countdown timer, theme switching (dark/light mode), and automatic CAPTCHA refresh on timeout or incorrect input.

🛠️ Features
✔️ Generates random math-based CAPTCHA images
✔️ Validates user input and provides instant feedback
✔️ Auto-refreshes CAPTCHA if the timer runs out
✔️ Dark/Light mode toggle for better UI experience
✔️ Python GUI (Tkinter) for a user-friendly interface
✔️ Uses PIL and ImageCaptcha for CAPTCHA image generation

🚀 Installation & Setup
Prerequisites
Ensure you have Python installed (version 3.x recommended). You can check with
# python --version

Step 1: Clone the Repository
# git clone https://github.com/your-username/Math-Captcha.git
# cd Math-Captcha

Step 2: Install Dependencies
Run the following command to install required Python libraries:
# pip install tkinter captcha pillow

Step 3: Run the Application
Execute the script using:
# python math_captcha.py


🛠️ Technologies Used
Python – Core programming language
Tkinter – GUI framework for UI components
Pillow (PIL) – Image processing for CAPTCHA generation
captcha library – Used to create CAPTCHA images
📌 Usage
1️⃣ Open the application
2️⃣ Solve the math CAPTCHA and enter the result
3️⃣ Click Submit to verify your answer
4️⃣ If incorrect, try again or click Refresh
5️⃣ If the timer runs out, a new CAPTCHA is generated automatically
