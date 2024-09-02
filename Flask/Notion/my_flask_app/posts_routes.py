from flask import Blueprint, request, jsonify, render_template
from app import mysql

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts/<int:id>')
def view_post(id):
    return render_template('post.html')

@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    cur.close()
    return jsonify([{'id': post[0], 'title': post[1], 'content': post[2], 'created_at': post[3]} for post in posts])

@posts_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts WHERE id = %s", (id,))
    post = cur.fetchone()
    cur.close()
    if post:
        return jsonify({'id': post[0], 'title': post[1], 'content': post[2], 'created_at': post[3]})
    return jsonify({'error': 'Post not found'}), 404

@posts_bp.route('/posts', methods=['POST'])
def create_post():
    title = request.json['title']
    content = request.json['content']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    mysql.connection.commit()
    new_id = cur.lastrowid
    cur.close()
    return jsonify({'id': new_id, 'title': title, 'content': content}), 201

@posts_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    title = request.json['title']
    content = request.json['content']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE posts SET title = %s, content = %s WHERE id = %s", (title, content, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'id': id, 'title': title, 'content': content})

@posts_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM posts WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Post deleted successfully'})