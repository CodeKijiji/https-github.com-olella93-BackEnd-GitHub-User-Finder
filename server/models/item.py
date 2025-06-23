from server.extensions import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    github_username = db.Column(db.String, nullable=False)
    note = db.Column(db.String)
    category = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    comments = db.relationship('Comment', backref='item', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Item {self.github_username} by User {self.user_id}>"
