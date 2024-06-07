from model.exercicio import listagemTodosExercicios, salvarExercicio, listarApenasUmExercicio, atualizarUmExercicio, removerUmExercicio

def listagemTodosExerciciosService():    
    return listagemTodosExercicios()

def salvarExercicioService(exercicio):    
    return salvarExercicio(exercicio)   

def listarApenasUmExercicioService(id):    
    return listarApenasUmExercicio(id) 

def atualizarUmExercicioService(id, exercicio):
    return atualizarUmExercicio(id, exercicio) 

def removerUmExercicioService(id):
    return removerUmExercicio(id) 


