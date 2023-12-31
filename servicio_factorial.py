from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def obtener_factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * obtener_factorial(n - 1)

@app.route('/factorial/<int:num>', methods=['GET'])
def factorial(num):
    resultado = obtener_factorial(num)
    container_id = os.uname()[1]
    
    return jsonify({'resultado': resultado}, {'container_id': container_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)