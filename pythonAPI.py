from flask import flask
from flask_sqlachemy import SQLAlchemy
import Json

app.config["SQUALCHEMY_DATABASE_URL"] = 'sqilte:///data.db'

db = SQLAlchemy(app)

class book(db.model):
    id = db.colum(db.integer, primary_key=True)
    book_name = db.colum(db.string(90),unique=True , nullable =False)
    author = db.colum(db.string(90),nullable=False)
    publisher = db.colum(db.string(90),nullable = False)

@app.route('/')
def index():
    return "hello"

@app.route('/books')
def get_books():
    Books= book.query.all()
    output=[]
    for Book in Books:
        book_data = {'id':book.id,'book_name': book.book_name,'author':book.author, 'publisher':book.publisher}
        return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    Book = book.query.get_or_404(id)
    return {'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}

@app.route('/books/', method = ['Post'])
def app_book():
    Book = book(book_name = request.json['book_name'],author = request.json ['author'],publisher = request.json['publisher'])
    db.session.add(Book)
    db.session.commit()
    return {'id':book.id}

@app.route("/books/<id>",method=['Delete'])
def delete_drink(id):
    Book = book.query.get(id)
    if Book is None:
        return {"error": "not found"}
    db.session.delete(Book)
    db.session.commit()
    return {"message": "ID has been deleted"}