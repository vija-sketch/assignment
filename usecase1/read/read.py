from flask import Flask, jsonify, request
import subprocess
import os.path
app = Flask(__name__)

@app.route('/read', methods = ['GET'])
def reads():
	path = 'assignment/usecase1/test.txt'
	check_file = os.path.isfile(path)
	if check_file == true:
		cmd = "cat assignment/usecase1/test.txt"
		returned_value = subprocess.call(cmd, shell=True)
		print('results:', returned_value)
		print('error:', false)
	else 
		print('results:', File not found)
		print('error:', false)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082,debug = True)
	
