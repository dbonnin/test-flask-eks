from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"key": "value"}  # Replace with your actual data
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)