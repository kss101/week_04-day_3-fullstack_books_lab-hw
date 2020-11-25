from flask import Flask, render_template, Blueprint, request, redirect
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors=authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
    # grab the form data for book: title, genre, publisher and author_id
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']

    # select the author using the repository
    author = author_repository.select(author_id)

    # create a new Book object
    book = Book(title, genre, publisher, author)

    # save the Book object to database with the .save method
    book_repository.save(book)

    return redirect('/books')

# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'

