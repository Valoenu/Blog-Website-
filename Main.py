from flask import Flask, render_template
import requests
import smtplib


# set your website owner email and make sure that you have correct email provider (@gmail.com)
WEBSITE_OWNER_EMAIL = "youremail@gmail.com" 

# Set your website owner password
WEBSITE_OWNER_PASSWORD = "password123"

# ! Make sure that you hide your email and password in secrets


# Create Flask app
app = Flask(__name__)

# Get your url with json formatted content (use n.point)
URL = ""
blog_content = requests.get(URL)


@app.route("/")
def posts_page():
  return render_template("index.html", all_posts=blog_content)


@app.route("/about")
def about_page():
  return render_template("about.html")


@app.route("/contact", methods=["GET"])
def contact_page():
  if request.method == 'POST':
    data = request.form # Return our list from contact.html
    print(data['email'])
    print(data['name'])
    print(data['message'])
    print(data['phone'])
    return render_template("contact.html", message_sent=True)
    email_send(data['name'], data['email'], data['phone'], data['message'])
  return render_template("contact.html", message_sent=False)# It will return either False or True, (depends on request.method)



# Structure for email
def email_send(name, email, message, phone):
  message_body = f'Subject: New message 💬!\nName: {name}\n Phone: {phone}\n Email: {email}\n Message: {message}'

  with smtplib.SMTP("smtp@gmail.com") as connect:
    connect.startls()
    connect.login(WEBSITE_OWNER_EMAIL, WEBSITE_OWNER_PASSWORD)
    connect.sendemail(WEBSITE_OWNER_EMAIL, WEBSITE_OWNER_PASSWORD, message_body)
    
    
@app.route("/post/<int:index>")
def post_view(index):
  requested_post = None
  for blog_post in blog_content:
    if blog_content['id'] == index:
      requested_post = blog_post
  return render_template("post.html", post=requested_post)


# Run your app and set port
if __name__ == "__main__":
  app.run(debug=True, port=5001)
