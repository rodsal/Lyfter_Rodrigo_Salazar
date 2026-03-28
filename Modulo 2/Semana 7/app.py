from functools import wraps
from datetime import datetime
from flask import Flask, request, Response, jsonify
from database.db import DB_Manager
from jwt_manager import JWT_Manager

app = Flask("user-service")
db_manager = DB_Manager()
jwt_manager = JWT_Manager('private.pem', 'public.pem', 'RS256')

def token_required(allowed_roles=None):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            try:
                token = request.headers.get('Authorization')
                if not token:
                    return Response(status=401)
                token = token.replace("Bearer ", "")
                decoded = jwt_manager.decode(token)
                if not decoded:
                    return Response(status=403)
                user_id = decoded['id']
                user = db_manager.get_user_by_id(user_id)
                if not user:
                    return Response(status=403)
                user_role = user[3]
                if allowed_roles and user_role not in allowed_roles:
                    if user_role != 'admin':
                        return Response(status=403)
                return f(user, *args, **kwargs)
            except Exception as e:
                return Response(status=500)
        return decorated
    return decorator

@app.route("/liveness")
def liveness():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if data.get('username') is None or data.get('password') is None:
        return Response(status=400)
    else:
        role = 'user'
        result = db_manager.insert_user(data.get('username'), data.get('password'), role)
        user_id = result[0]
        token = jwt_manager.encode({'id': user_id, 'role': role})
        return jsonify(token=token), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get('username') is None or data.get('password') is None:
        return Response(status=400)
    else:
        result = db_manager.get_user(data.get('username'), data.get('password'))
        if result is None:
            return Response(status=403)
        else:
            user_id = result[0]
            role = result[3]
            token = jwt_manager.encode({'id': user_id, 'role': role})
            return jsonify(token=token), 200

@app.route('/me')
@token_required(allowed_roles=['admin', 'user'])
def me(current_user):
    return jsonify(id=current_user[0], username=current_user[1], role=current_user[3]), 200

@app.route('/products', methods=['POST'])
@token_required(allowed_roles=['admin'])
def create_product(current_user):
    data = request.get_json()
    if not all(k in data for k in ('name', 'price', 'quantity', 'enter_date')):
        return Response(status=400)
    db_manager.products.insert(data['name'], data['price'], data['quantity'], data['enter_date'])
    return jsonify(message="Product created"), 201

@app.route('/products', methods=['GET'])
@token_required(allowed_roles=['admin'])
def get_products(current_user):
    products = db_manager.products.get_all()
    result = [{'id': p[0], 'name': p[1], 'price': p[2], 'enter_date': p[3], 'quantity': p[4]} for p in products]
    return jsonify(result), 200

@app.route('/products/<int:p_id>', methods=['GET'])
@token_required(allowed_roles=['admin'])
def get_product(current_user, p_id):
    p = db_manager.products.get_by_id(p_id)
    if not p:
        return Response(status=404)
    return jsonify({'id': p[0], 'name': p[1], 'price': p[2], 'enter_date': p[3], 'quantity': p[4]}), 200

@app.route('/products/<int:p_id>', methods=['PUT'])
@token_required(allowed_roles=['admin'])
def update_product(current_user, p_id):
    data = request.get_json()
    p = db_manager.products.get_by_id(p_id)
    if not p:
        return Response(status=404)
    db_manager.products.update('id', p_id, data)
    return jsonify(message="Product updated"), 200

@app.route('/products/<int:p_id>', methods=['DELETE'])
@token_required(allowed_roles=['admin'])
def delete_product(current_user, p_id):
    p = db_manager.products.get_by_id(p_id)
    if not p:
        return Response(status=404)
    db_manager.products.delete('id', p_id)
    return jsonify(message="Product deleted"), 200

@app.route('/buy', methods=['POST'])
@token_required(allowed_roles=['admin', 'user'])
def buy_product(current_user):
    data = request.get_json()
    product_id = data.get('product_id')
    cantidad = data.get('quantity')
    
    if not product_id or not cantidad or cantidad <= 0:
        return Response(status=400)
    
    p = db_manager.products.get_by_id(product_id)
    if not p:
        return Response(status=404)
        
    current_quantity = p[4]
    price = p[2]
    
    if current_quantity < cantidad:
        return jsonify(message="Not enough inventory"), 400
        
    total_price = price * cantidad
    new_quantity = current_quantity - cantidad
    
    # Update product inventory
    db_manager.products.update('id', product_id, {'quantity': new_quantity})
    
    # Create invoice
    fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_manager.invoices.insert(current_user[0], cantidad, product_id, fecha_compra, total_price)
    
    return jsonify(message="Purchase successful", total=total_price), 201

@app.route('/invoices', methods=['GET'])
@token_required(allowed_roles=['admin', 'user'])
def get_invoices(current_user):
    user_id = current_user[0]
    user_invoices = db_manager.invoices.get_by_user_id(user_id)
    result = [{'id': i[0], 'user_id': i[1], 'product_id': i[2], 'cantidad_comprada': i[3], 'fecha_compra': i[4], 'total': i[5]} for i in user_invoices]
    return jsonify(result), 200