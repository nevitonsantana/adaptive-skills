# 🗺️ Roadmap Evolutivo - Adaptive Skills

> **Versão do Roadmap:** 1.2 (Épico 5 — APM packaging — em PR review)
> **Data de Criação:** 2026-04-15
> **Última revisão:** 2026-05-25
> **Horizonte de Planejamento:** Q2-Q3 2026 (Abril-Setembro)
> **Princípio Guia:** "Evolução governada, não auto-edição"
>
> **Nota 2026-05-21:** As Fases 1-4 abaixo refletem o planejamento original de 2026-04-15. A partir de 2026-05-21, o roadmap operacional passa a ser conduzido pelo [plano cross-repo AletheIA + Adaptive Skills](https://github.com/nevitonsantana/AletheIA/blob/main/docs/roadmaps/evolution-backlog-aletheia-adaptive-skills.md) (8 épicos, gates explícitos). Os marcos abaixo permanecem como referência histórica de intenção, com status reconciliados; novas datas e prioridades vêm dos sprints do plano cross-repo.
>
> **Nota 2026-05-25 — execução do plano cross-repo até aqui:**
> - **Sprint 1** (Fronteira + Despoluição): Épico 1 (PR #37, ADR-001/002/003 + ecosystem-map), Épico 2 (PR #38, despoluição Crisis Monitor) — ambos mergeados.
> - **Sprint 2** (Padrões + Empacotamento AletheIA): Épico 3 (PR #39, ADR-004 Caso A para `agentskills.io`), Épico 4 (AletheIA PR #151, tag `v0.1.0-alpha`) — ambos mergeados.
> - **Sprint 3** (Empacotamento Adaptive Skills + Doc AletheIA): Épico 5 — APM packaging do Adaptive Skills mergeado (`apm.yml` no repo; PR #41). Decisões A1/C1/D3 registradas em ADR-005. Épico 6 (doc AletheIA) **entregue** no repo AletheIA (PR #157 — getting-started four-doc; PR #148 — minimal-overlay preset bundle; ecosystem-map + ADR-005 via PR #149). Épico 7 (getting-started Adaptive Skills) também entregue.
>
> **Nota 2026-06-05 — reconciliação cross-repo:** Knowledge Governance Layer (AletheIA ADR-008 + engine ↔ Adaptive Skills ADR-006 + governance skills), Feature Value Governance (AletheIA ADR-009 ↔ skill `feature-value-governance`) e Skill Evolution Validation Layer (ambos os lados) implementados. No Adaptive Skills, posterior: Engineering Skills Hardening Pack (PR #55) + skill-catalog sincronizado com as 30 skills genéricas (PR #57). AletheIA com soft-launch prep em curso (Épico 8, PR #159).

---

## 📌 Visão Estratégica

**Missão:** Construir a biblioteca de micro-habilidades mais confiável e adaptável para agentes de IA, com evolução governada por evidências reais.

**Objetivos Q2-Q3 2026:**
1. Consolidar Efficiency Layer v1.1 como baseline estável
2. Expandir para 10 domínios completos (35+ skills)
3. Estabelecer ciclo contínuo de evolução (6+ cycles/ano)
4. Alcançar 60% de coverage em integration tests
5. Lançar CLI unificada para projeção em múltiplos agentes

---

## 🎯 Fases do Roadmap

### **Fase 1: Consolidação (Abril 2026)**
*Status (reconciliado 2026-05-21): parcialmente entregue; itens não concluídos absorvidos ou aposentados*

| Entrega | Data prevista | Status real (2026-05-21) | Observação |
|---------|------|--------|---------------------|
| Efficiency Layer v1.1 | 2026-04-25 | 🟡 Parcial — skills mapeadas e templates ok; pilotos de validação parados | Validação restante absorvida pelos pilotos sobreviventes (P01/P03/P05) com gate em 28/05 |
| Policy de Superfícies Protegidas | 2026-04-16 | ⚪ Aposentada como item isolado | Conteúdo continua em [`docs/skill-model.md`](docs/skill-model.md) (seção *Protected surfaces*); policy formal será definida no Épico 1 do plano cross-repo (ADR-001/002) |
| Pilotos Ativos (5 skills) | 2026-04-20 | 🔴 2 aposentados (P02, P04), 3 com gate em 28/05 (P01, P03, P05) | Sem evidência de execução em ~5 semanas |
| Evolution Cycle #3 | 2026-04-25 | 🟡 7/10 observations catalogadas | Pipeline parou em 2026-04-15; Cycle #4 reformulado vai reabsorver |
| Domain Pack: Crisis Management | 2026-04-25 | 🟢 Entregue + reposicionamento [#31](https://github.com/nevitonsantana/adaptive-skills/pull/31) | Crisis Monitor passou a "team-owned field evidence, not active backlog" — alinhado ao plano cross-repo |

**Riscos consolidados (2026-05-21):**
- Pilotos podem voltar a estacionar se não houver disciplina de fechamento em 28/05
- Reconciliação narrativa Crisis Monitor (Épico 2 do plano) ainda precisa ser feita em conteúdo canônico (concepts/, contracts/)

---

### **Fase 2: Expansão (Maio 2026) — reescopada em 2026-05-21**
*Status: Reabsorvida pelo plano cross-repo*

Maioria das entregas originalmente planejadas para esta fase **foram absorvidas pelos épicos do plano cross-repo** ou **adiadas explicitamente** após reconciliação:

| Entrega original | Data prevista | Decisão 2026-05-21 |
|---|---|---|
| Domínio Product completo | 2026-05-10 | Adiado — será reavaliado após Épico 1 do plano cross-repo (ADRs de posicionamento) define se "completar domain skeleton" continua sendo prioridade vs. focar em adoption |
| Domínio Governance completo | 2026-05-15 | Adiado — idem; também depende da relação AletheIA ↔ Adaptive Skills ser fixada no ADR-003 |
| Skill Finder Matrix | 2026-05-05 | **Absorvido pelo Épico 7** do plano cross-repo (`docs/getting-started/skill-catalog.md`) |
| Evolution Cycle #4 (forma original) | 2026-05-20 | **Aposentado e reformulado** — ver abaixo |
| Evolution Cycle #5 | 2026-05-31 | Adiado — janela revista após Cycle #4 reformulado terminar (após 2026-06-30) |
| Guide: Telemetry Prática | 2026-05-08 | **Absorvido pelo Épico 7** (entra como seção no overview ou no FAQ do Adaptive Skills) |

#### Evolution Cycle #4 — reformulado (2026-05-21)

| Campo | Conteúdo |
|---|---|
| **Período** | 2026-05-21 → 2026-06-30 (~6 semanas) |
| **Foco** | "Reconciliação narrativa: do Crisis Monitor sandbox ao posicionamento ecossistêmico" |
| **Inputs** | 7 observations existentes em `evolution/observations/` (todas com viés Crisis Monitor); 2 proposals em `evolution/proposals/deferred/`; aprendizados embutidos nos PRs [#31](https://github.com/nevitonsantana/adaptive-skills/pull/31)-[#34](https://github.com/nevitonsantana/adaptive-skills/pull/34) |
| **Meta de evolução** | (1) Reclassificar cada observation como **canônica** (insight agnóstico) ou **exemplo** (Crisis Monitor-específica); (2) Reabrir as 2 proposals deferred com novo critério de agnosticismo; (3) Aprovar ≥1 proposal alinhada com Épicos 1/2 do plano cross-repo |
| **Dependência** | Onda 0 fechada (✅ 2026-05-21) + Épico 1 (ADRs) iniciado |
| **Critério de Done** | Observations reclassificadas + decisão registrada sobre as 2 proposals deferred + ≥1 proposal aprovada |
| **Como não vai falhar de novo** | Escopo amarrado ao plano cross-repo (não é cycle "abstrato"); entregável pequeno e verificável; gate explícito antes de Cycle #5 |

---

### **Fase 3: Maturidade (Junho 2026)**
*Status: Backlog*

| Entrega | Data | Status | Critério de Sucesso |
|---------|------|--------|---------------------|
| Integration Tests Framework | 2026-06-10 | ⚪ 0% | Framework definido e documentado |
| 60% Test Coverage | 2026-06-15 | ⚪ 0% | Todos core moves testados |
| Evolution Cycle #6 | 2026-06-20 | ⚪ 0% | 2+ skills evoluídas |
| Cross-Skill Patterns Catalog | 2026-06-25 | ⚪ 0% | 5+ patterns identificados |
| Failure Cases Documentation | 2026-06-30 | ⚪ 0% | 10+ exemplos de falhas reais |
| Versionamento Semântico por Skill | 2026-06-05 | ⚪ 0% | Política implementada |

**Iniciativas Estratégicas:**
- Identificar patterns reutilizáveis entre 15+ skills
- Documentar falhas reais para aprendizado coletivo
- Implementar política de versionamento (MAJOR.MINOR.PATCH por skill)

**Métricas de Sucesso:**
- Cycle Time médio < 3 dias
- Throughput ≥ 7 tarefas/semana
- Zero bugs em produção

---

### **Fase 4: Industrialização (Julho 2026)**
*Status: Visão*

| Entrega | Data | Status | Critério de Sucesso |
|---------|------|--------|---------------------|
| CLI Unificada | 2026-07-10 | ⚪ 0% | Projeção em Codex/Claude/GPT |
| Skill Bundles por Persona | 2026-07-15 | ⚪ 0% | 3 bundles (Eng, PM, Designer) |
| v2.0 Release | 2026-07-31 | ⚪ 0% | 35 skills + CLI + tests |
| Evolution Cycle #7 | 2026-07-20 | ⚪ 0% | Processo totalmente automatizado |
| Integration com AletheIA | 2026-07-25 | ⚪ 0% | Gates de risco operacionais |

**Visão de Longo Prazo:**
- CLI como interface padrão para instalação em agentes
- Bundles pré-configurados por persona aceleram onboarding
- Integração total com AletheIA para macro-micro orchestration

---

## 📊 Timeline Visual

```
Abril 2026          Maio 2026           Junho 2026          Julho 2026
│                   │                   │                   │
├─ Efficiency v1.1  ├─ Product Domain   ├─ Integration Tests├─ CLI Unificada
├─ Pilotos (5)      ├─ Governance       ├─ 60% Coverage     ├─ Skill Bundles
├─ Cycle #3         ├─ Cycles #4-#5     ├─ Cycle #6         ├─ v2.0 Release
├─ Policy Protected ├─ Skill Finder     ├─ Patterns Catalog ├─ AletheIA Integration
│                   ├─ Telemetry Guide  ├─ Failure Cases    │
│                   │                   ├─ Versionamento    │
```

---

## 🔁 Ciclos de Evolução

### Ciclo Anual (6 cycles/ano)

| Cycle | Período | Foco | Meta de Evolução |
|-------|---------|------|------------------|
| #1 | Jan-Fev | Baseline | 23 skills mapeadas |
| #2 | Mar-Abr | Efficiency Layer | 5 skills validadas |
| #3 | Abr-Mai | Observations | 10+ observations |
| #4 (reformulado) | 2026-05-21 → 2026-06-30 | Reconciliação narrativa (Crisis Monitor → ecossistêmico) | ≥1 proposal aprovada + observations reclassificadas |
| #5 | A definir após Cycle #4 | Implementation | 1+ skill evoluída |
| #6 | Jul-Ago | Automation | Processo automatizado |

### Loop de 8 Passos (v1.1)

```
1. OBSERVE → 2. READ → 3. EXECUTE → 4. REFLECT → 
5. ATTRIBUTE → 6. PROPOSE → 7. GOVERN → 8. WRITE
```

**Superfícies Protegidas:** Nome, Core Moves, Quando-Não-Quando  
**Proposta-Seguras:** Triggers, Módulos Opcionais, Outputs

---

## 🎯 OKRs por Trimestre

### Q2 2026 (Abr-Jun)

**Objective 1:** Consolidar Efficiency Layer como baseline estável
- KR1: 5 skills validadas em pilotos com 80% approval rate
- KR2: Policy de superfícies protegidas aprovada e documentada
- KR3: Zero regressões em core moves após evolution cycles

**Objective 2:** Expandir coverage para 10 domínios
- KR1: Product domain com 5+ skills
- KR2: Governance domain com 5+ skills + AletheIA integration
- KR3: Skill Finder matrix navegável publicada

**Objective 3:** Estabelecer cultura de evolução governada
- KR1: 4 evolution cycles completados
- KR2: 3+ skills evoluídas via processo formal
- KR3: 20+ observations catalogadas

**Objective 4:** Melhorar qualidade e confiabilidade
- KR1: Framework de integration tests definido
- KR2: 60% coverage em core moves
- KR3: 10+ failure cases documentados

### Q3 2026 (Jul-Set)

**Objective 1:** Industrializar distribuição e uso
- KR1: CLI unificada lançada e documentada
- KR2: 3 skill bundles por persona disponíveis
- KR3: 10+ agentes usando skills em produção

**Objective 2:** Aprofundar integração com AletheIA
- KR1: Gates de risco operacionais em 5+ skills
- KR2: Handoffs macro-micro documentados
- KR3: Caso real de integração publicado

**Objective 3:** Escalar evolução contínua
- KR1: 6+ evolution cycles/ano sustentados
- KR2: 50+ skills no registry
- KR3: Processos 80% automatizados

---

## 📈 Métricas de Progresso

### Métricas de Produto

| Métrica | Linha de Base | Meta Q2 | Meta Q3 |
|---------|---------------|---------|---------|
| Skills Validadas | 23 | 35 | 50 |
| Domínios Cobertos | 8 | 10 | 10 |
| Pilotos Ativos | 5 | 10 | 15 |
| Evolution Cycles/Ano | 2 | 6 | 6 |
| Test Coverage | 0% | 60% | 80% |

### Métricas de Processo

| Métrica | Linha de Base | Meta Q2 | Meta Q3 |
|---------|---------------|---------|---------|
| Throughput (tarefas/semana) | 4.5 | 7 | 10 |
| Cycle Time médio | 5.2 dias | 3 dias | 2 dias |
| WIP Limit | 7 | 5 | 5 |
| Taxa de conclusão | 85% | 90% | 95% |
| Bugs em produção | 0 | 0 | 0 |

### Métricas de Impacto

| Métrica | Linha de Base | Meta Q2 | Meta Q3 |
|---------|---------------|---------|---------|
| Agentes usando skills | 2 | 10 | 25 |
| Execuções/mês | ~100 | 1000 | 5000 |
| Approval rate em pilotos | N/A | 80% | 90% |
| Tempo de onboarding | N/A | <1 dia | <4 horas |
| NPS de usuários | N/A | 7+ | 9+ |

---

## ⚠️ Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação | Owner |
|-------|---------------|---------|-----------|-------|
| WIP excedido atrasa entregas | Alta | Médio | Congelar novas entradas, focar em concluir | PO |
| Falta de Domain Experts | Média | Alto | Recrutar contributors, criar programa de onboarding | Core Team |
| Evolution cycles sem proposals | Baixa | Médio | Incentivar observations, criar templates | Evolution Lead |
| Integration tests complexos | Média | Médio | Começar com smoke tests, escalar gradualmente | QA Lead |
| Baixa adoção de skills | Baixa | Alto | Criar bundles, melhorar documentação, casos reais | UX Lead |

---

## 🔄 Revisão e Atualização

**Frequência de Revisão:**
- **Semanal:** Atualizar status de tarefas no Kanban
- **Quinzenal:** Revisar métricas e ajustar prioridades (sprint review)
- **Mensal:** Atualizar roadmap e OKRs (monthly business review)
- **Trimestral:** Revisar visão estratégica e definir próximo trimestre

**Gatilhos de Replanejamento:**
- Mudança significativa no escopo (>30% das tarefas)
- Bloqueio crítico não resolvido em 1 semana
- Nova oportunidade estratégica identificada
- Feedback de usuários indicando mudança de direção

**Processo de Atualização:**
1. Core Team revisa métricas e progresso
2. Identifica desvios e ajusta prioridades
3. Comunica mudanças no PROJECT_KANBAN.md
4. Atualiza ROADMAP_EVOLUTIVO.md com novas datas/metras
5. Registra decisões e lições aprendidas

---

## 📝 Decisões Arquiteturais

### Princípios Guias

1. **Evolução Governada:** Nenhuma skill se auto-edita; todas mudanças passam por proposal + governance review
2. **Superfícies Protegidas:** Nome, Core Moves e Quando-Não-Quando são invariantes; triggers e módulos opcionais são evolutivos
3. **Core+Modules:** 3-5 ações essenciais + add-ons ativados por contexto
4. **Evidence-Based:** Todas evoluções baseadas em observations reais de execução
5. **Integration First:** Skills projetadas para funcionar integradas ou independentes do AletheIA

### Padrões de Design

- **Skill Template:** Estrutura padronizada (SKILL.md) com seções obrigatórias
- **Evolution Templates:** Observation, Proposal, Review com campos definidos
- **Projection Scripts:** Automatizam instalação em diferentes agentes
- **Validation Scripts:** Verificam integridade antes de merge

---

## 🔗 Referências

- [Project Kanban](./PROJECT_KANBAN.md)
- [Evolution Layer v1.1](./evolution/README.md)
- [Skills Registry](./projections/registry.json)
- [Crisis Monitor Case Study](./domain-packs/crisis-management/README.md)
- [AletheIA Macro Layer](https://github.com/nevitonsantana/AletheIA) *(referência externa)*

---

*Este roadmap é um documento vivo, atualizado a cada sprint. Última revisão: 2026-05-21 (reconciliação Onda 0)*
*Próxima revisão programada: ao final do Sprint 1 do plano cross-repo (após Épicos 1 e 2)*
