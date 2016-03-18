import os, socket, datetime
from flask import Flask, request
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
    res = "Hellow World! {0}".format(count)
    if 'debug' in request.args and request.args['debug'] == '1':
        hostname = socket.gethostname()
        now =  datetime.datetime.now()
        res += "<br/><br/>Datetime : {0}<br/>Hostname : {1}".format(now, hostname)
        res += "<br/>Request : {0} {1}".format(request.method, request.url)
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)

