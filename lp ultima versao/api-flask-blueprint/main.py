from flask import Blueprint
from controller.user import listarTodosUsuario, salvarUsuario, listarApenasUmUsuario, atualizarUmUsuario, removerUmUsuario, login
from controller.exercicio import listarTodosExercicio, salvarExercicio, listarApenasUmExercicio, atualizarUmExercicio, removerUmExercicio

blueprint = Blueprint('blueprint',__name__)

blueprint.route('/usuarios', methods=['GET'])(listarTodosUsuario)
blueprint.route('/usuario', methods=['POST'])(salvarUsuario)
blueprint.route('/usuario/<int:id>', methods=['GET'])(listarApenasUmUsuario)
blueprint.route('/usuario/<int:id>', methods=['PUT'])(atualizarUmUsuario)
blueprint.route('/usuario/<int:id>', methods=['DELETE'])(removerUmUsuario)
blueprint.route('/login', methods=['POST'])(login)

blueprint.route('/exercicios', methods=['GET'])(listarTodosExercicio)
blueprint.route('/exercicio', methods=['POST'])(salvarExercicio)
blueprint.route('/exercicio/<int:id>', methods=['GET'])(listarApenasUmExercicio)
blueprint.route('/exercicio/<int:id>', methods=['PUT'])(atualizarUmExercicio)
blueprint.route('/exercicio/<int:id>', methods=['DELETE'])(removerUmExercicio)
