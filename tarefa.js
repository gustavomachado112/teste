const toggleBtn = document.getElementById('toggleThemeBtn');
const body = document.body;

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
});

const form = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  Swal.fire({
    title: 'Confirmar criação?',
    text: 'Você tem certeza que quer criar esta tarefa?',
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Sim, criar',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.isConfirmed) {
      const taskName = document.getElementById('taskName').value;
      const description = document.getElementById('description').value;

      const taskItem = document.createElement('div');
      taskItem.classList.add('task-item');
      taskItem.innerHTML = `
        <strong>${taskName}</strong><br>
        <p>${description}</p>
        <button class="delete-btn">Excluir</button>
      `;

      taskItem.querySelector('.delete-btn').addEventListener('click', () => {
        Swal.fire({
          title: 'Excluir tarefa?',
          text: 'Tem certeza que deseja excluir esta tarefa?',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Sim, excluir',
          cancelButtonText: 'Cancelar'
        }).then((res) => {
          if (res.isConfirmed) {
            taskItem.remove();
          }
        });
      });

      taskList.appendChild(taskItem);
      form.reset();
    }
  });
});
document.getElementById('notificationBtn').addEventListener('click', () => {
  const dropdown = document.getElementById('notificationDropdown');
  dropdown.hidden = !dropdown.hidden;
});
