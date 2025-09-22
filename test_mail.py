import smtplib

try:
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login("rithika@tantude.com", "your_password_here")
    print("✅ Login successful")
    server.quit()
except Exception as e:
    print("❌ Login failed:", e)
