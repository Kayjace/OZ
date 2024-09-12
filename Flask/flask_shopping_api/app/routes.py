from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import app, db
from .models import User, Product, Order, Cart
from .utils import hash_password

# 유저 목록 조회 (관리자 권한 필요)
@app.route('/api/users', methods=['GET'])
@jwt_required()
def get_users():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if not current_user.isAdmin:
        return jsonify({"msg": "Admin access required"}), 403
    
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# 유저 상세 조회 (자신 또는 관리자)
@app.route('/api/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        current_user = User.query.get(current_user_id)
        if not current_user.isAdmin:
            return jsonify({"msg": "Access denied"}), 403
    
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

# 유저 정보 수정 (관리자 권한 필요)
@app.route('/api/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if not current_user.isAdmin:
        return jsonify({"msg": "Admin access required"}), 403

    user = User.query.get_or_404(user_id)
    data = request.get_json()

    user.firstName = data.get('firstName', user.firstName)
    user.lastName = data.get('lastName', user.lastName)
    user.email = data.get('email', user.email)
    user.isAdmin = data.get('isAdmin', user.isAdmin)
    # 비밀번호 변경 시 해시 처리 필요
    if 'password' in data:
        user.password = hash_password(data['password'])

    db.session.commit()
    return jsonify(user.to_dict())

# 제품 목록 조회
@app.route('/api/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

# 제품 상세 조회
@app.route('/api/products/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

# 제품 생성 (관리자 권한 필요)
@app.route('/api/products', methods=['POST'])
@jwt_required()
def create_product():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if not current_user.isAdmin:
        return jsonify({"msg": "Admin access required"}), 403
    
    data = request.get_json()
    new_product = Product(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        imageUrl=data['imageUrl'],
        status=data['status']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

# 제품 업데이트 (관리자 권한 필요)
@app.route('/api/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if not current_user.isAdmin:
        return jsonify({"msg": "Admin access required"}), 403

    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    product.title = data.get('title', product.title)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.imageUrl = data.get('imageUrl', product.imageUrl)
    product.status = data.get('status', product.status)
    db.session.commit()
    return jsonify(product.to_dict())

# 제품 삭제 (관리자 권한 필요)
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if not current_user.isAdmin:
        return jsonify({"msg": "Admin access required"}), 403

    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

# 주문 생성 (자신만 가능)
@app.route('/api/orders', methods=['POST'])
@jwt_required()
def create_order():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    if current_user_id != data['userId']:
        return jsonify({"msg": "Access denied"}), 403

    new_order = Order(
        userId=data['userId'],
        items=data['items'],
        grandTotal=data['grandTotal'],
        status=data['status']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

# 장바구니 조회 (자신만 가능)
@app.route('/api/cart/<int:user_id>', methods=['GET'])
@jwt_required()
def get_cart(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return jsonify({"msg": "Access denied"}), 403

    cart = Cart.query.filter_by(userId=user_id).all()
    return jsonify([item.to_dict() for item in cart])

# 장바구니 아이템 추가 (자신만 가능)
@app.route('/api/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    if current_user_id != data['userId']:
        return jsonify({"msg": "Access denied"}), 403

    new_cart_item = Cart(
        userId=data['userId'],
        cartItem=data['cartItem']
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify(new_cart_item.to_dict()), 201

# 장바구니 아이템 삭제 (자신만 가능)
@app.route('/api/cart/<int:cart_id>', methods=['DELETE'])
@jwt_required()
def delete_cart_item(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    current_user_id = get_jwt_identity()
    if current_user_id != cart_item.userId:
        return jsonify({"msg": "Access denied"}), 403

    db.session.delete(cart_item)
    db.session.commit()
    return '', 204