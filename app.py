from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "<h1><center> Hello World Flask App! Version beta 1- SecretsManager<center><h1>"

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000)
