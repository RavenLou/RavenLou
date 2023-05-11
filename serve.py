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
        ip = socket.gethostbyname('ec2-3-86-151-208.compute-1.amazonaws.com')
        return '%s' % ip

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8000)