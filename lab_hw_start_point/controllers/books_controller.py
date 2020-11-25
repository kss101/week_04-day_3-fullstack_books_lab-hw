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
@books_blueprint.route('/books/<id>', methods=["GET"])
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)


# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit" , methods=["GET"])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", authors=authors, book=book)


# UPDATE
# PUT '/books/<id>'
@books_blueprint.route('/books/<id>', methods=["POST"])
def update_book(id):
    # grab the form data for book: title, genre, publisher
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
   
    # select the author from the repository
    author = author_repository.select(request.form['author_id'])

    # create a new Book object
    book = Book(title, genre, publisher, author)

    # save the Book object to database with the .update method
    book_repository.update(book)

    return redirect('/books')


# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')
