# Cookiecutter Python Project

A Cookiecutter template for Python projects with automatic Cursor IDE rules integration via Git submodules.

## Features

- Python project structure with src/ and tests/ directories
- Automatic Git repository initialization
- Cursor IDE rules automatically added as a Git submodule
- Makefile for common tasks
- Pre-configured .gitignore for Python projects
- Basic pytest setup

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
│   │   └── rules/                # Placeholder - replaced by submodule
│   ├── src/                      # Source code directory
│   ├── tests/                    # Test directory
│   ├── .gitignore                # Python gitignore
│   ├── Makefile                  # Common tasks
│   ├── README.md                 # Project README
│   └── requirements.txt          # Python dependencies
└── README.md                     # This file
```

## Requirements

- Python 3.7+
- Git
- Cookiecutter (`pip install cookiecutter`)

## License

This template is open source and available under the MIT License.
