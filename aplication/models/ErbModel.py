from app import db

class ErbModel(db.Model):
    # table name will default to name of the model
    __tablename__ = 'erbs'
    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    num_serie = db.Column(db.String(255), unique=True, nullable=False)
    name_machine = db.Column(db.String(255), nullable=False)
    nick_name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    api_token = db.Column(db.String(255), unique=True, nullable=False)
    created = db.Column(db.Date(), nullable=False)
    updated = db.Column(db.Date(), nullable=True)
    # define what each instance or row in the DB will have (id is taken care of for you)
    def __init__(self, id, user_id, num_serie, name_machine, nick_name, password, api_token, created, updated):
        self.id = id
        self.user_id = user_id
        self.num_serie = num_serie
        self.name_machine = name_machine
        self.nick_name = nick_name
        self.password = password
        self.api_token = api_token
        self.created = created
        self.updated = updated

    # this is not essential, but a valuable method to overwrite as this is what we will see when we print out an instance in a REPL.
    def __repr__(self):
        return f"ErbModel('{self.id}','{self.user_id}','{self.num_serie}','{self.name_machine}','{self.nick_name}','{self.password}','{self.api_token}','{self.created}','{self.updated}')"

    #@property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'num_serie': self.num_serie,
            'name_machine': self.name_machine,
            'nick_name': self.nick_name,
            'password': self.password,
            'api_token': self.api_token,
            'created': self.created,
            'updated': self.updated
        }