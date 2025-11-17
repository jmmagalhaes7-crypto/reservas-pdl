# Configurar Base de Dados (CRÍTICO para Persistência) 🗄️

## Problema

Render's free tier tem um sistema de ficheiros **ephemeral** - os ficheiros são apagados em cada deploy. Por isso, as reservas desaparecem.

## Solução: Supabase (PostgreSQL Grátis)

Vamos usar Supabase que oferece PostgreSQL grátis e confiável.

## Passo 1: Criar Conta no Supabase

1. Vá para: https://supabase.com
2. Clique em **"Start your project"**
3. Crie conta com GitHub (mais fácil)
4. Crie um novo projeto:
   - **Name:** `reservas-pdl` (ou qualquer nome)
   - **Database Password:** Escolha uma senha forte (guarde-a!)
   - **Region:** Escolha mais próximo (ex: West Europe)
   - Clique **"Create new project"**
5. Aguarde ~2 minutos para o projeto ser criado

## Passo 2: Obter Connection String

1. No dashboard do Supabase, vá em **"Settings"** → **"Database"**
2. Role até **"Connection string"**
3. Escolha **"URI"**
4. Copie a connection string (parece com: `postgresql://postgres:[PASSWORD]@db.xxxxx.supabase.co:5432/postgres`)
5. **IMPORTANTE:** Substitua `[PASSWORD]` pela senha que você criou

## Passo 3: Adicionar ao Render

1. Vá para o dashboard do Render: https://dashboard.render.com
2. Encontre o seu serviço `reservas-pdl`
3. Vá em **"Environment"** (no menu lateral)
4. Clique em **"Add Environment Variable"**
5. Adicione:
   - **Key:** `DATABASE_URL`
   - **Value:** Cole a connection string completa do Supabase
6. Clique **"Save Changes"**
7. Render vai fazer redeploy automaticamente

## Passo 4: Verificar

1. Após o deploy, teste criando uma reserva
2. Faça um novo deploy (push qualquer mudança)
3. Verifique se a reserva ainda existe ✅

## Alternativa: Railway PostgreSQL (Mais Fácil)

Se preferir algo mais simples:

1. Vá para: https://railway.app
2. Crie conta
3. Clique **"New Project"** → **"Provision PostgreSQL"**
4. Clique na base de dados → **"Variables"**
5. Copie o `DATABASE_URL`
6. Adicione ao Render como acima

## Porquê Funciona?

- ✅ Base de dados na cloud (não é apagada)
- ✅ Persiste entre deploys
- ✅ Grátis e confiável
- ✅ Backup automático

**Nota:** O código funciona com ou sem base de dados. Se não houver `DATABASE_URL`, usa ficheiros JSON (mas podem ser apagados no Render free tier).

