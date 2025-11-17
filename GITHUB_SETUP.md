# Como Fazer Push para GitHub 🔐

## Passo 1: Criar Repositório no GitHub

1. Vá para: https://github.com/new
2. **Repository name:** `reservas-pdl`
3. Escolha **Public** ou **Private**
4. **NÃO** marque "Initialize with README"
5. Clique **"Create repository"**

## Passo 2: Criar Personal Access Token

1. Vá para: https://github.com/settings/tokens
2. Clique em **"Generate new token"** → **"Generate new token (classic)"**
3. **Note:** `reservas-pdl-token` (ou qualquer nome)
4. **Expiration:** Escolha duração (ex: 90 dias)
5. **Scopes:** Marque apenas `repo` (isso dá acesso completo aos repositórios)
6. Clique **"Generate token"**
7. **COPIE O TOKEN** (você só verá uma vez!)

## Passo 3: Fazer Push

Depois de criar o repositório e o token, execute:

```bash
cd /Users/joaomariamagalhaes/Documents/Python/mine/reservas_pdl
git push -u origin main
```

Quando pedir:
- **Username:** `jmmagalhaes7-crypto`
- **Password:** Cole o token que você copiou (não sua senha do GitHub!)

---

## Alternativa: Usar SSH (Mais Seguro)

Se preferir usar SSH (não precisa de token toda vez):

1. Gere chave SSH:
```bash
ssh-keygen -t ed25519 -C "jm.magalhaes7@gmail.com"
# Pressione Enter para aceitar localização padrão
# Pressione Enter para senha vazia (ou crie uma)
```

2. Copie a chave pública:
```bash
cat ~/.ssh/id_ed25519.pub
```

3. Adicione no GitHub:
   - Vá para: https://github.com/settings/keys
   - Clique "New SSH key"
   - Cole a chave
   - Salve

4. Mude o remote para SSH:
```bash
cd /Users/joaomariamagalhaes/Documents/Python/mine/reservas_pdl
git remote set-url origin git@github.com:jmmagalhaes7-crypto/reservas-pdl.git
git push -u origin main
```

---

**Recomendação:** Use o Personal Access Token primeiro (mais rápido). Depois pode configurar SSH se quiser.

