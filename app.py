from flask import Flask
#created a object which is app
app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello Vipin!!"


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
