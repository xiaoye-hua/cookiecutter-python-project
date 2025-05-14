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

### Managing Cursor Rules

```bash
# Pull latest cursor rules from the remote repository
make update-cursor-rules

# Push local rule changes back to the cursor-rules repository
make push-cursor-rule-edits
```

### Adding New Rules

1. Edit or add rules in `.cursor/rules/`
2. Run `make push-cursor-rule-edits` to push changes
3. Other projects can pull updates with `make update-cursor-rules`

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

This project was generated with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and includes automated setup for Cursor IDE rules via Git submodules.
