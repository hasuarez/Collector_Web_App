from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from send_email import email_send
from sqlalchemy.sql import func



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hector123@localhost:5432/height_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app) 
class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(120), unique = True)
    height = db.Column(db.Integer)

    def __init__(self , email_, height_):
        self.email= email_
        self.height = height_



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods =["POST"])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]
        print(email,height)
        if db.session.query(Data).filter(Data.email == email).count() == 0 :
            db.session.add(Data(email_=email, height_=height))  # instancia + add
            db.session.commit()  
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height,1)
            count = db.session.query(Data.height).count()
            email_send(email,height,average_height, count)
            return render_template("success.html")
        
        return render_template("index.html", text="parece que tenemos un error, el email que has ingresado ya existe")


if __name__ == "__main__":
    app.debug = True
    with app.app_context():
        db.create_all()
    app.run()