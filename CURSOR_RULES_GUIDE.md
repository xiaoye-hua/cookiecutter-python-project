# Cursor Rules Quick Reference

## Rule Catalog Overview

| File | ID | Scope | Mode | Purpose |
|------|-----|-------|------|---------|
| **010-core-python-style.mdc** | *style* | `src/**/*.py` | Always | PEP 8, Black, typing, f-strings |
| **020-docstrings.mdc** | *docs* | `src/**/*.py` | Auto | NumPy-style docstrings |
| **030-tdd-python.mdc** | *tdd* | `src/**/*.py` | Auto | Test-first workflow |
| **040-bug-fix-tdd.mdc** | *bug-fix* | `src/**/*.py` | Trigger | Bug regression tests |
| **100-pytest-autogen.mdc** | *scaffold* | *(none)* | Trigger | Test scaffolding |
| **200-domain-specific.mdc** | *domain* | `domain/**/*.py` | Auto | Business invariants |

## How Rules Work Together

### Always Active (Foundation)
- **010**: Ensures consistent Python style across all files
- Applies Black formatting, type hints, logging, f-strings

### Auto-Attached by File Pattern
- **020**: Adds docstrings when editing any Python file
- **030**: Enforces TDD when editing src/ files
- **200**: Applies business rules in domain layer

### Triggered by Request Type
- **040**: Activates on bug-fix requests
- **100**: Suggests test scaffolds for new features

## Typical Workflow

1. **New Feature Request**
   - Rule 100 triggers → suggests test scaffold
   - Rule 030 enforces → write failing test first
   - Rule 010 applies → maintain style standards
   - Rule 020 applies → add proper docstrings

2. **Bug Fix Request**
   - Rule 040 triggers → create regression test
   - Follow bug-fix TDD protocol
   - Document root cause

3. **Domain Layer Work**
   - Rule 200 activates → enforce business rules
   - Use Decimal for money, UoW for writes
   - Maintain 1-to-1 Customer-Segment relation

## Updating Rules

```bash
# Pull latest rules from central repository
git submodule update --remote

# Commit the update
git add .cursor/rules
git commit -m "Update cursor rules to latest"
```

## Creating New Rules

1. Clone the cursor-rules repository
2. Add new .mdc file with proper front-matter
3. Follow naming convention: `XXX-description.mdc`
4. Test in a project before pushing
5. Update all projects via submodule update
