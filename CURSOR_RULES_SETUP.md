# Setting Up Your Cursor Rules Repository

This guide explains how to create and manage a cursor rules repository for use with this cookiecutter template.

## Creating Your Cursor Rules Repository

1. **Create the repository structure**:
   ```bash
   mkdir cursor-rules
   cd cursor-rules
   mkdir -p .cursor/rules
   ```

2. **Add your cursor rule files**:
   Place your `.mdc` files in the `.cursor/rules/` directory. For example:
   - `.cursor/rules/010-core-python-style.mdc`
   - `.cursor/rules/020-docstrings.mdc`
   - `.cursor/rules/030-tdd-python.mdc`

3. **Initialize Git and push**:
   ```bash
   git init
   git add .
   git commit -m "Initial cursor rules"
   git remote add origin https://github.com/your-org/cursor-rules.git
   git push -u origin main
   ```

## Example Rule Structure

Here's an example of what your cursor rules repository should look like:

```
cursor-rules/
└── .cursor/
    └── rules/
        ├── 010-core-python-style.mdc
        ├── 020-docstrings.mdc
        ├── 030-tdd-python.mdc
        ├── 040-bug-fix-tdd.mdc
        ├── 100-pytest-autogen.mdc
        └── 200-domain-specific.mdc
```

## Using with Cookiecutter

1. Update the `cookiecutter.json` file in this template with your cursor rules repository URL
2. When generating projects, they will automatically include your rules as a submodule
3. Use the provided Makefile commands to manage rules:
   - `make update-cursor-rules` - Pull latest rules
   - `make push-cursor-rule-edits` - Push changes back

## Best Practices

- Use consistent numbering for rule files (010, 020, etc.) to control load order
- Include clear descriptions in each rule file
- Test rules thoroughly before pushing to the repository
- Use semantic commit messages when updating rules
- Consider using branches for testing new rules before merging to main
