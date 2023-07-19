from flask import Flask, jsonify, request
import subprocess
app = Flask(__name__)

@app.route('/create', methods = ['POST'])
def create():
	cmd = "./test.sh"
	returned_value = subprocess.call(cmd, shell=True)
	print('results:', returned_value)
	print('error:', false)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081,debug = True)

