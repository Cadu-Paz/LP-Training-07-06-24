from flask import make_response, jsonify, request
from service.exercicio import salvarExercicioService, listagemTodosExerciciosService, listarApenasUmExercicioService, atualizarUmExercicioService, removerUmExercicioService

def listarTodosExercicio():    
    return make_response(
        jsonify(
            mensagem = "Listagem de Exercicios",
            exercicios = listagemTodosExerciciosService()
        )
    ) 

def salvarExercicio():    
    exercicio = request.json     
    if not isinstance(exercicio.get('senha'), str):
        return make_response(
            jsonify(
              mensagem = "Senha deve ser uma string"  
            )
        )
       
    salvarExercicioService(exercicio)
    return make_response(
        jsonify(
            mensagem = "Cadastro com sucesso!!"
        )
    )

def listarApenasUmExercicio(id):       
    return make_response(
        jsonify(
            mensagem = "Exercicio",
            exercicio = listarApenasUmExercicioService(id)
        )
    ) 

def atualizarUmExercicio(id): 
    exercicio = request.json
    
    if not isinstance(exercicio.get('senha'), str):
        return make_response(
            jsonify(
              mensagem = "Senha deve ser uma string"  
            )
        )
    
    atualizarUmExercicioService(id, exercicio)          
    return make_response(
        jsonify(
            mensagem = "Exercicio Atualizado com sucesso!!"
        )
    ) 

def removerUmExercicio(id):     
    removerUmExercicioService(id)          
    return make_response(
        jsonify(
            mensagem = "Exercicio Removido com sucesso!!"
        )
    )