from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    customer_phone = db.Column(db.String(255), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)
    number_of_people = db.Column(db.Integer, nullable=False)
    special_requests = db.Column(db.Text)

    def __repr__(self):
        return f"<Reservation {self.customer_name}>"

# 테이블 생성
@app.before_first_request
def create_tables():
    db.create_all()

# 메인 페이지: 예약 목록 조회 및 새 예약 추가
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_reservation = Reservation(
            customer_name=request.form['customer_name'],
            customer_phone=request.form['customer_phone'],
            reservation_time=datetime.strptime(request.form['reservation_time'], '%Y-%m-%dT%H:%M'),
            number_of_people=request.form['number_of_people'],
            special_requests=request.form.get('special_requests')
        )
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        all_reservations = Reservation.query.all()
        return render_template('index.html', reservations=all_reservations)

# 특정 예약 수정 페이지
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    reservation = Reservation.query.get(id)
    if request.method == 'POST':
        reservation.customer_name = request.form['customer_name']
        reservation.customer_phone = request.form['customer_phone']
        reservation.reservation_time = datetime.strptime(request.form['reservation_time'], '%Y-%m-%dT%H:%M')
        reservation.number_of_people = request.form['number_of_people']
        reservation.special_requests = request.form.get('special_requests')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', reservation=reservation)

# 특정 예약 삭제
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    reservation = Reservation.query.get(id)
    db.session.delete(reservation)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)