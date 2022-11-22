from flask import Flask, render_template, request
from replit import db
app = Flask('app')

db["number1"] = "Dr.A"
db["score1"] = 20
db["number2"] = "Danielle"
db["score2"] = 18
db["number3"] = "Shemaya"
db["score3"] = 17
db["number4"] = "Antonia"
db["score4"] = 10
db["number5"] = "Brandon"
db["score5"] = 3

@app.route('/')
def homepage():
  number1 = db["number1"] + ": " + str(db["score1"])
  number2 = db["number2"] + ": " + str(db["score2"])
  number3 = db["number3"] + ": " + str(db["score3"])
  number4 = db["number4"] + ": " + str(db["score4"])
  number5 = db["number5"] + ": " + str(db["score5"])
  return render_template('leaderboard.html', number1=number1, number2=number2, number3=number3, number4=number4, number5=number5)


@app.route("/leaderboard", methods=["POST", "GET"])
def leaderboard():
  username = request.form["name_input"]
  score = request.form["score_input"]
  if score > db["score1"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = db["number3"]
    db["score4"] = db["score3"]
    db["number3"] = db["number2"]
    db["score3"] = db["score2"]
    db["number1"] = username
    db["score1"] = score
  elif score > db["score2"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = db["number3"]
    db["score4"] = db["score3"]
    db["number3"] = db["number2"]
    db["score3"] = db["score2"]
    db["number2"] = username
    db["score2"] = score
  elif score > db["score3"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = db["number3"]
    db["score4"] = db["score3"]
    db["number3"] = username
    db["score3"] = score
  elif score > db["score4"]:
    db["number5"] = db["number4"]
    db["score5"] = db["score4"]
    db["number4"] = username
    db["score4"] = score
  elif score > db["score5"]:
    db["number5"] = username
    db["score5"] = score
  number1 = db["number1"] + ": " + str(db["score1"])
  number2 = db["number2"] + ": " + str(db["score2"])
  number3 = db["number3"] + ": " + str(db["score3"])
  number4 = db["number4"] + ": " + str(db["score4"])
  number5 = db["number5"] + ": " + str(db["score5"])
  return render_template('leaderboard.html', number1=number1, number2=number2, number3=number3, number4=number4, number5=number5)

app.run(host='0.0.0.0', port=81)