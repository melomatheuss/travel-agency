# Travel Agency - Teste Técnico Django

Este projeto foi desenvolvido como parte de um **desafio técnico**.  
O objetivo da aplicação é fornecer um catálogo de países (via API REST Countries) e permitir a criação e gerenciamento de **roteiros de viagem (Itinerários)** vinculados a esses países.

A aplicação foi construída utilizando:

- [Django 5](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/) e Docker Compose
- Templates Django para renderização das páginas
- Consumo da API [REST Countries](https://restcountries.com/)

---

## Funcionalidades

- **Países**
  - Importação automática de ~250 países via API externa
  - Catálogo filtrável e pesquisável (`/countries/`)
  - Detalhe de país com seus respectivos itinerários

- **Itinerários**
  - CRUD completo de roteiros de viagem
  - Upload de imagem para cada roteiro
  - Listagem filtrada por país e/ou período
  - Página de detalhe com informações completas

- **Rotas públicas**
  - `/` → Página inicial com estatísticas, países em destaque e roteiros recentes
  - `/countries/` → Lista de países (busca, filtro, ordenação)
  - `/countries/<cca2>/` → Detalhe de país + roteiros relacionados
  - `/itineraries/` → Lista de itinerários (com filtros)
  - `/itineraries/<id>/` → Detalhe do roteiro
  - `/itineraries/add/` → Criação de roteiro
  - `/itineraries/<id>/edit/` → Edição de roteiro

---

## Como executar o projeto

### 1. Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado
- [Docker Compose](https://docs.docker.com/compose/) instalado

### 2. Configuração inicial

Clone este repositório:

```bash
git clone https://github.com/melomatheuss/travel-agency.git
cd travel-agency
```

Crie o arquivo .env a partir do modelo fornecido:

```bash
cp .env.example .env
```

### 3. Subir a aplicação
Construa e inicie os containers:

```bash
docker-compose up --build
```
Em um novo terminal aplique as migrations:
```bash
docker-compose run web python manage.py migrate
```
Sincronize a base de países (API REST Countries):
```bash
docker-compose run web python manage.py sync_countries
```
( Essa operação importa ~250 países para o banco.)

Opcionalmente, crie um superusuário para acessar o Django Admin:

```bash
docker-compose run web python manage.py createsuperuser
```

### 4. Acessar o sistema
Acesse no navegador:

Página inicial → http://localhost:8000/

Admin (se criou superusuário) → http://localhost:8000/admin/