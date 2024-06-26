from flask import Flask , render_template , jsonify

app = Flask(__name__)

Jobs = [{
    "id":1,
    "title":"Data Analyst",
    "location":"Hyd,India",
    "salary":"Rs. 10,00,000"
},
{
    "id":2,
    "title":"Data Scientist",
    "location":"Delhi ,India",
    "salary":"Rs. 15,00,000"
},
{
    "id":3,
    "title":"Bakcend Developer",
    "location":"Remote",
    "salary":"Rs. 12,00,000"
},
{
    "id":4,
    "title":"Frontend Dev",
    "location":"USA",
    "salary":"$120,000"
},
]

@app.route("/")
def hello_world():
    return render_template("home.html",jobs=Jobs,company_name ="Jackson")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)