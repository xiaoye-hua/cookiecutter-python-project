# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Author

- **Name**: {{ cookiecutter.author_name }}
- **Email**: {{ cookiecutter.author_email }}

## Version

{{ cookiecutter.version }}

## Python Version

This project requires Python {{ cookiecutter.python_version }}

## Cursor Rules

This project includes shared Cursor IDE rules via a git submodule. The rules are located in `.cursor/rules/`.

### Updating Cursor Rules

To update the cursor rules to the latest version from the shared repository:

```bash
git submodule update --remote
git add .cursor/rules
git commit -m "Update cursor rules to latest version"
```

### Adding New Rules

1. Clone the cursor-rules repository: `{{ cookiecutter.cursor_rules_repo }}`
2. Add or modify rules there
3. Commit and push your changes
4. Update this project's submodule using the commands above

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── .cursor/
│   └── rules/          # Shared cursor rules (git submodule)
├── src/                # Source code
├── tests/              # Test files
└── README.md          # This file
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   pytest
   ```

## Development

This project was generated with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and includes automated setup for Cursor IDE rules.
