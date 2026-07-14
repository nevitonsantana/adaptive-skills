---
name: 🔄 Evolution Cycle
about: Registrar observation, proposal ou review do evolution layer
title: '[EVOLUTION] '
labels: ['category:evolution', 'status:observation']
assignees: ''
---

## 📊 Tipo de Registro

- [ ] **Observation** - Dados coletados de execução real
- [ ] **Proposal** - Sugestão de mudança em skill existente
- [ ] **Review** - Avaliação de proposal
- [ ] **Decision** - Decisão de governança

**Cycle:** # (ex: #3, #4)

**Data:** YYYY-MM-DD

## 🔍 Contexto

### Skill(s) Envolvida(s)
<!-- Liste as skills observadas ou afetadas -->

1. 
2. 

### Piloto / Execução Real
<!-- De qual piloto ou execução esta observation veio? -->

- Piloto: 
- Agente: GPT Codex | Claude Code | Human
- Data da execução: 

## 📈 Observation / Proposal Details

### Se Observation:

**O que foi observado:**
<!-- Descreva o comportamento, padrão ou insight -->

**Evidências:**
- Logs / outputs: 
- Métricas: 
- Contexto específico: 

**Impacto potencial:**
- [ ] Performance
- [ ] Clareza
- [ ] Cobertura
- [ ] Risco
- [ ] Outro: 

### Se Proposal:

**Mudança proposta:**
<!-- Descreva exatamente o que mudar -->

**Justificativa:**
<!-- Por que esta mudança é necessária? -->

**Superfície afetada:**
- [ ] **Protegida** (nome, core moves) - requer governança
- [ ] **Segura** (triggers, optional modules) - pode ser proposta

**Risco de regressão:** Baixo | Médio | Alto

**Skills impactadas:**
1. 
2. 

### Se Review:

**Proposal relacionada:** #

**Avaliação:**
- [ ] ✅ Aprovar
- [ ] ⚠️ Aprovar com ajustes
- [ ] ❌ Rejeitar

**Comentários:**
<!-- Feedback detalhado -->

**Ajustes necessários:**
<!-- Se aplicável -->

## 🎯 Recomendação

<!-- Qual ação recomenda? -->

- [ ] Implementar mudança
- [ ] Coletar mais dados
- [ ] Discutir em governance review
- [ ] Arquivar sem ação

## 📝 Metadados

**Author:** @

**Reviewers:** @, @

**Target Release:** v1.x.0

**Priority:** P0-Critical | P1-High | P2-Medium | P3-Low

---

### ⚠️ Protocolo de Evolução

Este registro segue o [Evolution Layer v1.1](../../evolution/README.md):

**Loop de 8 passos:**
1. Observe ✓ (este registro)
2. Read □
3. Execute □
4. Reflect □
5. Attribute □
6. Propose □
7. Govern □
8. Write □

**Regras:**
- Observations devem vir de execuções reais
- Proposals em superfícies protegidas requerem governance review
- Todas mudanças devem ser atribuídas (authorship)
- Nada de auto-edição sem follow do protocolo
