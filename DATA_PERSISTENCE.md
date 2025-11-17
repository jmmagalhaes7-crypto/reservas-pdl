# Persistência de Dados 📦

## Como Funciona

Os dados são guardados em ficheiros JSON no servidor:
- `data/reservations.json` - Todas as reservas
- `data/feedback.json` - Todo o feedback, sugestões e comentários

## Persistência no Render.com

⚠️ **IMPORTANTE:** No plano grátis do Render, o sistema de ficheiros é **ephemeral** (temporário).

### O que isso significa:
- ✅ Os dados **PERSISTEM** entre deploys normais (quando você faz `git push`)
- ⚠️ Os dados podem ser **PERDIDOS** se:
  - O serviço for parado por muito tempo (mais de 15 minutos de inatividade)
  - Render reiniciar o servidor
  - Houver um problema no servidor

### Soluções Implementadas:

1. **Diretório dedicado** (`data/`) para melhor organização
2. **Inicialização automática** - ficheiros são criados automaticamente se não existirem
3. **Validação de JSON** - se um ficheiro estiver corrompido, é resetado automaticamente
4. **Escrita atómica** - usa ficheiros temporários para evitar corrupção durante escrita
5. **Verificação em cada request** - garante que os ficheiros existem

## Backup Recomendado (CRÍTICO!)

Para garantir que não perde dados, faça backup regular:

### Opção 1: Via Render Dashboard
1. Aceda ao Dashboard do Render
2. Vá em **"Shell"** (terminal)
3. Execute:
   ```bash
   cat data/reservations.json
   cat data/feedback.json
   ```
4. Copie o conteúdo e guarde localmente

### Opção 2: Download via Terminal
1. No Render Shell, execute:
   ```bash
   cat data/reservations.json > /tmp/reservations_backup.json
   cat data/feedback.json > /tmp/feedback_backup.json
   ```
2. Faça download dos ficheiros

### Opção 3: Backup Automático (Recomendado)
Considere adicionar um endpoint de backup ou usar um serviço de base de dados (SQLite, PostgreSQL) para produção.

## Ver Feedback

Para ver o feedback enviado:

1. Aceda ao terminal do Render (via dashboard)
2. Execute: `cat data/feedback.json`
3. Ou faça download do ficheiro

## Para Produção (Recomendado)

Para garantir persistência total, considere:
- **Render Persistent Disk** (plano pago) - mantém dados permanentemente
- **Base de dados externa** (PostgreSQL, MongoDB) - mais robusto
- **Backup automático** para cloud storage (S3, Google Drive)

**Nota:** Os ficheiros JSON não são versionados no Git (estão no `.gitignore`) para evitar conflitos, mas são guardados no servidor.

