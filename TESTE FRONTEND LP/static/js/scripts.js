// Função para redirecionar para a página home com o nome de usuário após o login
document.getElementById('loginForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    window.location.href = `/home?username=${username}`;
});

// Função para redirecionar para a página home após cadastrar usuário
document.getElementById('userForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Cadastro efetuado');
    window.location.href = '/home';
});

// Função para redirecionar para a página home com o nome de usuário após cadastrar exercício
document.getElementById('exerciseForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Cadastro de exercício efetuado');
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');
    window.location.href = `/home?username=${username}`;
});

// Função para redirecionar para a página de cadastro de treino
document.getElementById('treinoform')?.addEventListener('click', function() {
    e.preventDefault();
    alert('Cadastro de treino efetuado');
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');
    window.location.href = `/cadastro_treino?username=${username}`;
});

// Função para redirecionar para a página de visualizar treinos
document.getElementById('verTreinosBtn')?.addEventListener('click', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');
    window.location.href = `/visualizar_treinos?username=${username}`;
});
