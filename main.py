from flask import Flask, request, jsonify 
from collections import defaultdict
import json

app = Flask(__name__)
app.data = defaultdict(int)
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])


@app.route("/get_info", methods=['GET'])
def get_info():
  data = request.data
  data = json.loads(data)
  
  users = [("username", 5), ("someone", 15), ('n00b', 0)]
  
  # Sort user array
  users.sort(key=lambda a: a[1], reverse=True)

  # Format the users
  leaderboard = map(lambda user: user[0] + "| " + str(user[1]), users)
  
  # Output
  print("\n".join(leaderboard))
  return jsonify({'GET' : ' works'})

@app.route("/test_post", methods=['POST'])
def test_post():
  return jsonify({'status': 'post works', 'your_data': json.loads(request.data)})

  

app.run(host='0.0.0.0')