from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<string:name>",methods=["GET"])
def home():

  return jsonify[{"name"}]
