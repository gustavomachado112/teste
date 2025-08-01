// --- Lógica de Alternância de Tema ---
// CORRIGIDO: O ID do botão é 'modo-btn', não 'toggleThemeBtn'
const modoBtn = document.getElementById('modo-btn');
const body = document.body;

// Inicializa o tema ao carregar a página
const temaSalvo = localStorage.getItem('tema');
if (temaSalvo === 'dark') {
  body.classList.add('dark-mode');
  modoBtn.textContent = '☀️'; // Ícone de sol para modo escuro
} else {
  body.classList.remove('dark-mode'); // Garante que a classe não esteja presente se não for dark
  modoBtn.textContent = '🌙'; // Ícone de lua para modo claro
  // Se não houver tema salvo, define como 'light' para consistência
  if (!temaSalvo) {
    localStorage.setItem('tema', 'light');
  }
}

modoBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode'); // Alterna a classe 'dark-mode' no <body>
  const novoTema = body.classList.contains('dark-mode') ? 'dark' : 'light';
  localStorage.setItem('tema', novoTema); // Salva a nova preferência no localStorage
  modoBtn.textContent = novoTema === 'dark' ? '☀️' : '🌙'; // Atualiza o ícone do botão
});


// --- Lógica de Notificações ---
document.getElementById('notificationBtn').addEventListener('click', () => {
  const dropdown = document.getElementById('notificationDropdown');
  dropdown.hidden = !dropdown.hidden; // Isso alterna o atributo 'hidden'
});

// --- Lógica do Formulário de Tarefas (AGORA COM confirm() NATIVO E SEM SALVAR VISUALMENTE) ---
const form = document.getElementById('taskForm');
// REMOVIDO: const taskList = document.getElementById('taskList'); - Não usaremos mais para exibir tarefas.

form.addEventListener('submit', (e) => {
  e.preventDefault(); // Impede o envio padrão do formulário

  // CORRIGIDO: Usando confirm() nativo, como você pediu
  const confirmacao = confirm("Deseja realmente salvar esta tarefa?");

  if (confirmacao) {
    // Se o usuário clicar em "OK"
    alert("Tarefa salva com sucesso!"); // Feedback com alert() nativo
    form.reset(); // Limpa os campos do formulário
    // REMOVIDO: Lógica de criação e adição de taskItem a taskList
  } else {
    // Se o usuário clicar em "Cancelar"
    alert("Criação da tarefa cancelada."); // Feedback com alert() nativo
  }
});

// --- Lógica de Comentários ---
const commentInput = document.getElementById('commentInput');
const addCommentBtn = document.getElementById('addCommentBtn');
const commentsList = document.getElementById('commentsList');

addCommentBtn.addEventListener('click', () => {
    const commentText = commentInput.value.trim();
    if (commentText) {
        const commentDiv = document.createElement('div');
        commentDiv.classList.add('comment-item'); // Para estilização
        commentDiv.innerHTML = `<p>${commentText}</p>`;
        commentsList.appendChild(commentDiv);
        commentInput.value = ''; // Limpa o campo de comentário
    } else {
        alert('Por favor, digite um comentário antes de adicionar.'); // Alert nativo
    }
});
