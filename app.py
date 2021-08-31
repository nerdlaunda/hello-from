import os
from flask import Flask
from flask import render_template
import socket

app = Flask(__name__)

@app.route("/")
def main():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return 'Hello from hostname: ' + hostname + '\nHello from env.hostname: ' + os.environ['POD_NAME'] if "POD_NAME" in os.environ else "none" + '\nIP:' + local_ip + '\n'

@app.route('/host')
def host():

    return ''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")


    
