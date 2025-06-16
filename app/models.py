# يحتوي على نموذج قاعدة البيانات
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    cover_url = db.Column(db.String(255), nullable=True)
    publish_year = db.Column(db.String(10), nullable=True)

# دالة لإضافة 10 كتب وهمية إلى قاعدة البيانات
def seed_data():
    if Book.query.count() == 0:
        books = [
            Book(title="1984", author="George Orwell", cover_url="", publish_year="1949"),
            Book(title="To Kill a Mockingbird", author="Harper Lee", cover_url="", publish_year="1960"),
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald", cover_url="", publish_year="1925"),
            Book(title="Pride and Prejudice", author="Jane Austen", cover_url="", publish_year="1813"),
            Book(title="Moby-Dick", author="Herman Melville", cover_url="", publish_year="1851"),
            Book(title="War and Peace", author="Leo Tolstoy", cover_url="", publish_year="1869"),
            Book(title="The Catcher in the Rye", author="J.D. Salinger", cover_url="", publish_year="1951"),
            Book(title="The Hobbit", author="J.R.R. Tolkien", cover_url="", publish_year="1937"),
            Book(title="Crime and Punishment", author="Fyodor Dostoevsky", cover_url="", publish_year="1866"),
            Book(title="The Brothers Karamazov", author="Fyodor Dostoevsky", cover_url="", publish_year="1880"),
        ]
        db.session.add_all(books)
        db.session.commit()