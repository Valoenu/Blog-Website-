*Quick SMTPLIB Tutorial*

# Emails structure
import smtplib # To send emails


# set your website owner email and make sure that you have correct email provider (@gmail.com)
YOUR_EMAIL = "youremail@gmail.com" 

# Set your website owner password
YOUR_PASSWORD = "password123"

# ! Make sure that you hide your email and password in secrets
# Connect smtplib
connection = smtplib.SMTP("smtp.gmail.com")

# Securing connection to our email server (message encrypted)
connection.starttls()

# Log in
connection.login(user='YOUR_EMAIL', password='YOUR_PASSWORD)

# Send email
connection.sendmail(
  from_addr=,
  to_addrs="YOUR_EMAIL"
  msg="message",
)

# Close your connection
connection.close()
                 