from flask import Flask , request , render_template 
import joblib

# instance of api
app = Flask(__name__)

# loading the model
model = joblib.load("bank.pkl")

@app.route("/")
def hello():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def form_data():
    age = request.form.get("age")
    job = request.form.get("job")
    marital = request.form.get("marital")
    education = request.form.get("education")
    default = request.form.get("default")
    balance = request.form.get("balance")
    housing = request.form.get("housing")
    loan = request.form.get("loan")
    day = request.form.get("day")
    month = request.form.get("month")
    duration = request.form.get("duration")
    campaign = request.form.get("campaign")
    pdays = request.form.get("pdays")
    previous = request.form.get("previous")
    
    result = model.predict([[age, job, marital, education, default, balance, housing,loan, day, month, duration, campaign, pdays, previous]])

    if result==1:
        out = "Person will deposit the amount"
    else:
        out = "Person will not deposit the amount"
    
    return render_template("index.html", data=(out))
    
if __name__ =="__main__":
    app.run(debug=True)