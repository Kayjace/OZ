from flask import Flask, render_template
from flask_mysqldb import MySQL
import yaml
from posts_routes import posts_bp

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

# Register blueprints
app.register_blueprint(posts_bp)

@app.route('/')
def index():
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)