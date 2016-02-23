from hiren import db


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comments_url = db.Column(db.String(300), unique=True)

    def __init__(self, comments_url):
        self.comments_url = comments_url

    def __repr__(self):
        return '<url %r>' % self.comments_url

db.create_all()