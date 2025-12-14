[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-red)](https://www.django-rest-framework.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Descrição

O **Sistema de Gestão de Clientes e Serviços** é uma aplicação web completa desenvolvida em Django para gerenciar ordens de serviço, clientes, serviços e status de forma eficiente. Ideal para assistências técnicas, oficinas e empresas de manutenção que precisam organizar solicitações de serviço, rastrear o progresso e gerar relatórios.

### ✨ Funcionalidades Principais

#### 🎯 Gestão Completa
- **Ordens de Serviço**: Crie, edite, visualize e exclua ordens com sistema completo de CRUD
- **Cadastro de Clientes**: Gerencie informações completas (nome, email, telefone)
- **Catálogo de Serviços**: Cadastre serviços com descrição e preço
- **Status Personalizáveis**: Defina status customizados para rastrear o progresso das ordens
- **Detalhes Completos**: Visualize todas as informações de cada ordem em tela dedicada

#### 🔍 Busca e Filtros
- **Busca Inteligente**: Pesquise ordens por cliente, ID ou descrição do problema
- **Filtros por Status**: Filtre ordens rapidamente por status (Pendente, Em Andamento, Concluída)
- **Busca de Clientes**: Encontre clientes por nome ou email
- **Busca de Serviços**: Localize serviços cadastrados rapidamente
- **Paginação**: Navegação eficiente com 10-12 registros por página

#### 📊 Dashboard com Analytics
- **Visão Geral Completa**: Cards com totais de ordens, clientes, serviços e receita
- **Gráficos Interativos** (Chart.js):
  - Ordens por mês (últimos 6 meses) - Gráfico de linha
  - Distribuição de ordens por status - Gráfico de pizza
  - Receita mensal - Gráfico de barras
- **Top 5**: Clientes com mais ordens e serviços mais solicitados
- **Ordens Recentes**: Visualização rápida das 5 últimas ordens
- **Contadores**: Ordens pendentes e concluídas em tempo real

#### 🔐 API REST Completa
- **Endpoints RESTful**: API completa para todas as entidades
- **Autenticação**: Session e Basic Authentication
- **Serializers Otimizados**: 
  - Listagem simplificada para performance
  - Detalhes completos com dados aninhados
- **Filtros e Busca**: django-filter integrado
- **Paginação**: 10 registros por página
- **CORS**: Configurado para integração com frontends
- **Dashboard API**: Endpoint dedicado com todas as métricas

#### ✅ Validações e Regras de Negócio
- **Validação de Email**: Impede duplicação de emails de clientes
- **Data de Conclusão**: Obrigatória para ordens com status "Concluída"
- **Integridade Referencial**: Proteção contra exclusão acidental (PROTECT em FKs)
- **Validações Customizadas**: Em forms e serializers

#### 💾 Exportação de Dados
- **Exportação CSV**: Exporte todas as ordens com dados completos
- **Formato UTF-8**: Compatível com Excel e Google Sheets
- **Dados Incluídos**: Cliente, serviço, preço, status, datas e problema

#### 🎨 Interface Moderna
- **Design Responsivo**: Funciona perfeitamente em desktop, tablet e mobile
- **Cards Visuais**: Interface com cards para clientes, serviços e status
- **Tabelas Otimizadas**: Listagem de ordens em formato tabular
- **Badges de Status**: Indicadores visuais coloridos por status
- **Emojis e Ícones**: Interface amigável e intuitiva
- **Mensagens de Feedback**: Django Messages para confirmação de ações
- **Confirmação de Exclusão**: Tela dedicada antes de deletar registros

#### 🔧 Recursos Técnicos
- **Admin Django**: Interface administrativa completa
- **Select Related**: Queries otimizadas com joins
- **Aggregations**: Cálculos de totais, contagens e somas
- **Date Functions**: TruncMonth para agrupamento temporal
- **Ordenação**: Listas ordenadas por critérios lógicos
- **Meta Classes**: Verbose names em português para melhor UX

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 4.2**: Framework web robusto
- **Python 3.11**: Linguagem de programação
- **Django REST Framework 3.14**: API RESTful
- **django-filter**: Filtros automáticos para API
- **django-cors-headers**: Configuração de CORS

### Frontend
- **HTML5**: Estrutura semântica
- **CSS3**: Estilização moderna (Grid, Flexbox, Transitions)
- **Chart.js 4.4**: Gráficos interativos
- **JavaScript Vanilla**: Sem dependências pesadas

### Banco de Dados
- **SQLite**: Desenvolvimento (padrão Django)
- **PostgreSQL/MySQL**: Produção (fácil migração)

## 📦 Instalação

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git instalado

### Passos para Instalação

1. **Clone o Repositório**:
```bash
git clone https://github.com/seu-usuario/sistema-assistencia.git
cd sistema-assistencia
```

2. **Crie um Ambiente Virtual**:
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate
```

3. **Instale as Dependências**:
```bash
pip install -r requirements.txt
```

**Dependências Principais**:
```
Django==4.2
djangorestframework==3.14.0
django-filter==23.5
django-cors-headers==4.3.1
```

4. **Configure o Banco de Dados**:
```bash
cd assistencia
python manage.py migrate
```

5. **Crie um Superusuário** (para acesso admin):
```bash
python manage.py createsuperuser
```
*Siga as instruções para definir username, email e senha*

6. **Execute o Servidor de Desenvolvimento**:
```bash
python manage.py runserver
```

7. **Acesse a Aplicação**:
- **Interface Web**: http://127.0.0.1:8000/
- **Dashboard**: http://127.0.0.1:8000/dashboard/
- **Admin Django**: http://127.0.0.1:8000/admin/
- **API REST**: http://127.0.0.1:8000/api/
- **API Browsable**: http://127.0.0.1:8000/api-auth/

## 🚀 Uso

### Interface Web

1. **Login**: Use as credenciais do superusuário criado
2. **Dashboard**: Visualize métricas e gráficos em tempo real
3. **Navegação**: Use o menu para acessar Ordens, Clientes, Serviços e Status

#### Fluxo Básico de Uso

**1. Cadastrar Dados Básicos:**
```
Status → Criar → "Pendente", "Em Andamento", "Concluída"
Clientes → Novo Cliente → Preencher dados
Serviços → Novo Serviço → Nome, descrição, preço
```

**2. Criar Ordem de Serviço:**
```
Ordens → Nova Ordem
↓
Selecionar: Cliente, Serviço, Status
↓
Descrever o problema
↓
Salvar
```

**3. Gerenciar Ordens:**
```
- Ver detalhes (👁️)
- Editar status/data conclusão (✏️)
- Filtrar por status
- Buscar por cliente/problema
- Excluir se necessário (🗑️)
```

**4. Exportar Dados:**
```
Menu → Exportar → Baixa CSV com todas as ordens
```

### API REST

#### Endpoints Disponíveis

```
GET    /api/clientes/           # Listar clientes
POST   /api/clientes/           # Criar cliente
GET    /api/clientes/{id}/      # Detalhe do cliente
PUT    /api/clientes/{id}/      # Atualizar cliente completo
PATCH  /api/clientes/{id}/      # Atualizar campos específicos
DELETE /api/clientes/{id}/      # Excluir cliente

GET    /api/servicos/           # Listar serviços
POST   /api/servicos/           # Criar serviço
GET    /api/servicos/{id}/      # Detalhe do serviço
PUT    /api/servicos/{id}/      # Atualizar serviço
PATCH  /api/servicos/{id}/      # Atualizar parcial
DELETE /api/servicos/{id}/      # Excluir serviço

GET    /api/status/             # Listar status
POST   /api/status/             # Criar status
GET    /api/status/{id}/        # Detalhe do status
PUT    /api/status/{id}/        # Atualizar status
PATCH  /api/status/{id}/        # Atualizar parcial
DELETE /api/status/{id}/        # Excluir status

GET    /api/ordens/             # Listar ordens
POST   /api/ordens/             # Criar ordem
GET    /api/ordens/{id}/        # Detalhe da ordem
PUT    /api/ordens/{id}/        # Atualizar ordem
PATCH  /api/ordens/{id}/        # Atualizar parcial
DELETE /api/ordens/{id}/        # Excluir ordem

GET    /api/dashboard/          # Métricas do dashboard
```

#### Exemplos de Uso da API

**Listar Clientes com Filtros:**
```bash
# Buscar por nome
curl -u admin:senha http://localhost:8000/api/clientes/?search=João

# Ordenar
curl -u admin:senha http://localhost:8000/api/clientes/?ordering=nome

# Paginação
curl -u admin:senha http://localhost:8000/api/clientes/?page=2
```

**Criar Ordem de Serviço:**
```bash
curl -X POST http://localhost:8000/api/ordens/ \
  -u admin:senha \
  -H "Content-Type: application/json" \
  -d '{
    "cliente_id": 1,
    "servico_id": 2,
    "status_id": 1,
    "descricao_problema": "Tela quebrada"
  }'
```

**Dashboard com Métricas:**
```bash
curl -u admin:senha http://localhost:8000/api/dashboard/
```

**Resposta:**
```json
{
  "total_ordens": 45,
  "total_clientes": 23,
  "total_servicos": 8,
  "receita_total": "15420.00",
  "ordens_pendentes": 12,
  "ordens_concluidas": 30,
  "ordens_por_status": [...],
  "ordens_por_mes": [...],
  "receita_por_mes": [...],
  "top_clientes": [...],
  "top_servicos": [...]
}
```

## 🧪 Testes

O projeto inclui uma suite completa de testes para a API REST:

```bash
# Executar todos os testes
python manage.py test

# Executar testes específicos
python manage.py test core.test_api.ClienteAPITest

# Executar com verbosidade
python manage.py test --verbosity=2

# Ver cobertura (se tiver coverage instalado)
coverage run --source='.' manage.py test
coverage report
```

### Testes Incluídos
- ✅ CRUD completo de Clientes
- ✅ CRUD completo de Ordens de Serviço
- ✅ Validações (email duplicado, data conclusão)
- ✅ Filtros e buscas
- ✅ Dashboard e métricas
- ✅ Autenticação

## 📁 Estrutura do Projeto

```
sistema-assistencia/
│
├── assistencia/                 # Projeto Django principal
│   ├── __init__.py
│   ├── settings.py             # Configurações (REST, CORS, i18n)
│   ├── urls.py                 # URLs principais (admin, api, web)
│   ├── wsgi.py                 # WSGI para deploy
│   └── asgi.py                 # ASGI para deploy
│
├── core/                        # App principal
│   ├── migrations/             # Migrações do banco
│   ├── templates/core/         # Templates HTML
│   │   ├── base.html          # Template base com navbar
│   │   ├── dashboard.html     # Dashboard com gráficos
│   │   ├── lista_ordens.html  # Lista de ordens
│   │   ├── lista_clientes.html
│   │   ├── lista_servicos.html
│   │   ├── lista_status.html
│   │   ├── form_ordem.html    # Formulário de ordem
│   │   ├── form_cliente.html
│   │   ├── form_servico.html
│   │   ├── form_status.html
│   │   ├── detalhe_ordem.html # Detalhes da ordem
│   │   ├── confirmar_exclusao.html
│   │   └── pagination.html    # Template reutilizável
│   │
│   ├── models.py               # Modelos (Cliente, Servico, Status, OrdemServico)
│   ├── views.py                # Views web (CBVs)
│   ├── api_views.py            # Views da API REST (ViewSets)
│   ├── forms.py                # Formulários Django
│   ├── serializers.py          # Serializers DRF
│   ├── urls.py                 # URLs web
│   ├── api_urls.py             # URLs da API
│   ├── admin.py                # Admin customizado
│   ├── test_api.py             # Testes da API
│   └── apps.py
│
├── manage.py                    # Comando Django
├── requirements.txt             # Dependências
├── README.md                    # Documentação
└── db.sqlite3                   # Banco de dados (dev)
```

## ⚙️ Configuração Adicional

### Variáveis de Ambiente (Produção)

Crie um arquivo `.env`:

```env
SECRET_KEY=sua-secret-key-super-segura-aqui
DEBUG=False
ALLOWED_HOSTS=seudominio.com,www.seudominio.com
DATABASE_URL=postgres://usuario:senha@host:5432/dbname
```

### Banco de Dados PostgreSQL

Edite `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Deploy em Produção

**Passos Essenciais:**

1. **Configure variáveis de ambiente**
2. **Colete arquivos estáticos:**
```bash
python manage.py collectstatic
```

3. **Use servidor WSGI (Gunicorn):**
```bash
pip install gunicorn
gunicorn assistencia.wsgi:application
```

4. **Configure servidor web (Nginx/Apache)**
5. **Use banco de dados robusto (PostgreSQL)**
6. **Configure HTTPS**
7. **Desabilite DEBUG**

**Plataformas Recomendadas:**
- Render.com (fácil e gratuito)
- Railway
- Heroku
- DigitalOcean
- AWS

## 🤝 Contribuição

Contribuições são muito bem-vindas! Siga estes passos:

1. **Fork o projeto**
2. **Crie uma branch para sua feature:**
```bash
git checkout -b feature/nova-funcionalidade
```

3. **Commit suas mudanças:**
```bash
git commit -m 'Adiciona nova funcionalidade X'
```

4. **Push para a branch:**
```bash
git push origin feature/nova-funcionalidade
```

5. **Abra um Pull Request**

### Padrões de Código
- Siga **PEP 8** para Python
- Use nomes descritivos em português/inglês (consistente)
- Documente funções complexas
- Adicione testes para novas features
- Mantenha commits atômicos e descritivos

## 📝 Roadmap / Próximas Funcionalidades

- [ ] Sistema de notificações por email
- [ ] Anexar fotos/arquivos às ordens
- [ ] Histórico de alterações (audit log)
- [ ] Relatórios em PDF
- [ ] App mobile (React Native)
- [ ] Sistema de permissões por cargo
- [ ] WhatsApp API integration
- [ ] Pagamentos online
- [ ] Agendamento de serviços

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como projeto de portfólio para demonstrar habilidades em:
- Django / Django REST Framework
- Python / POO
- SQL / PostgreSQL
- API RESTful
- HTML/CSS/JavaScript
- Git/GitHub

---

**💡 Dica para Entrevistas:** Este projeto demonstra conhecimento em arquitetura MVC, APIs RESTful, validações, testes automatizados, e boas práticas de desenvolvimento Django.
