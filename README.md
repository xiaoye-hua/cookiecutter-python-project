# Cookiecutter Python Project

A Cookiecutter template for Python projects with automatic Cursor IDE rules integration via Git submodules.

## Features

- Python project structure with src/ and tests/ directories
- Automatic Git repository initialization
- Cursor IDE rules automatically added as a Git submodule
- Makefile for common tasks
- Pre-configured .gitignore for Python projects
- Basic pytest setup
- Complete set of TDD-focused Cursor rules

## Usage

```bash
cookiecutter /Users/hua/Documents/codes_private/cookiecutter-python-project
```

Or if you host this on GitHub:

```bash
cookiecutter https://github.com/your-username/cookiecutter-python-project
```

## Variables

The template will prompt you for the following variables:

- `project_name`: The name of your project (e.g., "My Awesome Project")
- `project_slug`: The directory name (auto-generated from project_name)
- `project_short_description`: A brief description of your project
- `author_name`: Your name
- `author_email`: Your email address
- `version`: Initial version (default: 0.1.0)
- `python_version`: Required Python version (default: 3.11)
- `cursor_rules_repo`: URL of your shared Cursor rules repository

## Available Cursor Rules

The example-cursor-rules/ directory contains a complete set of cursor rules:

| Rule File | Purpose | Auto-Attach | Scope |
|-----------|---------|-------------|-------|
| 010-core-python-style.mdc | PEP 8, Black, typing, f-strings | Always applied | All Python files |
| 020-docstrings.mdc | NumPy-style docstrings | Auto-attach | src/**/*.py |
| 030-tdd-python.mdc | Test-driven development | Auto-attach | src/**/*.py |
| 040-bug-fix-tdd.mdc | Bug fix protocol | Agent request trigger | src/**/*.py |
| 100-pytest-autogen.mdc | Test scaffolding | Agent request trigger | New features |
| 200-domain-specific.mdc | Business rules | Auto-attach | domain/**/*.py |

📚 Complete cursor rules are included in the template: `{{cookiecutter.project_slug}}/.cursor/rules/`

## Post-Generation Hook

This template includes a post-generation hook that automatically:

1. Initializes a Git repository in your new project
2. Adds the cursor-rules repository as a Git submodule at `.cursor/rules`
3. Commits the initial project structure

## Cursor Rules Workflow

### For New Projects

1. Use this cookiecutter template to create a new project
2. The cursor rules will be automatically added as a submodule
3. Cursor IDE will immediately use these shared rules

### Updating Rules in an Existing Project

```bash
# Update to latest cursor rules
make update-rules

# Or manually:
git submodule update --remote
git add .cursor/rules
git commit -m "Update cursor rules"
```

### Adding New Rules

1. Clone your cursor-rules repository
2. Add or modify rule files
3. Commit and push changes
4. Update the submodule in your projects using the commands above

## Structure

```
cookiecutter-python-project/
├── cookiecutter.json              # Template configuration
├── hooks/
│   └── post_gen_project.py       # Automatically adds cursor rules submodule
├── {{cookiecutter.project_slug}}/
│   ├── .cursor/
│   │   └── rules/                # Cursor rules (will be replaced by submodule)
│   │       ├── 010-core-python-style.mdc
│   │       ├── 020-docstrings.mdc
│   │       ├── 030-tdd-python.mdc
│   │       ├── 040-bug-fix-tdd.mdc
│   │       ├── 100-pytest-autogen.mdc
│   │       ├── 200-domain-specific.mdc
│   │       └── .gitkeep
│   ├── src/                      # Source code directory
│   ├── tests/                    # Test directory
│   │   ├── regressions/          # Bug regression tests
│   │   └── _bug_template.py      # Template for bug fixes
│   ├── .gitignore                # Python gitignore
│   ├── Makefile                  # Common tasks
│   ├── README.md                 # Project README
│   └── requirements.txt          # Python dependencies
└── README.md                     # This file
```

## Rule Loading Order

Cursor loads rules in alphabetical order by filename. The numbering scheme ensures:

1. **010-020**: Core style rules (always active)
2. **030-040**: TDD workflow rules (context-sensitive)
3. **100+**: Feature scaffolding and domain-specific rules

This ordering allows foundational rules to apply first, with more specific rules layering on top.

## Requirements

- Python 3.7+
- Git
- Cookiecutter (`pip install cookiecutter`)

## Getting Started with Cursor Rules

1. The template already includes a complete set of cursor rules
2. To use them as a shared repository:
   ```bash
   # Copy the rules to a new repository
   cp -r {{cookiecutter.project_slug}}/.cursor/rules/* /path/to/cursor-rules/.cursor/rules/
   cd /path/to/cursor-rules
   git init
   git add .
   git commit -m "Initial cursor rules"
   git remote add origin https://github.com/your-org/cursor-rules.git
   git push -u origin main
   ```

3. Update the cookiecutter.json file to point to your repository

4. The post-generation hook will automatically replace the local rules with the submodule

## License

This template is open source and available under the MIT License.
