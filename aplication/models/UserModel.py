from app import db

class UserModel(db.Model):
    # table name will default to name of the model
    __tablename__ = 'users'
    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    email_verified = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    remember_token = db.Column(db.String(255), unique=True, nullable=False)
    created = db.Column(db.Date(), nullable=False)
    updated = db.Column(db.Date(), nullable=True)
    # define what each instance or row in the DB will have (id is taken care of for you)
    def __init__(self, id, name, email, email_verified, password, remember_token, created, updated):
        self.id = id
        self.name = name
        self.email = email
        self.email_verified = email_verified
        self.password = password
        self.remember_token = remember_token
        self.created = created
        self.updated = updated

    # this is not essential, but a valuable method to overwrite as this is what we will see when we print out an instance in a REPL.
    def __repr__(self):
        return f"UserModel('{self.id}','{self.name}','{self.email}','{self.email_verified}','{self.password}','{self.remember_token}','{self.created}','{self.updated}')"

    #@property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'email_verified': self.email_verified,
            'remember_token': self.remember_token,
            'created': self.created,
            'updated': self.updated
        }