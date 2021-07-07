from sqlalchemy.sql.operators import desc_op
from bot import db

class NewsArticle(db.Model):
    title = db.Column(db.String())
    description = db.Column(db.String())
    publication_date_and_time = db.Column(db.String())
    link = db.Column(db.String())

    def __repr__(self):
        return f"\n{self.title}\n{self.link}\n"

db.create_all()