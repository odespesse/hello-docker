import os
from flask import Flask
app = Flask(__name__)

@app.route("/greetings")
def hello():
    count_path = "/tmp/hello/count"
    count = 0
    if os.path.isfile(count_path):
        with open(count_path, 'r') as f:
            count = int(f.read())
    count += 1
    with open(count_path, 'w') as f:
        f.write(str(count))
    return "Hello World! {0}".format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)

