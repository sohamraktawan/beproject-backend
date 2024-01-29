from mongoengine import Document, StringField, EmailField
from werkzeug.security import generate_password_hash, check_password_hash
from validators import email, length

class User(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True, validation=email("Please enter a valid email"))
    password = StringField(required=True, validation=length(min=6, error="The password should be at least 6 characters long"))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    @staticmethod
    def login(email, password):
        user = User.objects(email=email).first()
        if user and check_password_hash(user.password, password):
            return user
        raise Exception('incorrect email' if not user else 'incorrect password')
