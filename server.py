from flask import Flask, jsonify, request
import uuid


app = Flask(__name__) # Instance of Flask

# Endpoints
# http://127.0.0.1:5000/home
@app.route("/home", methods=['GET'])
def home():
    return {"message": "Welcome to Flask, Cohort 67"}

# http://127.0.0.1:5000/greet-students
@app.route("/greet-students", methods=["GET"])
def say_hi():
    return {"message": "Ey Hello Students"}


# http://127.0.0.1:5000/cohort-67
@app.route("/cohort-67", methods=["GET"])
def get_students_67():
    student_list = ["Arturo", "Lyn", "Leo"]
    return student_list


# http://127.0.0.1:5000/course-information
@app.route("/course-information", methods=["GET"])
def get_course_information():
    course_informtaion = {
        "title": "Introductory web API with FLsk",
        "duratiion": "4 sessions",
        "level": "Beginner",
    }
    return course_informtaion


"""
    Mini-Challenge

    - Create a /user endpoint
    - Return dictionary with:
        - name
        - role
        - is_active
        - favorite_technologies
    - Test on Thunderclient
"""

# http://127.0.0.1:5000/user
@app.route("/user", methods=["GET"])
def get_user():
    user = {
        "name": "Lyn",
        "role": "student",
        "is_active": True,
        "favorite_technologies": ["Python", "React"]
    }
    return user


# ---- Products -----
products = [
    {
        "id": "1",
        "title": "Nintendo Switch",
        "price": 499.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"
    },
    {
        "id": "2",
        "title": "Smart Refrigerator",
        "price": 999.99,
        "category": "Kitchen",
        "image": "https://picsum.photos/300/200?random=1"
    },
    {
        "id": "3",
        "title": "Blutooth Speaker",
        "price": 79.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"     
    },
]


# http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])
def get_products():
    return products


# ---- Path Parameters ----
# http://127.0.0.1:5000/greet/lyn
@app.route("/greet/<string:name>", methods=["GET"])
def say_hello(name):
    # logic here
    return jsonify({"message": f"Hello {name}"}) 


# http://127.0.0.1:5000/api/products/#
@app.route("/api/products/<string:id>", methods=["GET"])
def get_product_by_id(id):
    print(f"product id: {id}")

    for product in products:
        if product["id"] == id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), 200
    
    return jsonify({
        "success": False,
        "message": f"Product with product id: {id} not found",
    }), 404
    


# POST http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    print(f"request informatiom: {request.get_json()}")
    new_product = request.get_json()
    new_product["id"] = str(uuid.uuid4())
    print(new_product)

    products.append(new_product)

    return jsonify({
        "success": True,
        "message": "Product created successfully",
    }), 201
    

# PUT http://127.0.0.1:5000/api/products/<product_id>
@app.route("/api/products/<string:product_id>", methods=["PUT"])
def update_product(product_id):
    updated_product = request.get_json()
    print(updated_product)
    for product in products:
        if product["id"] == product_id:
            product["title"] = updated_product.get("title", product["title"]) # .get looks for the update, but if not found, it uses the default
            product["price"] = updated_product.get("price", product["price"])
            product["category"] = updated_product.get("category", product["category"])
            product["image"] = updated_product.get("image", product["image"])
            return jsonify({
                "success": True,
                "message": "Product updated successfully",
            }), 200
    return jsonify({
        "success": False,
        "message": "Product not found",
    }), 404
 

# DELETE http://127.0.0.1:5000/api/products/<product_id>
@app.route("/api/products/<string:product_id>", methods=["DELETE"])
def delete_product(product_id):
    print(f"product id: {product_id}")
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({
                "success": True,
                "message": "Product deleted successfully",
            }), 200 # 204 "no content" returns no info      

    return jsonify({
        "success": False,
        "message": "Product not found",
    }), 404


# ---- Coupons ----
coupons = [ 
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]


# http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons


# http://127.0.0.1:5000/api/coupons/count
@app.route("/api/coupons/count", methods=["GET"])
def get_coupon_count():
    return {"count": len(coupons)}


# POST http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    new_coupon["_id"] = len(coupons) + 1

    print(new_coupon)
  
    coupons.append(new_coupon)
    return jsonify({
        "success": True,
        "message": "Coupon created successfully",
    }), 201


# GET http://127.0.0.1:5000/api/coupons/<int:id>
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify({
                "success": True,
                "message": "Coupon retrieved successfully",
                "data": coupon
            }), 200
    return jsonify({
        "success": False,
        "message": "Coupon not found",
    }), 404
        


# PUT http://127.0.0.1:5000/api/coupons/<int:id>
@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])
def update_coupon(coupon_id):
    updated_coupon = request.get_json()
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupon["code"] = updated_coupon.get("code", coupon["code"])
            coupon["discount"] = updated_coupon.get("discount", coupon["discount"])
            return jsonify({
                "success": True,
                "message": "Coupon updated successfully",
            }), 200
    return jsonify({
        "success": False,
        "message": "Coupon not found",
    }), 404


# DELETE http://127.0.0.1:5000/api/coupons/<int:id>
@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon(coupon_id):
    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupons.remove(coupon)
            return jsonify({
                "success": True,
                "message": "Coupon deleted successfully",
            }), 200
    return jsonify({
        "success": False,
        "message": "Coupon not found",
    }), 404


if __name__ == '__main__':
    app.run(debug=True)