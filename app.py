from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, jsonify
from flask_sqlalchemy import SQLAlchemy, Model
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:////Users/Sudharsan/PycharmProjects/Billing_System/brob_try/trialapp/try.db'
db = SQLAlchemy(app)

app.secret_key = 'hello'


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    phonenumber = db.Column(db.String(80))

    def json(self):
        # okk = bytes(self.username, 'utf-8').decode(encoding = 'UTF-8',errors = 'strict')
        # ok_tamil_test = bytes(self.username,encoding='utf-8').decode(encoding = 'UTF-8',errors = 'strict')
        # print(self.username,ok_tamil_test,type(ok_tamil_test),'-----')
        return {
        'id':self.id,'username':self.username,'phonenumber':self.phonenumber
    }






@app.route("/", methods=["GET", "POST"])
def hello():
    # image_binary = read_image()

    if request.method == "POST":

        uname = request.form["uname"]
        # with open('ttt.txt', encoding='utf-8') as f:
        #     contents = f.readlines()
        #     # letters = utf8.get_letters(contents)
        #     print(type(contents))
        #     uname = contents
        phonenumber = request.form["phonenumber"]
        # # print(type(uname))
        # for i in uname:
        #     a=i.split(",")
        # uplode = user(username=a[0],phonenumber=a[1])
        uplode = user(username=uname, phonenumber=phonenumber)
        db.session.add(uplode)
        db.session.commit()



        return render_template('Ok.html')
    return render_template('app.html')


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search = request.form["search"]
        # allemail = user.query.filter(user.username.startswith(search)).all()
        ok = db.session.query(user).filter(user.username.startswith(search)).all()
        print(ok,type(ok),search)
        # search_listt = []
        # for k in allemail:
        #     print(k.username)
        #     print(type(k))
        #     search_listt.append(k.username)

        # return jsonify([Customer.json(item) for item in inhouse_list])
        return jsonify([user.json(k) for k in ok])
        # return jsonify((k.username,j.phonenumber) for k,j in allemail)
        # return  'okkk'



@app.route('/uuu')
def get_current_user():
    return jsonify(
        username='g.user.username',
        email='g.user.email',
        id='g.user.id'
    )





if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=5027)
    # app.run(debug=True, port=1001)
    # app.run(host="0.0.0.0", port=5000, debug=True)
    # socketio = SocketIO(app, logger=True, engineio_logger=True)
    # socketio.run(app, host="0.0.0.0", port=5000, debug=True,allow_unsafe_werkzeug=True)