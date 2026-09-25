# Skill: Jira Analysis

## Purpose
Understand and parse a Jira work item (requirement or bug) into structured context.

## When to use
At the start of any workflow, when the source is a Jira ticket.

## Expected inputs
- Raw Jira ticket text (description, summary, comments, attachments/filenames).

## Expected outputs
- Objective, work-item type, known facts, assumptions, unknowns, and open questions.

## Important rules
- Do not modify the ticket.
- Preserve the original text for traceability.
- Flag ambiguous or contradictory ticket content as open questions.

## Failure / uncertainty
- If the ticket is missing critical information, mark the workflow as needing clarification.
