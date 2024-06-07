from config.config import get_db_connection


def listagemTodosExercicios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM exercicios')
    exercicios = cursor.fetchall()
    conn.close()
    return exercicios

def salvarExercicio(exercicio):    
    nome = exercicio.get('nome')
    grupo_muscular = exercicio.get('Grupo muscular')
    descricao = exercicio.get('Descrição')
    
    conn = get_db_connection()
    cursor = conn.cursor() 
    cursor.execute(
        'INSERT INTO exercicios (nome, grupo_muscular, descricao) VALUES (%s, %s,%s)',
          (nome, grupo_muscular, descricao))
    conn.commit()
    conn.close()


def listarApenasUmExercicio(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)    
    cursor.execute("SELECT * FROM exercicios WHERE id = %s", (id,))
    exercicio = cursor.fetchone()
    conn.close()
    return exercicio         

def atualizarUmExercicio(id, exercicio):
    nome = exercicio.get('nome')
    grupo_muscular = exercicio.get('Grupo muscular')
    descricao = exercicio.get('Descrição')


    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE exercicios SET nome = %s, grupo_muscular = %s, descricao = %s WHERE id = %s", (nome, grupo_muscular, descricao, id))
    connection.commit()
    cursor.close()
    connection.close()

def removerUmExercicio(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM exercicios WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()



    