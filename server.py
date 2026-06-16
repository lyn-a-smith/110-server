from flask import Flask

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
        "id": 1,
        "title": "Nintendo Switch",
        "price": 499.99,
        "category": "Electronics",
        "image": "https://picsum.photos/300/200?random=1"
    },
    {
        "id": 2,
        "title": "Smart Refrigerator",
        "price": 999.99,
        "category": "Kitchen",
        "image": "https://picsum.photos/300/200?random=1"
    },
    {
        "id": 3,
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


if __name__ == '__main__':
    app.run(debug=True)