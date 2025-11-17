# Reservas Praia da Luz 🏖️

Sistema de reservas familiar para Praia da Luz com interface inspirada no design da Apple.

## Funcionalidades

- 📅 Calendário visual mensal
- ➕ Criar novas reservas
- 🗑️ Eliminar reservas
- ⚠️ Detecção de conflitos de datas
- 📱 Design responsivo
- 🎨 Interface limpa e moderna

## Instalação Local

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute a aplicação:
```bash
python app.py
```

3. Abra o navegador em `http://localhost:5000`

## Como Hospedar Gratuitamente (Sem Pagar)

### Opção 1: Render (Recomendado - Mais Fácil) ⭐

**Vantagens:** Grátis, fácil de usar, suporta Flask automaticamente

1. Crie uma conta em [render.com](https://render.com) (grátis)
2. Conecte seu repositório GitHub
3. Crie um novo "Web Service"
4. Render detecta automaticamente Flask
5. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Deploy automático!

**Limitações do plano grátis:**
- Aplicação "dorme" após 15 minutos de inatividade (primeira requisição pode demorar ~30s)
- 750 horas grátis por mês (suficiente para uso familiar)
- Sem limite de usuários

### Opção 2: Railway

**Vantagens:** Não "dorme", muito rápido

1. Crie conta em [railway.app](https://railway.app)
2. Conecte GitHub
3. Crie novo projeto
4. Railway detecta Flask automaticamente
5. Deploy!

**Limitações:**
- $5 grátis por mês (suficiente para uso familiar)
- Aplicação não dorme

### Opção 3: PythonAnywhere

**Vantagens:** Especializado em Python, muito estável

1. Crie conta grátis em [pythonanywhere.com](https://www.pythonanywhere.com)
2. Vá em "Web" → "Add a new web app"
3. Escolha Flask
4. Faça upload dos arquivos via interface web
5. Configure o WSGI file

**Limitações:**
- Apenas 1 aplicação web grátis
- Domínio: `seuusuario.pythonanywhere.com`
- Não dorme, mas pode ter limitações de tráfego

### Opção 4: Fly.io

**Vantagens:** Muito rápido, boa performance

1. Instale Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Crie conta: `fly auth signup`
3. No diretório do projeto: `fly launch`
4. Siga as instruções

**Limitações:**
- 3 VMs grátis compartilhadas
- Suficiente para uso familiar

### Opção 5: Vercel (Com Adaptação)

**Nota:** Vercel é otimizado para frontend, mas pode funcionar com Flask usando serverless functions.

## Recomendação Final

**Para uso familiar, recomendo Render ou Railway:**

- **Render:** Se não se importar com o "sleep" (primeira requisição pode demorar)
- **Railway:** Se quiser sempre rápido (mas tem limite de $5/mês)

Ambos são muito fáceis de configurar e totalmente grátis para uso familiar!

## Estrutura de Arquivos

```
reservas_pdl/
├── app.py                 # Aplicação Flask
├── templates/
│   └── index.html         # Interface web
├── reservations.json      # Base de dados (criado automaticamente)
├── requirements.txt       # Dependências Python
└── README.md             # Este ficheiro
```

## Notas

- Os dados são guardados em `reservations.json` (criado automaticamente)
- Para backup, faça download periódico deste ficheiro
- O sistema detecta automaticamente conflitos de datas

## Suporte

Para questões ou problemas, verifique os logs da aplicação no serviço de hosting escolhido.

