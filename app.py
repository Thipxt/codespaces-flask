from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
books = [
   {"id": 1, "title": "Book 1", "author": "Author 1"},
   {"id": 2, "title": "Book 2", "author": "Author 2"},
   {"id": 3, "title": "Book 3", "author": "Author 3"}
]
@app.route("/")
def hello_world():
   return "<h1>Hello World</h1>"
# GET all books
@app.route("/books", methods=["GET"])
def get_all_books():
   return jsonify({"books": books})
# POST insert new book
@app.route("/books", methods=["POST"])
def insert_book():
   data = request.get_json()
   new_book = {
       "id": data["id"],
       "title": data["title"],
       "author": data["author"]
   }
   books.append(new_book)
   return jsonify({"message": "Book added successfully"})
# PUT update existing book
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
   data = request.get_json()
   for book in books:
       if book["id"] == id:
           book["title"] = data.get("title", book["title"])
           book["author"] = data.get("author", book["author"])
           return jsonify({"message": "Book updated successfully"})
   return jsonify({"error": "Book not found"}), 404
# DELETE delete existing book
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
   global books
   books = [book for book in books if book["id"] != id]
   return jsonify({"message": "Book deleted successfully"})
if __name__ == "__main__":
   app.run(host="0.0.0.0",port = 5000,debug = True)