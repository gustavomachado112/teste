const toggleBtn = document.getElementById("modo-btn");
const body = document.body;

const temaSalvo = localStorage.getItem('tema') || 'light';
if (temaSalvo === 'dark') {
  body.classList.add('dark-mode');
  toggleBtn.textContent = '☀️';
} else {
  toggleBtn.textContent = '🌙';
}

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  const novoTema = body.classList.contains('dark-mode') ? 'dark' : 'light';
  localStorage.setItem('tema', novoTema);
  toggleBtn.textContent = novoTema === 'dark' ? '☀️' : '🌙';
});

const notificationBtn = document.getElementById("notificationBtn");
const notificationDropdown = document.getElementById("notificationDropdown");

notificationBtn.addEventListener("click", () => {
  const isHidden = notificationDropdown.hasAttribute("hidden");
  if (isHidden) {
    notificationDropdown.removeAttribute("hidden");
  } else {
    notificationDropdown.setAttribute("hidden", "");
  }
});

document.addEventListener("click", e => {
  if (!notificationBtn.contains(e.target) && !notificationDropdown.contains(e.target)) {
    notificationDropdown.setAttribute("hidden", "");
  }
});

const formPrioridade = document.getElementById("formPrioridade");
const prioridadesList = document.getElementById("prioridadesList");
const noPrioritiesMessage = prioridadesList.querySelector('.no-priorities-message');

noPrioritiesMessage.style.display = 'block';

formPrioridade.addEventListener("submit", (event) => {
  event.preventDefault();

  const confirmacao = confirm("Deseja realmente adicionar esta prioridade?");
  if (!confirmacao) {
    return;
  }

  const nome = document.getElementById("nome").value;
  const urgencia = document.getElementById("urgencia").value;

  alert(`Prioridade "${nome}" (Urgência: ${urgencia}) adicionada com sucesso!`);

  formPrioridade.reset();

  while (prioridadesList.children.length > 1) {
    if (prioridadesList.lastChild !== noPrioritiesMessage && prioridadesList.lastChild.tagName !== 'H2') {
        prioridadesList.removeChild(prioridadesList.lastChild);
    } else {
        break;
    }
  }
  noPrioritiesMessage.style.display = 'block';
});
