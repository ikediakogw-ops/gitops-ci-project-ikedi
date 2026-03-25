from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"}), 200


@app.route('/sum', methods=['POST'])
def get_sum():
    data = request.get_json()

    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Invalid input"}), 400

    result = data['a'] + data['b']
    return jsonify({"result": result})


@app.route('/reverse-string', methods=['POST'])
def reverse_string():
    data = request.get_json()
    text = data.get('text', "")
    return jsonify({"result": text[::-1]})


if __name__ == '__main__':
    app.run()

