from flask import Flask,render_template

app = Flask(__name__)


def index():
    # return "<center><h1 style='color:red'>hello word</h1></center>"
    return render_template("index.html")


# url
app.add_url_rule('/', 'index', index)
# app.add_url_rule('/register', 'register', register, methods=["POST"])
from url import urls

for url in urls:
    app.add_url_rule(rule=url["url"], endpoint=url["name"], view_func=url["fun"], methods=url["methods"])
if __name__ == '__main__':
    print(app.url_map)

    app.run()

    "cd Documents/python/flask_test"
