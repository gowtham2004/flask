from flask import Flask,jsonify,request

app = Flask(__name__)

dict = {"hema":"flutter","mathan":"python","thej":"python","vs":"code"}

@app.route("/",methods=["GET","POST"])
def home():
  if request.method == "GET":
    return jsonify({"response" : "Hello World"})
  elif request.method == "POST":
    query = request.json
    name = query["name"]
    code = dict[name]
    return jsonify({"response" : name+" : "+code})

if __name__ == "__main__":
  app.run(debug=True)
