# Cursor Rules

This directory contains Cursor IDE rules that will be replaced by a Git submodule during project generation.

## Included Rules

| Rule | Purpose |
|------|---------|
| 010-core-python-style.mdc | Modern Python style (PEP 8, Black, typing, f-strings) |
| 020-docstrings.mdc | NumPy-style docstrings |
| 030-tdd-python.mdc | Test-driven development workflow |
| 040-bug-fix-tdd.mdc | Bug fix protocol with regression tests |
| 100-pytest-autogen.mdc | Test scaffolding for new features |
| 200-domain-specific.mdc | Business rules for domain layer |

## How This Works

When you generate a project using this cookiecutter template:

1. The `post_gen_project.py` hook runs automatically
2. It removes this local copy of the rules
3. It adds your shared cursor-rules repository as a Git submodule
4. Future updates to rules can be pulled via `git submodule update --remote`

## Using These Rules as a Starting Point

To create your own shared cursor-rules repository:

```bash
# Create a new directory for your rules repo
mkdir cursor-rules
cd cursor-rules

# Copy these rules as a starting point
cp -r path/to/this/directory/* .

# Initialize git and push to your repository
git init
git add .
git commit -m "Initial cursor rules"
git remote add origin https://github.com/your-org/cursor-rules.git
git push -u origin main
```

Then update the `cursor_rules_repo` in cookiecutter.json to point to your repository.
