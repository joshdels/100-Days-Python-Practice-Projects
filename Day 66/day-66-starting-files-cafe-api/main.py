from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    def to_dict(self):
        dictionary = {}
        
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
            
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    results = db.session.execute(db.select(Cafe))
    all_cafes = results.scalars().all()
    random_cafe = random.choice(all_cafes)
    
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all", methods=["GET"])
def get_all_cafe():
    results = db.session.execute(db.select(Cafe))
    all_cafes = results.scalars().all()

    all_cafes_list = []
    for cafe in all_cafes:
        all_cafes_list.append(cafe.to_dict())
        
    return jsonify(cafe=all_cafes_list)

# HTTP POST - Create Record
@app.route("/search")
def search():
    query_location = request.args.get("loc")
    results = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = results.scalars().all()
    
    if all_cafes:
        return jsonify(cafe = [cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error=["Not Found: we dont have that location."]),404    
    
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_wifi=bool(request.form.get("has_wifi")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe"})
    
# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        return jsonify(response={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"Success": "Successfully updated the price"}), 200
        
# HTTP DELETE - Delete Records
@app.route("/report-close/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api-key") == "TopSecretAPIKey": 
        cafe = db.session.get(Cafe, cafe_id)
        if cafe is None:
            return jsonify(response={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Remove the cafe"}), 200
    else: 
        return jsonify(response={"error": "Sorry, that's not allowed. Make sure you have the correct api_keys"}), 403
    


if __name__ == '__main__':
    app.run(debug=True)
    
# I got introduction in postman
# https://.postman.co/workspace/My-Workspace~e1f434ef-5e3b-49ef-86f6-9f736f9fd2cc/collection/45527495-ea68e224-586e-424e-b45f-953880d2f955?action=share&creator=45527495
