from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulação de banco de dados para os exercícios
exercicios = []
treinos = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    username = request.args.get('username', 'Usuário')
    return render_template('home.html', username=username)

@app.route('/meu_perfil')
def meu_perfil():
    username = request.args.get('username', 'Usuário')
    return render_template('meu_perfil.html', username=username)

@app.route('/cadastro_exercicio', methods=['GET', 'POST'])
def cadastro_exercicio():
    if request.method == 'POST':
        nome_exercicio = request.form['nome_exercicio']
        grupo_muscular = request.form['grupo_muscular']
        descricao = request.form['descricao']
        exercicios.append({
            'nome': nome_exercicio,
            'grupo_muscular': grupo_muscular,
            'descricao': descricao
        })
        return redirect(url_for('home', username=request.args.get('username', 'Usuário')))
    return render_template('cadastro_exercicio.html')

@app.route('/visualizar_exercicios')
def visualizar_exercicios():
    username = request.args.get('username', 'Usuário')
    return render_template('visualizar_exercicios.html', exercicios=exercicios, username=username)

@app.route('/calendario')
def calendario():
    username = request.args.get('username', 'Usuário')
    return render_template('calendario.html', username=username)

@app.route('/cadastro_treino')
def cadastro_treino():
    return render_template('cadastro_treino.html')

@app.route('/visualizar_treinos')
def visualizar_treinos():
    return render_template('visualizar_treinos.html', treinos=treinos)

@app.route('/salvar_treino', methods=['POST'])
def salvar_treino():
    nome_treino = request.form['nome_treino']
    treinos.append(nome_treino)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
