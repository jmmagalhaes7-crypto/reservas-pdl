# Deploy no Render.com - Passo a Passo 🚀

## Passo 1: Criar Conta no Render

1. Vá para: https://render.com
2. Clique em **"Get Started for Free"** ou **"Sign Up"**
3. Escolha **"Sign up with GitHub"** (mais fácil!)
4. Autorize Render a acessar seus repositórios

## Passo 2: Criar Web Service

1. No dashboard do Render, clique em **"New +"** → **"Web Service"**
2. Se não aparecer, clique em **"New"** no topo e escolha **"Web Service"**

## Passo 3: Conectar Repositório

1. Render vai mostrar seus repositórios GitHub
2. Procure e selecione: **`jmmagalhaes7-crypto/reservas-pdl`**
3. Clique em **"Connect"**

## Passo 4: Configurar Deploy

Render vai detectar automaticamente que é Flask! Configure assim:

- **Name:** `reservas-pdl` (ou qualquer nome)
- **Region:** Escolha mais próximo (ex: Frankfurt)
- **Branch:** `main` (já deve estar selecionado)
- **Root Directory:** (deixe vazio)
- **Runtime:** `Python 3` (já deve estar selecionado)
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

## Passo 5: Deploy!

1. Clique em **"Create Web Service"**
2. Aguarde ~2-3 minutos enquanto Render:
   - Instala dependências
   - Faz build da aplicação
   - Inicia o servidor
3. Quando aparecer **"Live"** em verde, está pronto!

## Passo 6: Acessar e Compartilhar

1. Render vai criar uma URL tipo: `https://reservas-pdl.onrender.com`
2. Clique na URL para testar
3. **Compartilhe essa URL com toda a família!** 🎉

---

## Notas Importantes

- **Primeira vez:** Pode demorar ~30 segundos para carregar (app "dorme" após 15min)
- **Plano grátis:** 750 horas/mês (mais que suficiente para uso familiar)
- **Atualizações:** Quando você fizer `git push`, Render atualiza automaticamente!

---

## Próximos Passos

Depois de deployar, você pode:
- Personalizar a URL (Render permite mudar)
- Adicionar domínio próprio (se quiser)
- Ver logs em tempo real no dashboard do Render

