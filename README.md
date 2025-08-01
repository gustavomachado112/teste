# 📅 Agenda Inteligente

## 📌 1. Nome do Projeto
**Agenda Inteligente**

## 🎯 2. Objetivo do Sistema
Organizar tarefas com agenda inteligente.

## 👥 3. Público-Alvo / Usuários
Pessoas adultas que querem organizar suas tarefas diárias.

## ⚙️ 4. Funcionalidades Principais
- Permitir modificar tarefas  
- Avisar quando uma tarefa estiver próxima  
- Buscar tarefas  

## ✅ 5. Requisitos Funcionais
- **Permitir que o usuário crie, edite e apague suas tarefas e compromissos.**  
- **Avisar o usuário com um alerta quando a tarefa estiver próxima do horário.**  
- **Mostrar uma lista com todas as tarefas para o usuário visualizar.**  
- **Permitir buscar uma tarefa pelo nome ou data.**

## 🚀 6. Requisitos Não Funcionais
- **Desempenho rápido na consulta e atualização dos dados.**  
- **Segurança básica para proteção dos dados pessoais (senha, email, telefone, CPF).**  
- **Usabilidade simples e clara para facilitar o uso por qualquer pessoa.**  
- **Tempo de resposta adequado, especialmente para notificações em tempo real.**  
- **Persistência local confiável dos dados (banco local).**

## 📝 7. Entradas do Sistema
- **Dados pessoais: nome, email, senha, telefone, CPF (opcional).**  
- **Dados das tarefas e eventos: nome, descrição, datas de início e fim, prioridade, status.**  
- **Dados de compartilhamento e permissões.**  
- **Dados para sincronização externa (tokens, tipos de serviço).**

## 📤 8. Saídas do Sistema
- **Notificações e alertas sobre tarefas próximas do prazo.**  
- **Listas e relatórios de tarefas, eventos e calendários.**  
- **Confirmações de criação, edição ou exclusão de dados.**  
- **Exibição dos dados cadastrados com formatação amigável.**

## 👤 9. Atores Envolvidos
- **Usuário comum**: pessoa que usa a agenda para organizar suas tarefas diárias.

## 📌 10. Casos de Uso ou Cenários
- **Usuário cadastra uma nova tarefa com prazo e descrição.**  
- **Usuário recebe alerta 30 minutos antes da tarefa expirar.**  
- **Usuário busca por tarefas relacionadas a um projeto específico.**  
- **Usuário compartilha uma tarefa com colega, definindo permissão de leitura.**  
- **Usuário visualiza o calendário semanal com todos os eventos.**

## 🔄 11. Fluxo das Operações
- **Login do usuário (autenticação).**  
- **Menu principal: escolher entre criar, editar, listar ou buscar tarefas/eventos.**  
- **Cadastro ou edição da tarefa/evento com dados necessários.**  
- **Salvamento local dos dados.**  
- **Verificação periódica para enviar notificações.**  
- **Visualização e compartilhamento.**  
- **Logout ou encerramento da sessão.**

## ⚠️ 12. Restrições de Uso
- **Apenas o criador pode editar ou excluir suas tarefas.**  
- **Permissões de leitura/escrita para tarefas compartilhadas.**  
- **Limite mínimo para campos obrigatórios (ex: nome da tarefa não pode ficar vazio).**  
- **Validação dos formatos de data e dados pessoais.**

## 🖥️ 14. Plataforma Alvo
- **Web e mobile**

## 🔒 15. Autenticação e Segurança
- **Sistema com login por email e senha.**  
- **Senhas armazenadas de forma segura.**  
- **Controle de permissões para tarefas e compartilhamentos (leitura, escrita, total).**

## 🗂️ 16. Armazenamento de Dados
- **Informações dos clientes, salvas localmente em um banco de dados.**

## 🎨 17. Layout e Design Desejado
- **Interface simples e funcional para terminal no momento.**  
- **Foco em clareza e usabilidade, com mensagens diretas e amigáveis.**  
- **Futuramente, vai ser adaptado para HTML e CSS.**

## 🏆 18. Critérios de Sucesso
- **Usuário consegue cadastrar, editar, buscar e excluir tarefas e eventos sem erros.**  
- **Notificações funcionam corretamente para avisar das tarefas próximas.**  
- **Dados persistem corretamente após o encerramento do programa.**  
- **Permissões de compartilhamento são respeitadas.**  
- **Sistema é estável, responsivo e de fácil uso para o público-alvo.**


## 💻 Requisitos front-end
- 🧩 1.Responsividade
- 🧱 2.Layout consistente
- 🧼 3.Design limpo e intuitivo
- 🌐 4.Compatibilidade entre navegadores
- ♻️ 5.Componentes reutilizáveis
- 🎨 6.Sistema de cores acessível
- 🧭 7.Barra de navegação acessível
- 🔁 8.Sistema de feedback visual
- ♿ 9.Acessibilidade
- 🖼️ 10.Ícones e ilustrações funcionais
- 📱 11.Mensagens e alertas responsivos(Sweet Alert)
- ⚠️ 12.Confirmações antes de ações críticas(Sweet Alert)
- 🌙 13.Compatibilidade com temas claro/escuro (dark mode)
