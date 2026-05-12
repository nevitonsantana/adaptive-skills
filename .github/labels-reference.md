# Labels do GitHub Project - Adaptive Skills

## Prioridade

| Label | Descrição | SLA |
|-------|-----------|-----|
| `priority:P0-Critical` | Bloqueia pilotos ou viola princípios de governança | 24-48h |
| `priority:P1-High` | Impacta >5 skills ou habilita novos domínios | 1 semana |
| `priority:P2-Medium` | Melhoria incremental ou documentação | 2 semanas |
| `priority:P3-Low` | Nice-to-have ou otimização | 1 mês |

## Categoria

| Label | Descrição |
|-------|-----------|
| `category:skill` | Criação ou evolução de skill |
| `category:task` | Tarefa geral do projeto |
| `category:evolution` | Evolution cycle (observation/proposal/review) |
| `category:infrastructure` | Scripts, tooling, automação |
| `category:documentation` | Docs, guides, templates |
| `category:pilot` | Piloto de validação |
| `category:governance` | Decisões de governança, policies |

## Domínio

| Label | Descrição |
|-------|-----------|
| `domain:engineering` | Engineering skills |
| `domain:design` | Design skills |
| `domain:product` | Product skills |
| `domain:business` | Business skills |
| `domain:quality` | Quality skills |
| `domain:metrics` | Metrics skills |
| `domain:cross-functional` | Cross-functional skills |
| `domain:efficiency` | Efficiency layer skills |
| `domain:governance` | Governance skills |

## Status

| Label | Descrição |
|-------|-----------|
| `status:proposal` | Aguardando aprovação |
| `status:in-progress` | Em execução |
| `status:review` | Em revisão |
| `status:blocked` | Bloqueado |
| `status:ready` | Pronto para release |
| `status:done` | Concluído |

## Tipo de Executor

| Label | Descrição |
|-------|-----------|
| `executor:gpt-codex` | GPT Codex |
| `executor:claude-code` | Claude Code |
| `executor:human` | Humano |
| `executor:mixed` | Múltiplos executores |

## Complexidade

| Label | Descrição | Estimativa |
|-------|-----------|------------|
| `complexity:XS` | Muito simples | < 4h |
| `complexity:S` | Simples | 4-8h |
| `complexity:M` | Média | 1-3 dias |
| `complexity:L` | Grande | 3-7 dias |
| `complexity:XL` | Muito grande | > 1 semana |

## Release

| Label | Descrição |
|-------|-----------|
| `release:v1.1.0` | Efficiency Layer v1.1 |
| `release:v1.2.0` | Domain expansion |
| `release:v2.0.0` | Major release Q3 2026 |

---

## Como Sincronizar Labels

```bash
# Instalar gh CLI se necessário
brew install gh  # macOS
# ou
sudo apt-get install gh  # Linux

# Autenticar
gh auth login

# Sincronizar labels
gh label sync --delete-missing .github/labels.yml
```

## Script de Criação Manual (alternativo)

```bash
#!/bin/bash

# Prioridade
gh label create "priority:P0-Critical" --color "ff0000" --description "Bloqueia pilotos ou viola governança"
gh label create "priority:P1-High" --color "ff6600" --description "Impacto alto, 1 semana SLA"
gh label create "priority:P2-Medium" --color "ffcc00" --description "Melhoria incremental, 2 semanas"
gh label create "priority:P3-Low" --color "00cc00" --description "Nice-to-have, 1 mês"

# Categoria
gh label create "category:skill" --color "0066ff" --description "Criação ou evolução de skill"
gh label create "category:task" --color "0099ff" --description "Tarefa geral"
gh label create "category:evolution" --color "00ccff" --description "Evolution cycle"
gh label create "category:infrastructure" --color "00ffff" --description "Scripts, tooling"
gh label create "category:documentation" --color "6600ff" --description "Docs, guides"
gh label create "category:pilot" --color "9900ff" --description "Piloto de validação"
gh label create "category:governance" --color "cc00ff" --description "Decisões de governança"

# Domínio
gh label create "domain:engineering" --color "ff99ff"
gh label create "domain:design" --color "ff66cc"
gh label create "domain:product" --color "ff3399"
gh label create "domain:business" --color "ff0066"
gh label create "domain:quality" --color "cc0033"
gh label create "domain:metrics" --color "990000"
gh label create "domain:cross-functional" --color "660000"
gh label create "domain:efficiency" --color "330000"
gh label create "domain:governance" --color "000000"

# Status
gh label create "status:proposal" --color "cccccc"
gh label create "status:in-progress" --color "9999ff"
gh label create "status:review" --color "6666ff"
gh label create "status:blocked" --color "ff3300"
gh label create "status:ready" --color "00ff00"
gh label create "status:done" --color "009900"

# Executor
gh label create "executor:gpt-codex" --color "ffcc99"
gh label create "executor:claude-code" --color "ff9966"
gh label create "executor:human" --color "ff6633"
gh label create "executor:mixed" --color "ff3300"

# Complexidade
gh label create "complexity:XS" --color "00ff00" --description "< 4h"
gh label create "complexity:S" --color "99ff00" --description "4-8h"
gh label create "complexity:M" --color "ffff00" --description "1-3 dias"
gh label create "complexity:L" --color "ff9900" --description "3-7 dias"
gh label create "complexity:XL" --color "ff0000" --description "> 1 semana"

# Release
gh label create "release:v1.1.0" --color "9933ff"
gh label create "release:v1.2.0" --color "6600cc"
gh label create "release:v2.0.0" --color "330099"

echo "✅ Labels criados com sucesso!"
```

---

## Uso Recomendado por Tipo de Issue

### Task Geral
```
Labels mínimos: priority:X, category:task, domain:X
Opcional: complexity:X, executor:X, release:X
```

### Nova Skill
```
Labels mínimos: priority:X, category:skill, domain:X, status:proposal
Opcional: complexity:X, release:X
```

### Evolution Cycle
```
Labels mínimos: priority:X, category:evolution, status:observation|proposal|review
Opcional: domain:X (se afeta domínio específico)
```

### Pilot
```
Labels mínimos: priority:X, category:pilot, domain:X, status:in-progress
Opcional: executor:X
```

---

*Documento de referência para gestão de labels no GitHub Project #3*
