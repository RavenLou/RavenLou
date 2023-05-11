from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def myFunc():
    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return 'success'
    else:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return '%s' % ip

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8000)
