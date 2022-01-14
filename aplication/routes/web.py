from flask import Blueprint
from aplication.controllers import UserController, ErbController


user = Blueprint('user', __name__, template_folder='../views/modules/user')
user.route('/user/', methods=['GET'])(UserController.index)
user.route('/user/<int:id>', methods=['GET'])(UserController.show)
user.route('/user/create/', methods=['POST'])(UserController.store)
user.route('/user/<int:id>', methods=['POST'])(UserController.update)
user.route('/user/<int:id>', methods=['DELETE'])(UserController.destroy)

erb = Blueprint('erb', __name__, template_folder='../views/modules/erb')
erb.route('/erb/', methods=['GET'])(ErbController.index)
erb.route('/erb/<int:id>', methods=['GET'])(ErbController.show)
erb.route('/erb/create/', methods=['POST'])(ErbController.store)
erb.route('/erb/<int:id>', methods=['POST'])(ErbController.update)
erb.route('/erb/<int:id>', methods=['DELETE'])(ErbController.destroy)