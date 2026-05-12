# 🚀 Setup do GitHub Project - Adaptive Skills

> **Project URL:** https://github.com/users/nevitonsantana/projects/3/views/1  
> **Versão deste guia:** 1.0.0  
> **Data:** 2026-04-16

---

## ✅ Checklist de Setup (30-45 minutos)

### Passo 1: Instalar e Autenticar GitHub CLI (5 min)

```bash
# macOS
brew install gh

# Linux (Ubuntu/Debian)
sudo apt-get update && sudo apt-get install gh

# Windows (com winget)
winget install --id GitHub.cli

# Autenticar
gh auth login
# Selecione: GitHub.com -> HTTPS -> Login with browser token
```

### Passo 2: Configurar Labels (5-10 min)

```bash
# Navegue até o repositório
cd /path/to/adaptive-skills

# Sincronizar labels a partir do arquivo .github/labels.yml
gh label sync --delete-missing .github/labels.yml

# OU usar script manual se preferir controle total
bash .github/create-labels.sh
```

### Passo 3: Criar Issue Templates (Já feito ✓)

Templates já criados em `.github/ISSUE_TEMPLATE/`:
- ✅ `task-kanban.md` - Tarefas gerais
- ✅ `new-skill.md` - Novas skills
- ✅ `evolution-cycle.md` - Evolution observations/proposals

### Passo 4: Configurar Campos Customizados do Project (10 min)

Acesse: https://github.com/users/nevitonsantana/projects/3/settings/fields

**Campos obrigatórios:**

| Nome | Tipo | Opções |
|------|------|--------|
| `Priority` | Single Select | `P0-Critical`, `P1-High`, `P2-Medium`, `P3-Low` |
| `Executor` | Single Select | `GPT Codex`, `Claude Code`, `Human` |
| `Target Release` | Text | (campo livre para versão) |
| `Link / Context` | Text | (campo livre para URL) |
| `Complexity` | Single Select | `XS`, `S`, `M`, `L`, `XL` |
| `Domain` | Single Select | `engineering`, `design`, `product`, `business`, `quality`, `metrics`, `cross-functional`, `efficiency`, `governance` |

**Como criar cada campo:**
1. Click em "New field"
2. Selecione o tipo (Single Select ou Text)
3. Preencha nome e opções
4. Save

### Passo 5: Configurar Views do Project (5 min)

Acesse: https://github.com/users/nevitonsantana/projects/3/views/1

**View principal: Kanban Board**

1. **Layout:** Board
2. **Group by:** `Status`
3. **Sort by:** `Priority` (descendente)
4. **Filters:**
   ```
   Status is not Done
   ```

**Colunas do Board:**
- Backlog
- Ready
- In Progress
- Pending Handoff
- In Review
- Blocked
- Done

**View secundária: Roadmap (opcional)**

1. Click "New view" -> Timeline
2. Group by: `Domain` ou `Target Release`
3. Adicionar campo customizado "Due Date" se necessário

### Passo 6: Criar Issues Iniciais (10-15 min)

Use os templates criados para adicionar as primeiras issues:

```bash
# Exemplo: Criar issue de task via CLI
gh issue create \
  --title "[TASK] Preencher skeleton do domínio Product" \
  --body-file .github/ISSUE_TEMPLATE/task-kanban.md \
  --label "priority:P1-High,category:skill,domain:product,complexity:M" \
  --project "Adaptive Skills Kanban"

# Ou use a UI do GitHub:
# 1. Acesse https://github.com/nevitonsantana/adaptive-skills/issues/new/choose
# 2. Selecione template apropriado
# 3. Preencha e submit
```

**Issues recomendadas para começar:**

Baseadas no [PROJECT_KANBAN.md](../PROJECT_KANBAN.md):

1. **T01** - Preencher skeleton do domínio Product (P1)
2. **T02** - Preencher skeleton do domínio Governance (P1)
3. **T03** - Criar guia de telemetry prática (P1)
4. **T04** - Criar índice de descoberta (P2)
5. **P01-P07** - Pilotos em andamento (migrar do kanban atual)
6. **B01-B10** - Backlog priorizado

### Passo 7: Migrar Cards Existentes (se aplicável) (10 min)

Se já há issues sem vínculo com o project:

```bash
# Adicionar issue existente ao project
gh project item-add --project-id "PVT_kwDO..." --url "https://github.com/nevitonsantana/adaptive-skills/issues/<numero>"

# Setar campos
gh project item-edit --project-id "PVT_kwDO..." --id "<item-id>" \
  --field "Priority" --single-select-option "P1-High" \
  --field "Status" --single-select-option "In Progress"
```

Para descobrir o `project-id`:
```bash
gh project list --user nevitonsantana
```

---

## 📋 Comandos Úteis do Dia-a-Dia

### Criar Issue e Já Vincular ao Project

```bash
# Criar
ISSUE_NUM=$(gh issue create \
  --title "[TASK] Minha tarefa" \
  --body "Descrição..." \
  --label "priority:P2-Medium,category:task" \
  --repo nevitonsantana/adaptive-skills)

# Extrair número da issue
ISSUE_NUM=$(echo $ISSUE_NUM | grep -o '[0-9]\+')

# Adicionar ao project
gh project item-add --project-id "PVT_kwDO..." --url "https://github.com/nevitonsantana/adaptive-skills/issues/$ISSUE_NUM"
```

### Iniciar Trabalho (Claim)

```bash
# Mover para In Progress
ITEM_ID=$(gh project item-list --project-id "PVT_kwDO..." --limit 100 | grep "issues/$ISSUE_NUM" | awk '{print $1}')

gh project item-edit --project-id "PVT_kwDO..." --id "$ITEM_ID" \
  --field "Status" --single-select-option "In Progress" \
  --field "Executor" --single-select-option "GPT Codex"

# Publicar claim comment
gh issue comment $ISSUE_NUM --body "Execução iniciada.
<!-- executor-lock: GPT Codex | owner: nevitonsantana | started: $(date -Iseconds) -->
- responsável humano: @nevitonsantana
- executor atual: GPT Codex
- objetivo: ..."
```

### Encerrar Trabalho

```bash
# Mover para Done (ou outro status)
gh project item-edit --project-id "PVT_kwDO..." --id "$ITEM_ID" \
  --field "Status" --single-select-option "Done"

# Publicar comentário de encerramento
gh issue comment $ISSUE_NUM --body "Execução encerrada.
<!-- executor-lock: closed | owner: nevitonsantana | finished: $(date -Iseconds) -->
- resultado: ...
- PR / artefato: #..."
```

### Handoff

```bash
# Mover para Pending Handoff
gh project item-edit --project-id "PVT_kwDO..." --id "$ITEM_ID" \
  --field "Status" --single-select-option "Pending Handoff"

# Comentar handoff
gh issue comment $ISSUE_NUM --body "Handoff registrado.
- modelo: same-issue
- de: @nevitonsantana (GPT Codex)
- para: @bruno (Human)
- estado: ...
- próximo passo: ..."
```

---

## 🔗 Links de Referência

- **Project Kanban:** https://github.com/users/nevitonsantana/projects/3/views/1
- **GitHub Project Operations:** [.github/GITHUB_PROJECT_OPERATIONS.md](./GITHUB_PROJECT_OPERATIONS.md)
- **Labels Reference:** [.github/labels-reference.md](./labels-reference.md)
- **Issue Templates:** [.github/ISSUE_TEMPLATE/](./ISSUE_TEMPLATE/)
- **Kanban Atual:** [../PROJECT_KANBAN.md](../PROJECT_KANBAN.md)
- **Roadmap:** [../ROADMAP_EVOLUTIVO.md](../ROADMAP_EVOLUTIVO.md)

---

## ❓ Troubleshooting

### "Project not found"
Verifique se tem permissão de write no repositório e se o project está vinculado.

### "Field not found"
Os nomes dos campos são case-sensitive. Use exatamente como configurado.

### "Label already exists"
Use `gh label sync` em vez de criar manualmente, ou delete antes de recriar.

### Não consigo mover card manualmente
Movimentação manual exige comentário documental imediato. Veja [GITHUB_PROJECT_OPERATIONS.md](./GITHUB_PROJECT_OPERATIONS.md).

---

## 📊 Métricas de Setup Completo

Setup considerado completo quando:

- [ ] Todos labels sincronizados (22+ labels)
- [ ] 3 issue templates disponíveis
- [ ] 6 campos customizados configurados
- [ ] View Kanban com 7 colunas
- [ ] 10+ issues criadas e vinculadas
- [ ] Pelo menos 1 issue em cada coluna (exceto Done)
- [ ] Documentação lida por todos os contributors

---

*Última atualização: 2026-04-16*
