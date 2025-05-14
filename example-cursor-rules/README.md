# Example Cursor Rules

This directory contains a complete set of Cursor IDE rules designed for Python projects following Test-Driven Development (TDD) practices.

## Rule Files

### Foundation Rules (Always Active)

**010-core-python-style.mdc**
- Enforces PEP 8 and Black formatting (100 char line length)
- Requires type hints on all public functions
- Mandates logging over print statements
- Enforces f-string usage for string formatting

### Development Rules (Auto-Attached)

**020-docstrings.mdc**
- Ensures NumPy-style docstrings on all functions/classes
- Auto-generates docstring templates
- Includes parameters, returns, and examples sections

**030-tdd-python.mdc**
- Enforces test-first development workflow
- Requires failing test before implementation
- Promotes small, focused commits

### Specialized Rules (Triggered)

**040-bug-fix-tdd.mdc**
- Activated on bug-fix requests
- Requires regression test in `tests/regressions/`
- Documents root cause and fix

**100-pytest-autogen.mdc**
- Triggered on new feature requests
- Suggests test scaffold before implementation
- Uses pytest.mark.parametrize for edge cases

### Domain Rules (Context-Specific)

**200-domain-specific.mdc**
- Applies to domain layer only (`domain/**/*.py`)
- Enforces business invariants
- Decimal for money, UnitOfWork for persistence

## Using These Rules

1. **As a Git Submodule** (Recommended):
   ```bash
   git init cursor-rules
   cp -r example-cursor-rules/.cursor cursor-rules/
   cd cursor-rules
   git add .
   git commit -m "Initial cursor rules"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Direct Copy**:
   ```bash
   cp -r example-cursor-rules/.cursor /your/project/
   ```

## Rule Ordering

Rules are numbered to control load order:
- 010-020: Core style (always first)
- 030-040: TDD workflow
- 100+: Feature-specific rules

Lower numbers load first, establishing base behavior that higher-numbered rules can build upon.

## Customization

Feel free to:
- Adjust rule numbers to change priority
- Modify globs to match your project structure
- Add project-specific rules (300+)
- Disable rules by setting `alwaysApply: false`

## Best Practices

1. Keep rules focused and single-purpose
2. Use descriptive file names
3. Document rule behavior clearly
4. Test rules in isolation before deploying
5. Version control your rules repository
