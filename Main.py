from flask import Flask, render_template
import requests

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

@app.route("/contact")
def contact_page():
  return render_template("contact.html")

@app.route("/post/<int:index>")
def post_view(index):
  requested_post = None
  for blog_post in blog_content:
    if blog_content['id'] == index:
      requested_post = blog_post
  return render_template("post.html", post=requested_post)
  
  

# Run your app and set port to 5001
if __name__ == "__main__":
  app.run(debug=True, port=5001)
