# Cursor Rules Guide - Two-Repo Model

## Overview

This template uses the two-repo model where cursor rules are:
- Stored in a separate repository
- Added to projects as a Git submodule
- Updated independently from project code

## Setup

### 1. Create Your Cursor Rules Repository

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

### 2. Configure Cookiecutter

Update `cookiecutter.json` with your cursor rules repository URL:

```json
{
    "cursor_rules_repo": "https://github.com/your-org/cursor-rules.git"
}
```

### 3. Generate Projects

Projects will automatically include your cursor rules as a submodule.

## Managing Rules

### From Any Project

#### Update to Latest Rules
```bash
make update-cursor-rules
```

This command:
1. Fetches the latest rules from the remote repository
2. Updates the submodule reference
3. Commits the change

#### Push Rule Changes
```bash
make push-cursor-rule-edits
```

This command:
1. Commits local rule changes
2. Pushes to the cursor-rules repository
3. Updates the submodule reference in the project

### Manual Commands

If you prefer manual Git commands:

```bash
# Update rules
git submodule update --remote --merge
git add .cursor/rules
git commit -m "Update cursor rules"

# Push changes
cd .cursor/rules
git add .
git commit -m "Update rules"
git push origin main
cd ../..
git add .cursor/rules
git commit -m "Track updated cursor rule pointer"
```

## Typical Workflow

1. **Edit rules in any project**
   ```bash
   cd my-project/.cursor/rules
   # Edit .mdc files
   ```

2. **Push changes back**
   ```bash
   make push-cursor-rule-edits
   ```

3. **Update other projects**
   ```bash
   cd other-project
   make update-cursor-rules
   ```

## Benefits

✅ **Centralized Management**: One source of truth for all rules  
✅ **Easy Updates**: Pull latest rules with one command  
✅ **Bidirectional Sync**: Push changes from any project  
✅ **Version Control**: Full Git history for rule changes  
✅ **Independent Versioning**: Rules evolve separately from code  

## Troubleshooting

### Submodule Not Found
```bash
git submodule init
git submodule update
```

### Merge Conflicts in Rules
```bash
cd .cursor/rules
git status
# Resolve conflicts
git add .
git commit
```

### Detached HEAD in Submodule
```bash
cd .cursor/rules
git checkout main
git pull origin main
```

## Best Practices

1. **Commit Rule Changes Separately**: Keep rule commits focused
2. **Use Descriptive Messages**: Explain what changed and why
3. **Test Before Pushing**: Verify rules work as expected
4. **Document Complex Rules**: Add comments in .mdc files
5. **Review Rule Changes**: Consider PR workflow for the cursor-rules repo

## Example Cursor Rules Structure

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

Each rule file includes:
- Front matter with metadata
- Clear description
- Specific instructions
- Examples when helpful
