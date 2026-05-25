# 📋 GitHub Project Operations - Adaptive Skills

> **Baseado em:** Crisis Monitor Project Operations  
> **Adaptado para:** Adaptive Skills Library  
> **Versão:** 1.0.0  
> **Data:** 2026-04-16

---

## 🎯 Objetivo

Usar o [GitHub Project](https://github.com/users/nevitonsantana/projects/3) como sistema oficial de:

- roadmap
- backlog
- discovery
- priorização
- execução
- bloqueios
- ownership

**Regra central:**

> Nada relevante deve existir só no chat. Se algo virou tarefa real, iniciativa, discovery, handoff ou mudança de estado, ele precisa deixar rastro em:
> - GitHub Project
> - Issue correspondente
> - docs do repositório, quando aplicável

---

## 🏗️ Modelo Oficial: Pessoa Primeiro

| Conceito | Campo GitHub | Regra |
|----------|--------------|-----|
| **Responsible Human** | `Assignee` nativo | Humano que detém a Issue |
| **Current Executor** | campo `Executor` do Project | `GPT Codex`, `Claude Code` ou `Human` |
| **Status operacional** | `Status` do Project | `Backlog`, `Ready`, `In Progress`, `Pending Handoff`, `In Review`, `Blocked`, `Done` |

### Observações Importantes

- Toda Issue em `In Progress` deve ter **exatamente 1 Assignee efetivo**, mesmo que o GitHub permita mais de um
- O campo `Owner` é **legado** e não é mais a fonte oficial de ownership
- O protocolo é **social com suporte técnico parcial**, não um mutex real de sistema
- `Pending Handoff` representa coordenação interna pendente, não bloqueio externo

---

## 🔒 Regra Oficial de Posse da Issue

Um agente só pode iniciar trabalho se:

1. O `Assignee` já for o humano solicitante, **OU**
2. Houver handoff explícito documentado

**Se a Issue estiver com outro humano responsável:**

- ⛔ **BLOQUEAR POR PADRÃO**
- Não iniciar automaticamente
- Orientar handoff explícito ou subissue

---

## 🔄 Ciclo Obrigatório da Tarefa

### 1. Antes de Começar

```bash
# Checklist pré-execução
□ Localizar a Issue correspondente
□ Se não existir, criar a Issue
□ Garantir vínculo com GitHub Project (Project #3)
□ Verificar campo `Status`
□ Verificar campo `Assignee`
□ Verificar se existe `executor-lock` ativo nos comentários
□ Se livre: setar `Assignee`, `Executor`, mover para `In Progress`
□ Publicar comentário de claim com lock
```

### 2. Durante a Tarefa

- Atualizar `Link / Context` se o documento principal mudar
- Ajustar `Priority` ou `Target Release` **só se houver mudança real de escopo**
- Adicionar comentários documentais na Issue conforme a frente avançar
- Registrar handoff explícito se a próxima camada pertencer a outra frente
- **Não dividir** a mesma Issue informalmente entre duas pessoas

### 3. Ao Encerrar

```bash
# Checklist de encerramento
□ Comentar o resultado na Issue
□ Mover item para status correto:
  - Pending Handoff (se há próximo owner)
  - In Review (se precisa validação)
  - Blocked (se há impedimento)
  - Done (se objetivo total entregue)
□ Manter `Assignee` intacto por padrão
□ Encerrar `executor-lock` com comentário explícito
□ Atualizar docs estruturais quando houver impacto real
```

### ⚠️ Regra de `Done`

Uma Issue **NÃO PODE** ir para `Done` se:

- ❌ Houver handoff pendente
- ❌ Houver subissues abertas
- ❌ O objetivo total ainda não estiver entregue

**Se a fatia atual terminou, mas o objetivo total depende do próximo owner:**

- Usar `Pending Handoff`, **OU**
- Abrir subissue/issue nova conforme modelo escolhido

---

## 👥 Regras para Múltiplas Pessoas e Múltiplos Agentes

### Handoff

Sem estes passos, a posse da Issue **não muda**:

```bash
□ Comentário documental de handoff
□ Troca de `Assignee` quando aplicável
□ Atualização de `Executor`
□ Encerramento do lock anterior
□ Criação de novo lock na nova execução
```

**No modelo `mesma issue`:**

- O `Assignee` **não muda** no momento do handoff
- A Issue vai para `Pending Handoff`
- O próximo owner só assume efetivamente ao executar `start`

### Trabalho Simultâneo

⚠️ **NÃO usar a mesma Issue como unidade paralela informal**

Se duas pessoas precisarem atuar ao mesmo tempo:

- Usar **subissues obrigatórias** para paralelismo real

#### Modelos Aceitos

| Modelo | Quando Usar | Regra |
|--------|-------------|-------|
| **A — Issue pai + subissues** | Paralelismo real | ✅ **PREFERIDO E OBRIGATÓRIO** |
| **B — Handoff sequencial** | Uma fatia termina antes da outra começar | ✅ Aceitável |
| **C — Shared issue explícita** | Caso extremo | ⚠️ Evitar; exige comentário dizendo quem faz qual parte |

### Movimentação Manual no Board

⚠️ **Mover card manualmente sem comentário é violação do protocolo.**

Se alguém mover manualmente:

```bash
□ Comentar na Issue no mesmo momento
□ Registrar:
  - Coluna nova
  - Responsável humano
  - Executor
  - Motivo da movimentação
```

### Fechamento da Issue Pai

Ao fechar uma subissue:

- Se ainda houver irmãs abertas: helper comenta na pai quais continuam abertas
- Se todas estiverem `Done`: helper alerta que a pai **pode** ser fechada
- **Fechamento da pai exige confirmação humana explícita**

---

## 🔐 `executor-lock` como Sinal Secundário

### Ao Iniciar Execução

Postar comentário:

```md
Execução iniciada.
<!-- executor-lock: [executor] | owner: [humano] | started: [ISO timestamp] -->

- responsável humano: ...
- executor atual: ...
- objetivo desta fatia: ...
- contexto canônico: ...
- risco conhecido: ...
```

### Lock Ativo

Um lock é considerado **ativo** se:

1. A Issue está em `In Progress`
2. É o lock mais recente da Issue
3. Não existe comentário posterior de encerramento do lock

### Conflito de Lock

- **Se houver lock ativo de outro owner:** ⛔ BLOQUEAR POR PADRÃO
- **Se houver lock antigo sem encerramento:** Tratar como `stale warning`, exigir handoff ou fechamento explícito

---

## 📝 Regra de Comentários Documentais na Issue

Comentários na Issue fazem parte do ciclo oficial de rastreabilidade.

**Devem registrar:**

- Avanço material de uma fatia
- Decisão local importante
- Validação relevante
- Bloqueio real
- Handoff entre frentes
- Próximo passo recomendado
- Fechamento do lock

**Objetivo:**

- Manter histórico consultável fora do chat
- Tornar a leitura da Issue suficiente para entender o andamento
- Reduzir perda de contexto entre sessões e entre agentes

---

## 📋 Templates de Comentário

### Claim (Início de Execução)

```md
Execução iniciada.
<!-- executor-lock: [executor] | owner: [humano] | started: [ISO timestamp] -->

- responsável humano: @nevitonsantana
- executor atual: GPT Codex
- objetivo desta fatia: Implementar core moves da skill X
- contexto canônico: docs/skill-model.md
- risco conhecido: Nenhum identificado
```

### Handoff

```md
Handoff registrado.

- modelo adotado: same-issue
- responsável anterior: @nevitonsantana
- novo responsável: @bruno
- executor anterior: GPT Codex
- próximo executor: Human
- estado atual: Core moves implementados, módulos opcionais pendentes
- validação já feita: Tests unitários passing
- próximo passo: Revisar triggers e documentação
- subissue criada: #... (se aplicável)
- issue nova criada: #... (se aplicável)
```

### Encerramento do Lock

```md
Execução encerrada.
<!-- executor-lock: closed | owner: [humano] | finished: [ISO timestamp] -->

- resultado: Skill X implementada com 3 core moves + 2 optional modules
- PR / artefato: PR #123
- pendências para handoff ou próxima iteração: Revisão de triggers necessária
```

### Backlog

```md
Item mapeado no backlog.

- motivo da entrada: Nova skill identificada no evolution cycle #3
- contexto principal: docs/efficiency-layer.md
- dependência relevante: AletheIA gates definidos
- próximo gatilho para entrar: Após conclusão dos pilotos atuais
```

### Ready

```md
Item pronto para execução.

- escopo imediato: Criar skill `product-roadmap-prioritization`
- critério de sucesso desta entrada: SKILL.md completo + validation passing
- contexto canônico: templates/skill/SKILL_TEMPLATE.md
- risco conhecido antes de começar: Depende de definição de domain taxonomy
```

### In Progress

```md
Avanço desta etapa:

- fatia trabalhada: Core moves definidos (3/5)
- decisão local: Separar módulo de stakeholder analysis como optional
- validação já feita: Template validation script passing
- próximo passo imediato: Completar optional modules e triggers
```

### In Review

```md
Entrega pronta para revisão.

- o que foi entregue: Skill completa com docs e examples
- validação executada: validate_skills.py + manual review
- ponto que merece atenção na revisão: Triggers podem precisar ajuste fino
- referência de código/doc/PR: PR #123, skills/roadmap-prioritization/SKILL.md
```

### Blocked

```md
Bloqueio registrado.

- bloqueio atual: Aguardando definição de AletheIA integration pattern
- impacto no andamento: Impede implementação de risk gates
- dependência ou frente responsável: Core Team - AletheIA integration
- próximo passo recomendado: Core Team definir pattern até 2026-04-20
```

### Done

```md
Entrega concluída.

- resultado final: Skill `product-roadmap-prioritization` validada e publicada
- validação final: All checks passing, pilot agendado
- decisão ou aprendizado relevante: Pattern de triggers funciona bem para product domain
- efeito no roadmap/fluxo seguinte: Habilita criação de mais 3 skills de product
```

### Pending Handoff

```md
Handoff pendente.

- modelo adotado: same-issue
- fatia concluída nesta etapa: Implementação completa da skill
- próximo owner esperado: @qa-lead
- próximo passo: Validação em piloto real
- subissue / issue nova: #... (se aplicável)
```

---

## ✅ Checklist Mínima para Codex e Claude

### Entrada da Tarefa

```bash
□ Achei a Issue?
□ Garanti vínculo com Project #3?
□ Confirmei `Assignee`?
□ Confirmei `Executor`?
□ Verifiquei lock ativo?
□ Movi para `In Progress`?
□ Publiquei claim com lock?
```

### Durante a Tarefa

```bash
□ `Link / Context` continua correto?
□ Mudou prioridade ou release de verdade?
□ Surgiu handoff para outra frente?
□ Já deixei comentário documental se houve avanço material?
```

### Saída da Tarefa

```bash
□ Comentei o resultado?
□ Deixei `Status` correto?
□ Fechei o lock?
□ Mantive ownership coerente?
□ Atualizei docs estruturais se necessário?
□ Só usei `Done` depois de confirmar que não havia handoff pendente nem subissues abertas?
```

---

## 🛠️ Comandos Operacionais

### Iniciar Trabalho em Issue Existente

```bash
# Para GPT Codex
gh project item-edit --project-id "PVT_kwDO..." --id "<item-id>" \
  --field "Status" --single-select-option "In Progress"

# Publicar claim comment
gh issue comment <numero> --body "Execução iniciada.
<!-- executor-lock: GPT Codex | owner: nevitonsantana | started: $(date -Iseconds) -->
- responsável humano: @nevitonsantana
- executor atual: GPT Codex
- objetivo: ..."

# Para Claude Code (mesmo pattern)
```

### Criar Issue Nova e Já Iniciar

```bash
# Criar issue
gh issue create \
  --title "Título da iniciativa ou tarefa" \
  --body "Descrição completa..." \
  --label "priority:P1,category:skill,domain:product" \
  --project "Adaptive Skills Kanban"

# Vincular ao project e iniciar
gh project item-add --project-id "PVT_kwDO..." --url "https://github.com/nevitonsantana/adaptive-skills/issues/<numero>"

# Setar campos
gh project item-edit --project-id "PVT_kwDO..." --id "<item-id>" \
  --field "Priority" --single-select-option "P1" \
  --field "Target Release" --text "v1.2.0" \
  --field "Status" --single-select-option "In Progress"
```

### Encerrar para Revisão

```bash
gh issue comment <numero> --body "Entrega pronta para revisão.
<!-- executor-lock: closed | owner: nevitonsantana | finished: $(date -Iseconds) -->
- resultado: ...
- PR: #123"

gh project item-edit --project-id "PVT_kwDO..." --id "<item-id>" \
  --field "Status" --single-select-option "In Review"
```

### Encerrar Bloqueado

```bash
gh issue comment <numero> --body "Bloqueio registrado.
- bloqueio: ...
- impacto: ...
- próximo passo: ..."

gh project item-edit --project-id "PVT_kwDO..." --id "<item-id>" \
  --field "Status" --single-select-option "Blocked"
```

### Handoff Explícito

```bash
gh issue comment <numero> --body "Handoff registrado.
- modelo: same-issue
- de: @nevitonsantana (GPT Codex)
- para: @bruno (Human)
- estado: ...
- próximo passo: ..."

gh project item-edit --project-id "PVT_kwDO..." --id "<item-id>" \
  --field "Status" --single-select-option "Pending Handoff"
```

### Encerrar Fatia e Abrir Subissue

```bash
# Criar subissue
gh issue create \
  --title "Fatia restante: ..." \
  --body "Continuação da #<numero>..." \
  --label "priority:P1" \
  --project "Adaptive Skills Kanban"

# Linkar como subissue
gh issue edit <subissue-numero> --milestone "<parent-issue>"

# Comentar na pai
gh issue comment <numero> --body "Fatia atual concluída.
Subissue criada: #<subissue-numero>
Próximo executor: Claude Code"
```

---

## 📦 Regra de PR

Uma PR só deve ser aberta se:

- ✅ Estiver vinculada à Issue correta (`Fixes #...` ou `Related to #...`)
- ✅ O `Assignee` da Issue continuar coerente com quem conduz a tarefa
- ✅ Se houve troca de responsável, o handoff já estiver documentado
- ✅ A Issue já tiver histórico documental suficiente para leitura futura

⚠️ **PR sem vínculo com Issue/Project deve ser exceção justificada.**

---

## 🧭 Árvore de Decisão: Posso Marcar como `Done`?

```text
Issue pode ir para Done?
│
├── Existem subissues abertas?
│   └── SIM → ❌ NÃO (manter em Pending Handoff ou In Review)
│
├── Existe handoff documentado e pendente?
│   └── SIM → ❌ NÃO (usar Pending Handoff)
│
├── O objetivo total da issue está entregue?
│   └── NÃO → ❌ NÃO (completar ou criar subissue)
│
└── Tudo acima OK?
    └── SIM → ✅ Pode ir para Done
```

---

## 🤖 Prompt Operacional Curto para Início de Sessão

### Para GPT Codex

> Antes de executar, localize ou crie a Issue correspondente, confirme `Assignee`, `Executor`, lock ativo e subissues abertas, bloqueie por padrão se a Issue estiver com outro humano responsável, e só então mova o item para `In Progress` com claim documental. Ao encerrar, só use `Done` se o objetivo total tiver acabado; caso contrário, use `Pending Handoff` ou abra subissue/issue nova.

### Para Claude Code

> Antes de executar, localize ou crie a Issue correspondente, confirme `Assignee`, `Executor`, lock ativo e subissues abertas, bloqueie por padrão se a Issue estiver com outro humano responsável, e só então mova o item para `In Progress` com claim documental. Ao encerrar, só use `Done` se o objetivo total tiver acabado; caso contrário, use `Pending Handoff` ou abra subissue/issue nova.

---

## 📊 Campos Customizados do Project #3

| Campo | Tipo | Opções/Formato | Obrigatório |
|-------|------|----------------|-------------|
| **Priority** | Single Select | `P0-Critical`, `P1-High`, `P2-Medium`, `P3-Low` | ✅ |
| **Executor** | Single Select | `GPT Codex`, `Claude Code`, `Human` | ✅ |
| **Target Release** | Text | `v1.x.0` | ❌ |
| **Link / Context** | Text | URL para doc principal | ❌ |
| **Complexity** | Single Select | `XS`, `S`, `M`, `L`, `XL` | ❌ |
| **Domain** | Single Select | `engineering`, `design`, `product`, `business`, `quality`, `metrics`, `cross-functional`, `efficiency`, `governance` | ❌ |

---

## 🔗 Links Úteis

- **Project Kanban:** https://github.com/users/nevitonsantana/projects/3/views/1
- **Issue Template:** `.github/ISSUE_TEMPLATE/task.md`
- **Skill Template:** `templates/skill/SKILL_TEMPLATE.md`
- **Validation Scripts:** `scripts/validate_*.py`
- **Evolution Layer:** `evolution/EVOLUTION_LAYER_V1.1.md`

---

## 📈 Métricas de Adoção

| Métrica | Meta Q2 2026 | Status Atual |
|---------|--------------|--------------|
| Issues com link ao Project | 100% | TBD |
| Issues com executor-lock | 90% | TBD |
| Handoffs documentados | 100% | TBD |
| Comments documentais/tarefa | ≥2 | TBD |
| PRs sem Issue vinculada | 0% | TBD |

---

*Documento baseado nas regras do Crisis Monitor, adaptado para Adaptive Skills. Última atualização: 2026-04-16*
