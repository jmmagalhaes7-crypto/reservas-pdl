# Persistência de Dados 📦

## Como Funciona

Os dados são guardados em ficheiros JSON no servidor:
- `reservations.json` - Todas as reservas
- `feedback.json` - Todo o feedback, sugestões e comentários

## Persistência no Render.com

✅ **Os dados PERSISTEM entre deploys!**

- Render mantém os ficheiros no sistema de ficheiros do servidor
- Mesmo quando você faz `git push` e Render faz redeploy, os dados ficam guardados
- Os ficheiros JSON são criados automaticamente na primeira utilização

## Backup Recomendado

Para garantir que não perde dados:

1. **Aceda ao Dashboard do Render**
2. Vá em **"Shell"** ou **"Logs"**
3. Faça download periódico dos ficheiros:
   - `reservations.json`
   - `feedback.json`

Ou use o terminal do Render para copiar os ficheiros.

## Ver Feedback

Para ver o feedback enviado:

1. Aceda ao terminal do Render (via dashboard)
2. Execute: `cat feedback.json`
3. Ou faça download do ficheiro

**Nota:** Os ficheiros JSON não são versionados no Git (estão no `.gitignore`) para evitar conflitos, mas são guardados no servidor.

