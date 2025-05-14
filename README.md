# Cookiecutter Python Project

A Cookiecutter template for Python projects with automatic Cursor IDE rules integration via Git submodules.

## Features

- Python project structure with src/ and tests/ directories
- Automatic Git repository initialization
- Cursor IDE rules automatically added as a Git submodule
- Makefile with cursor rule management commands
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
- `cursor_rules_repo`: URL of your cursor rules repository

## Cursor Rules (Two-Repo Model)

This template uses the two-repo model where cursor rules are:

1. Stored in a separate repository (e.g., `github.com/your-org/cursor-rules`)
2. Added to projects as a Git submodule at `.cursor/rules`
3. Easily updated across all projects

### Benefits

- ✅ Update rules from any project and push changes back
- ✅ Pull latest rule changes into existing projects
- ✅ Keep rules synced across many codebases
- ✅ Independent versioning of rules

### Managing Cursor Rules

After generating a project, use these commands:

```bash
# Pull latest cursor rules from remote
make update-cursor-rules

# Push local rule changes back to cursor-rules repo
make push-cursor-rule-edits
```

## Setting Up Your Cursor Rules Repository

1. Create a new repository for your cursor rules:
   ```bash
   mkdir cursor-rules
   cd cursor-rules
   mkdir -p .cursor/rules
   # Add your .mdc files to .cursor/rules/
   git init
   git add .
   git commit -m "Initial cursor rules"
   git remote add origin https://github.com/your-org/cursor-rules.git
   git push -u origin main
   ```

2. Update `cookiecutter.json` with your cursor rules repo URL

3. Generate projects that automatically include your rules as a submodule

## Post-Generation Hook

This template includes a post-generation hook that automatically:

1. Initializes a Git repository in your new project
2. Adds the cursor-rules repository as a Git submodule at `.cursor/rules`
3. Commits the initial project structure

## Structure

```
cookiecutter-python-project/
├── cookiecutter.json              # Template configuration
├── hooks/
│   └── post_gen_project.py       # Adds cursor rules submodule
├── {{cookiecutter.project_slug}}/
│   ├── .cursor/
│   │   └── rules/                # Git submodule (empty in template)
│   ├── src/                      # Source code directory
│   ├── tests/                    # Test directory
│   ├── .gitignore                # Python gitignore
│   ├── Makefile                  # Includes cursor rule commands
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
