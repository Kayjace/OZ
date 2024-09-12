from email_validator import validate_email, EmailNotValidError
from flask import Flask, render_template, url_for, request, redirect, flash, make_response, session
from flask_debugtoolbar import DebugToolbarExtension #코드 추가
import logging
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["SECRET_KEY"] = "2AHDHjsajh2308238328"
app.logger.setLevel(logging.DEBUG)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "hktysh@gmail.com"
app.config["MAIL_PASSWORD"] = ""
app.config["MAIL_DEFAULT_SENDER"] = "hktysh@gmail.com"

mail = Mail(app)
#코드추가
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)

@app.route("/")
def index():
    return "Hello oz"

@app.route("/contact")
def contact():
    #응답 정도 취득
    response = make_response(render_template("contact.html"))
    #쿠키 설정
    response.set_cookie("oz key", "oz value")
    #세션 설정
    session["name"] = "oz"

    return response

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print(name)
        print(email)
        print(message)
        is_valid = True

        if not name:
            flash("사용자명은 필수로 입력해주세요")
            is_valid = False
        
        if not email:
            flash("메일 주소는 필수로 입력해주세요")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요")
            is_valid = False
        
        if not message:
            flash("문의 내용은 필수로 입력해주세요")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))

        flash("문의해 주셔서 감사합니다.")
        send_email(email, "문의 감사합니다.", "contact_mail", name=name,description=message,)
        return redirect(url_for("contact_complete"))
        
    
    return render_template("contact_complete.html")

def send_email(to, subject, template, **kwargs):

    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template+ ".html", **kwargs)
    msg.charset = 'utf-8'
    mail.send(msg)