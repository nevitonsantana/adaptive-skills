# 📋 Adaptive Skills - Kanban Board Setup

## Link do Projeto GitHub
**https://github.com/users/nevitonsantana/projects/3/views/1**

---

## 🎯 Resumo Executivo

Este documento descreve a estrutura completa do Kanban e Roadmap Evolutivo para o projeto **Adaptive Skills**. O quadro foi projetado para suportar o sistema de evolução governada das skills, com rastreabilidade completa desde observações até releases.

---

## 📊 Estrutura do Kanban

### Colunas Principais

| Coluna | Descrição | WIP Limit |
|--------|-----------|-----------|
| **BACKLOG** | Tarefas identificadas, não priorizadas | ∞ |
| **TODO (Next 2 weeks)** | Priorizadas para curto prazo | 10 |
| **IN PROGRESS** | Em execução ativa | 5 |
| **REVIEW** | Aguardando validação/governança | 5 |
| **DONE** | Concluídas e validadas | ∞ |
| **READY FOR RELEASE** | Prontas para próxima versão | ∞ |

---

## 🎯 Tasks Criadas (15 total)

### 🔴 HIGH PRIORITY (P0) - 6 tasks
1. **Completar Domain Skeletons Pendentes** - 3 dias
2. **Criar Guia de Telemetry Prática** - 2 dias
3. **Índice de Descoberta de Skills** - 2 dias
4. **Política de Versionamento por Skill** - 1 dia
5. **Identificar Cross-Skill Patterns** - 3 dias
6. **Exemplos de Falhas Reais (Failure Cases)** - 2 dias

### 🟡 MEDIUM PRIORITY (P1) - 4 tasks
7. **CLI Unificada para Gestão de Skills** - 5 dias
8. **Integration Tests para Skills Críticas** - 4 dias
9. **Skill Bundles por Persona** - 3 dias
10. **Evolution Layer Automation** - 5 dias

### 🟢 LOW PRIORITY (P2) - 5 tasks
11. **Visual Skill Map Interativo** - 4 dias
12. **Multi-Agent Coordination Patterns** - 5 dias
13. **Skill Performance Benchmarks** - 3 dias
14. **Community Contribution Guidelines** - 2 dias
15. **Localization Framework** - 4 dias

---

## 🗺️ Roadmap Evolutivo

### Fase 1: Foundation Solidification (Abril - Maio 2026)
- ✅ Domains skeleton completos
- ✅ Guia de telemetry publicado
- ✅ Índice de descoberta lançado
- ✅ Política de versionamento em vigor

### Fase 2: Tooling & Automation (Junho - Julho 2026)
- CLI v1.0 lançada
- Integration tests em produção
- Evolution bot ativo
- Skill bundles por persona disponíveis

### Fase 3: Scale & Community (Agosto - Setembro 2026)
- Visual skill map lançado
- Primeiros contributors externos
- Benchmarks públicos
- Multi-agent case study publicado

### Fase 4: Ecosystem Expansion (Outubro - Dezembro 2026)
- 50+ skills no registry
- API pública beta
- Enterprise case studies
- v2.0 release planning

---

## 🏷️ Sistema de Labels

### Prioridade
- `priority: critical` (P0 - urgência máxima)
- `priority: high` (P1 - próximo sprint)
- `priority: medium` (P2 - próximo mês)
- `priority: low` (P3 - backlog longo prazo)

### Categoria
- `category: domain-expansion`
- `category: tooling`
- `category: documentation`
- `category: testing`
- `category: automation`
- `category: governance`
- `category: community`
- `category: feature`
- `category: research`
- `category: refactoring`

### Tipo
- `type: feature`
- `type: bug`
- `type: enhancement`
- `type: tech-debt`
- `type: research`

### Status
- `status: blocked`
- `status: needs-review`
- `status: ready-for-release`

---

## 📝 Como Popular o Kanban

### Opção 1: Script Automático (Recomendado)

```bash
# Autentique-se no GitHub CLI
gh auth login

# Execute o script de criação
./scripts/create-kanban-issues.sh

# Adicione as issues ao projeto
gh project item-add 3 --owner nevitonsantana --type ISSUE \
  --url "https://github.com/nevitonsantana/adaptive-skills/issues/XXX"
```

### Opção 2: Manual

1. Acesse https://github.com/nevitonsantana/adaptive-skills/issues
2. Clique em "New issue"
3. Copie título e descrição do arquivo `.github/PROJECT_SETUP.md`
4. Aplique os labels correspondentes
5. Após criar, adicione ao Project #3

---

## 🔧 Configuração das Views

### Board View (Kanban Principal)
- **Group by**: Status (colunas)
- **Filter**: None
- **Sort**: Priority (critical → high → medium → low)

### Roadmap View (Timeline)
- **Layout**: Timeline
- **Start date field**: Created at
- **Due date field**: Milestone due date
- **Group by**: Milestone

### Table View (Gestão)
- **Columns**: Title, Assignee, Labels, Milestone, Created At
- **Filter**: `priority: critical OR priority: high`
- **Sort**: Created At (descending)

### Evolution Tracker (Custom)
- **Filter**: `label:"category: governance" OR label:"category: automation"`
- **Group by**: Milestone
- **Sort**: Priority

---

## 📊 Métricas de Acompanhamento

### Semanais (toda sexta-feira)
- [ ] Issues em IN PROGRESS
- [ ] Issues bloqueadas (> 2 dias)
- [ ] Throughput da semana
- [ ] Cycle time médio

### Mensais
- [ ] Velocity (issues completadas/mês)
- [ ] Taxa de entrega por prioridade
- [ ] Acumulado de technical debt
- [ ] Progresso nos OKRs do roadmap

### Por Sprint (2 semanas)
- [ ] Commitment vs entregue
- [ ] Carryover de tarefas
- [ ] Bloqueios recorrentes
- [ ] Lições aprendidas

---

## 🔄 Workflow de Governança

### Para Tasks de Evolution Layer

1. **Proposal criada** → Move para REVIEW
2. **Review aprovado** → Move para IN PROGRESS
3. **Implementação completa** → Move para READY FOR RELEASE
4. **Release publicada** → Move para DONE

### Critérios de Review

- [ ] Documentação atualizada
- [ ] Tests passando
- [ ] Changelog atualizado
- [ ] Aprovação de 1 reviewer mínimo
- [ ] Validação de compatibilidade (para changes em core moves)

---

## 📅 Review Cadence

| Frequência | Participantes | Foco | Duração |
|------------|---------------|------|---------|
| **Daily** | Core team | Blockers, IN PROGRESS | 15 min |
| **Weekly** | Contributors | Priorização, TODO → IN PROGRESS | 30 min |
| **Bi-weekly** | All | Retrospective, planejamento sprint | 1h |
| **Monthly** | Stakeholders | Roadmap review, OKRs | 1h |
| **Quarterly** | All hands | Estratégia, próximo quarter | 2h |

---

## 🚀 Próximos Passos Imediatos

1. **Hoje**:
   - [ ] Executar `./scripts/create-kanban-issues.sh`
   - [ ] Configurar labels no repositório
   - [ ] Adicionar todas as issues ao Project #3

2. **Esta semana**:
   - [ ] Mover 6 tasks P0 para TODO
   - [ ] Atribuir owners para cada task
   - [ ] Configurar view de Roadmap
   - [ ] Agendar weekly review

3. **Próximas 2 semanas**:
   - [ ] Completar pelo menos 3 tasks P0
   - [ ] Estabelecer ritmo de reviews
   - [ ] Documentar primeiras learnings

---

## 📚 Recursos Relacionados

- **Documentação Principal**: `/docs/README.md`
- **Sistema de Evolução**: `/evolution/README.md`
- **Templates**: `/templates/`
- **Scripts**: `/scripts/`
- **Project Setup**: `/.github/PROJECT_SETUP.md`

---

## 💡 Dicas de Uso

1. **Mantenha WIP baixo**: Máximo 5 tasks em IN PROGRESS simultâneas
2. **Atualize diariamente**: Mova cards assim que o status mudar
3. **Use blockers**: Marque issues bloqueadas imediatamente
4. **Documente decisões**: Comente nas issues com contexto de decisões
5. **Celebre entregas**: Mova para DONE com comentários de aprendizado

---

*Última atualização: 2026-04-16*
*Responsável: @nevitonsantana*
*Próxima revisão: 2026-04-23*
