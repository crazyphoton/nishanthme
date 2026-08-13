# Handling conflicts in an evolving product

## What I want to say

- Fable auto-reviewed and fixed 6 Linear bugs overnight; 4/5 landed. The interesting failure was the fifth.
- The fifth was a "cannot reproduce": QA hit a deliberate rule (services hidden for new customers) without realizing a setting was on. Fable knew the rule, investigated correctly, then sided with the human and changed the spec anyway.
- The model has no intuition for when a contradiction is a human misunderstanding vs. when the spec is genuinely wrong and should change.
- Desirable behavior depends on context: fully autonomous loop -> "Won't Fix, inconsistent product spec" (forces QA to be precise and override explicitly); human-augmented loop -> surface the conflict and ask why.
- Open question / next big battle: when signals conflict, what guardrails make an agent hold its ground and keep the product coherent?

## Raw notes

- Asked Fable to connect to Linear, review 6 reports, fix overnight. Told it some might already be fixed, so review first.
- 2 already fixed, fixed the other 4, verified. Good night's work.
- Fifth: QA said an "already fixed" bug was only partially fixed, specific case where it didn't work.
- Context: dashboard for appointment bookings over a list of services. Bug was services list not loading in some places (now fixed). Separate setting: some services only for repeat customers; hidden for new customers even when editing their appointment.
- QA didn't realize the setting was on, tested on a new customer, thought the edit-appointment services list was buggy. Correct resolution: cannot reproduce.
- Fable knew the rule: freshly seeded DB, confirmed dropdown reads live catalogue and refetches on open, traced the one diff to that setting, read the deliberate-behavior code comment.
- Then carved an exception to bypass the gate, wrote tests, opened PR, posted confident RCA. Sided with the human over the spec.

## Sources

-

## Material intentionally left out of the finished post

- QA colleague's name (kept anonymous).
- Earlier "four out of five / spec is the authority" framing; replaced by the conflicting-signals / hold-its-ground framing.
- "Founder-locked" phrasing (unclear meaning, dropped).
