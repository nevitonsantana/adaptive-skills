# 🚀 Quick Start - Setup do Kanban

## Pré-requisitos
- GitHub CLI instalado (`gh`)
- Autenticação configurada (`gh auth login`)
- Acesso de escrita ao repositório

## Passo 1: Configurar Labels

```bash
# Importar todos os labels definidos
gh label sync --delete-missing .github/labels.yml
```

Ou manualmente via UI:
1. Acesse https://github.com/nevitonsantana/adaptive-skills/labels
2. Clique em "New label"
3. Crie cada label conforme `.github/labels.yml`

## Passo 2: Criar Issues

```bash
# Executar script de criação automática
./scripts/create-kanban-issues.sh
```

Isso criará 15 issues com:
- 6 HIGH PRIORITY (P0)
- 4 MEDIUM PRIORITY (P1)  
- 5 LOW PRIORITY (P2)

## Passo 3: Adicionar Issues ao Project

```bash
# Para cada issue criada, adicionar ao Project #3
# O script já retorna as URLs das issues criadas

# Exemplo (substitua XXX pelo número da issue):
gh project item-add 3 --owner nevitonsantana --type ISSUE \
  --url "https://github.com/nevitonsantana/adaptive-skills/issues/XXX"
```

## Passo 4: Configurar Views no Project

### Board View (Kanban)
1. Acesse https://github.com/users/nevitonsantana/projects/3/views/1
2. Clique em "+ Add view" → "Board"
3. Configure:
   - **Group by**: Status
   - **Sort**: Priority (custom field ou label)

### Roadmap View
1. Clique em "+ Add view" → "Roadmap"
2. Configure:
   - **Start date**: Created at
   - **End date**: Due date (milestone)
   - **Group by**: Milestone

### Table View
1. Clique em "+ Add view" → "Table"
2. Adicione columns:
   - Title
   - Assignee
   - Labels
   - Milestone
   - Created At

## Passo 5: Configurar Milestones

```bash
# Criar milestones do roadmap
gh milestone create "Fase 1: Foundation" --due-date 2026-05-30
gh milestone create "Fase 2: Tooling" --due-date 2026-07-30
gh milestone create "Fase 3: Scale" --due-date 2026-09-30
gh milestone create "Fase 4: Ecosystem" --due-date 2026-12-15
```

## Passo 6: Organizar Cards

Mova as issues para as colunas apropriadas:

| Issue | Coluna Inicial |
|-------|---------------|
| Tasks P0 (1-6) | TODO |
| Tasks P1 (7-10) | BACKLOG |
| Tasks P2 (11-15) | BACKLOG |

## Verificação Final

```bash
# Listar issues criadas
gh issue list --label "priority: critical"
gh issue list --label "priority: high"
gh issue list --label "priority: medium"

# Verificar labels
gh label list

# Verificar milestones
gh milestone list
```

## Próximos Passos

1. Agendar weekly review (toda sexta, 30 min)
2. Atribuir owners para tasks P0
3. Começar execução da Task #1 (Domain Skeletons)
4. Documentar progresso nas issues

---

**Tempo estimado para setup completo**: 30-45 minutos

**Dúvidas?** Consulte `.github/KANBAN_GUIDE.md` para detalhes completos.
