# يحتوي على جميع المسارات المتعلقة بالكتب (CRUD)
from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Book

main_bp = Blueprint("main_bp", __name__)

# عرض كل الكتب
@main_bp.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

# إضافة كتاب جديد
@main_bp.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            cover_url=request.form["cover_url"],
            publish_year=request.form["publish_year"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("main_bp.index"))
    return render_template("add_book.html")

# تعديل كتاب
@main_bp.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.cover_url = request.form["cover_url"]
        book.publish_year = request.form["publish_year"]
        db.session.commit()
        return redirect(url_for("main_bp.index"))
    return render_template("edit_book.html", book=book)

# حذف كتاب
@main_bp.route("/delete/<int:book_id>")
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("main_bp.index"))