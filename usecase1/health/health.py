from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

@app.route('/health', methods = ['GET'])
def health():
    if health_status:
        resp = jsonify(health="healthy",error="false")
        
    else:
        resp = jsonify(health="unhealthy",error="true")
        

    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug = True)