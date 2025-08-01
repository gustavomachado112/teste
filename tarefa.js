// --- Lógica de Alternância de Tema ---
// Certifica-se de que o ID do botão no HTML ('modo-btn') corresponde ao ID no JavaScript.
const modoBtn = document.getElementById('modo-btn');
const body = document.body;

// Inicializa o tema ao carregar a página, lendo a preferência salva no localStorage.
const temaSalvo = localStorage.getItem('tema');
if (temaSalvo === 'dark') {
  body.classList.add('dark-mode'); // Adiciona a classe se o tema salvo for escuro
  if (modoBtn) { // Verifica se o botão existe antes de tentar modificar seu texto
    modoBtn.textContent = '☀️'; // Ícone de sol para modo escuro
  }
} else {
  body.classList.remove('dark-mode'); // Garante que a classe não esteja presente se não for dark
  if (modoBtn) { // Verifica se o botão existe antes de tentar modificar seu texto
    modoBtn.textContent = '🌙'; // Ícone de lua para modo claro
  }
  // Se não houver tema salvo, define como 'light' para consistência futura
  if (!temaSalvo) {
    localStorage.setItem('tema', 'light');
  }
}

// Adiciona o ouvinte de evento de clique ao botão do modo.
// A verificação 'if (modoBtn)' é importante caso o elemento não seja encontrado, prevenindo erros.
if (modoBtn) {
  modoBtn.addEventListener('click', () => {
    body.classList.toggle('dark-mode'); // Alterna a classe 'dark-mode' no <body>
    const novoTema = body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('tema', novoTema); // Salva a nova preferência no localStorage
    modoBtn.textContent = novoTema === 'dark' ? '☀️' : '🌙'; // Atualiza o ícone do botão
  });
} else {
  console.error("Botão de modo escuro (ID 'modo-btn') não encontrado no HTML.");
}


// --- Lógica de Notificações ---
const notificationBtn = document.getElementById('notificationBtn');
const notificationDropdown = document.getElementById('notificationDropdown');

if (notificationBtn && notificationDropdown) {
  notificationBtn.addEventListener('click', () => {
    notificationDropdown.hidden = !notificationDropdown.hidden; // Isso alterna o atributo 'hidden'
  });
} else {
  console.error("Botão de notificação (ID 'notificationBtn') ou dropdown (ID 'notificationDropdown') não encontrado no HTML.");
}


// --- Lógica do Formulário de Tarefas (AGORA COM confirm() NATIVO E SEM SALVAR VISUALMENTE) ---
const form = document.getElementById('taskForm');

if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // Impede o envio padrão do formulário

    // Usando confirm() nativo para confirmação.
    const confirmacao = confirm("Deseja realmente salvar esta tarefa?");

    if (confirmacao) {
      // Se o usuário clicar em "OK"
      alert("Tarefa salva com sucesso!"); // Feedback com alert() nativo
      form.reset(); // Limpa os campos do formulário
      // A lógica de criação e adição de taskItem a taskList foi removida.
    } else {
      // Se o usuário clicar em "Cancelar"
      alert("Criação da tarefa cancelada."); // Feedback com alert() nativo
    }
  });
} else {
  console.error("Formulário de tarefa (ID 'taskForm') não encontrado no HTML.");
}


// --- Lógica de Comentários ---
const commentInput = document.getElementById('commentInput');
const addCommentBtn = document.getElementById('addCommentBtn');
const commentsList = document.getElementById('commentsList');

if (commentInput && addCommentBtn && commentsList) {
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
} else {
  console.error("Elementos de comentário (input, botão ou lista) não encontrados no HTML.");
}
