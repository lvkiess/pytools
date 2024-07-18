from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    print("接收到的内容：", data)
    response_data = {"status": "success", "message": "内容已打印", "from": "ccy"}
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
