# Restricted Context Check — Template

- task_id:
- deliverable_audience:           # internal_review | client_delivery | external_publication | regulator
- agent_id:
- user_id:
- sources_under_check:
  - <pack_id@version>

## Findings

- data_leakage:                   # pass | warn | fail
  notes:
- prompt_injection:               # pass | warn | fail
  notes:
- data_poisoning:                 # pass | warn | fail
  notes:
- permission_mismatch:            # pass | warn | fail
  notes:
- context_contamination:          # pass | warn | fail
  notes:

## Restrictions to apply

- []

## Human review

- human_review_required:
- human_review_reason:
- routed_to:

## Decision

- decision:                       # allow | allow_with_restrictions | refuse
- refusal_reason:

## Audit

- audit_entry_written:
- timestamp:
