# 📋 Kanban & Roadmap - Adaptive Skills

> **Project Board**: https://github.com/users/nevitonsantana/projects/3/views/1

Este diretório contém toda a documentação e ferramentas para gestão do projeto Adaptive Skills via Kanban e Roadmap Evolutivo.

---

## 📁 Estrutura de Arquivos

```
.github/
├── README_KANBAN.md       # Este arquivo - visão geral
├── PROJECT_SETUP.md       # Configuração completa (tasks, roadmap, OKRs)
├── KANBAN_GUIDE.md        # Guia de uso do Kanban
├── SETUP_QUICKSTART.md    # Quick start (30-45 min setup)
└── labels.yml             # Definição de labels para importação

scripts/
└── create-kanban-issues.sh # Script de criação automática de issues
```

---

## 🚀 Setup Rápido

Siga o **SETUP_QUICKSTART.md** para configurar em 30-45 minutos:

```bash
# 1. Configurar labels
gh label sync --delete-missing .github/labels.yml

# 2. Criar todas as issues
./scripts/create-kanban-issues.sh

# 3. Criar milestones
gh milestone create "Fase 1: Foundation" --due-date 2026-05-30
gh milestone create "Fase 2: Tooling" --due-date 2026-07-30
gh milestone create "Fase 3: Scale" --due-date 2026-09-30
gh milestone create "Fase 4: Ecosystem" --due-date 2026-12-15

# 4. Adicionar issues ao project (manual ou via script)
```

---

## 🎯 Tasks Prioritizadas

### HIGH PRIORITY (P0) - Próximas 2 semanas
| # | Task | Estimativa | Status |
|---|------|------------|--------|
| 1 | Completar Domain Skeletons Pendentes | 3 dias | 🔴 |
| 2 | Criar Guia de Telemetry Prática | 2 dias | 🔴 |
| 3 | Índice de Descoberta de Skills | 2 dias | 🔴 |
| 4 | Política de Versionamento por Skill | 1 dia | 🔴 |
| 5 | Identificar Cross-Skill Patterns | 3 dias | 🔴 |
| 6 | Exemplos de Falhas Reais | 2 dias | 🔴 |

### MEDIUM PRIORITY (P1) - 2-4 semanas
| # | Task | Estimativa | Status |
|---|------|------------|--------|
| 7 | CLI Unificada para Gestão de Skills | 5 dias | 🟡 |
| 8 | Integration Tests para Skills Críticas | 4 dias | 🟡 |
| 9 | Skill Bundles por Persona | 3 dias | 🟡 |
| 10 | Evolution Layer Automation | 5 dias | 🟡 |

### LOW PRIORITY (P2) - 1-2 meses
| # | Task | Estimativa | Status |
|---|------|------------|--------|
| 11 | Visual Skill Map Interativo | 4 dias | 🟢 |
| 12 | Multi-Agent Coordination Patterns | 5 dias | 🟢 |
| 13 | Skill Performance Benchmarks | 3 dias | 🟢 |
| 14 | Community Contribution Guidelines | 2 dias | 🟢 |
| 15 | Localization Framework | 4 dias | 🟢 |

---

## 🗺️ Roadmap Evolutivo

```
Fase 1: Foundation (Abr-Mai 2026)
├─ Domains skeleton completos
├─ Guia de telemetry
├─ Índice de descoberta
└─ Política de versionamento

Fase 2: Tooling (Jun-Jul 2026)
├─ CLI v1.0
├─ Integration tests
├─ Evolution bot
└─ Skill bundles

Fase 3: Scale (Ago-Set 2026)
├─ Visual skill map
├─ Community contributors
├─ Benchmarks públicos
└─ Multi-agent case study

Fase 4: Ecosystem (Out-Dez 2026)
├─ 50+ skills
├─ API pública
├─ Enterprise cases
└─ v2.0 planning
```

---

## 🏷️ Sistema de Labels

### Prioridade
- `priority: critical` 🔴 - P0, urgência máxima
- `priority: high` 🟠 - P1, próximo sprint
- `priority: medium` 🟡 - P2, próximo mês
- `priority: low` 🟢 - P3, backlog longo prazo

### Categoria
- `category: domain-expansion` - Novos domains/skills
- `category: tooling` - Ferramentas
- `category: documentation` - Docs e guides
- `category: testing` - Tests e QA
- `category: automation` - Bots e automação
- `category: governance` - Políticas
- `category: community` - Contribuições externas
- `category: feature` - Features novas
- `category: research` - Pesquisa
- `category: refactoring` - Refatoração

---

## 📊 Views do Project

### 1. Board View (Kanban Principal)
- **Colunas**: BACKLOG → TODO → IN PROGRESS → REVIEW → DONE → READY FOR RELEASE
- **Group by**: Status
- **Sort**: Priority

### 2. Roadmap View (Timeline)
- **Layout**: Timeline
- **Group by**: Milestone (Fases 1-4)
- **Período**: Abril - Dezembro 2026

### 3. Table View (Gestão)
- **Columns**: Title, Assignee, Labels, Milestone, Created At
- **Filter**: `priority: critical OR priority: high`

### 4. Evolution Tracker (Custom)
- **Filter**: `category: governance OR category: automation`
- **Foco**: Tasks do evolution layer

---

## 🔄 Workflow

### Nova Task
1. Criar issue com template apropriado
2. Aplicar labels (prioridade + categoria)
3. Adicionar ao Project #3
4. Colocar em BACKLOG ou TODO (se P0)

### Execução
1. Mover de TODO → IN PROGRESS
2. Atualizar progresso nos comentários
3. Marcar blockers imediatamente

### Review
1. Mover para REVIEW quando completo
2. Aguardar aprovação (1 reviewer mínimo)
3. Para core moves: validação de governança

### Release
1. Mover para READY FOR RELEASE
2. Incluir na próxima release
3. Após release: mover para DONE

---

## 📅 Cadência de Reviews

| Frequência | Quando | Duração | Participantes |
|------------|--------|---------|---------------|
| Daily | Diário | 15 min | Core team |
| Weekly | Sexta | 30 min | Contributors |
| Bi-weekly | Quinzenal | 1h | All |
| Monthly | Mensal | 1h | Stakeholders |
| Quarterly | Trimestral | 2h | All hands |

---

## 📈 Métricas

### Semanais
- Throughput (issues completadas)
- Cycle time médio
- Issues bloqueadas (> 2 dias)
- WIP em IN PROGRESS

### Mensais
- Velocity (issues/mês)
- Entrega por prioridade
- Progresso nos OKRs
- Technical debt acumulado

---

## 📚 Documentação Relacionada

- **Project Setup Completo**: `.github/PROJECT_SETUP.md`
- **Guia Detalhado do Kanban**: `.github/KANBAN_GUIDE.md`
- **Quick Start**: `.github/SETUP_QUICKSTART.md`
- **Sistema de Evolução**: `/evolution/README.md`
- **Skills Registry**: `/projections/README.md`

---

## 💡 Dicas

1. **Mantenha WIP baixo**: Máximo 5 tasks em IN PROGRESS
2. **Atualize diariamente**: Mova cards no mesmo dia
3. **Documente decisões**: Comente nas issues
4. **Use blockers**: Marque issues travadas imediatamente
5. **Celebre entregas**: Comente aprendizados ao mover para DONE

---

*Última atualização: 2026-04-16*  
*Próxima revisão: 2026-04-23*  
*Responsável: @nevitonsantana*
