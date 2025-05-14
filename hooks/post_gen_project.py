import subprocess
import os
import sys

def run(cmd, cwd=None):
    """Execute a shell command and handle errors."""
    print(f">>> Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        sys.exit(1)

def init_git_repo(project_dir):
    """Initialize a git repository if it doesn't exist."""
    git_dir = os.path.join(project_dir, ".git")
    if not os.path.exists(git_dir):
        print("Initializing git repository...")
        run("git init", cwd=project_dir)
        run("git add .", cwd=project_dir)
        run('git commit -m "Initial project scaffold from cookiecutter"', cwd=project_dir)

def add_cursor_rules_submodule(project_dir):
    """Add the cursor-rules repository as a git submodule."""
    repo_url = "{{ cookiecutter.cursor_rules_repo }}"
    submodule_path = os.path.join(project_dir, ".cursor", "rules")
    
    # Smart detection: Check if the rules already exist and if they're from the same source
    if os.path.exists(os.path.join(submodule_path, "010-core-python-style.mdc")):
        print("Cursor rules already exist in the project.")
        
        # Option A: If using the template repo as cursor rules, just use the local files
        if "cookiecutter-python-project" in repo_url:
            print("Using the cookiecutter template's cursor rules directly.")
            print("No submodule needed - the rules are already included.")
            print("\n💡 Tip: To use a separate cursor-rules repository:")
            print("   1. Create a new repository for your cursor rules")
            print("   2. Copy the rules from .cursor/rules/ to your new repository")
            print("   3. Update to use that repository URL for future projects")
            return
        
        # Option B: If using a different repo, we need to replace with submodule
        else:
            print(f"Replacing local rules with submodule from {repo_url}")
            # Remove from git index first
            run(f"git rm -rf .cursor/rules", cwd=project_dir)
            run('git commit -m "Remove template cursor rules to add custom submodule"', cwd=project_dir)
    
    # Only add submodule if we actually need it
    print(f"Adding cursor-rules submodule from {repo_url}")
    run(f"git submodule add {repo_url} .cursor/rules", cwd=project_dir)
    run("git submodule update --init --recursive", cwd=project_dir)
    run("git add .gitmodules .cursor/rules", cwd=project_dir)
    run('git commit -m "Add cursor-rules as submodule"', cwd=project_dir)

def main():
    """Main post-generation hook."""
    project_dir = os.path.realpath(os.path.curdir)
    print(f"Running post-generation hook in: {project_dir}")
    
    # Initialize git repo first
    init_git_repo(project_dir)
    
    # Add cursor rules submodule
    add_cursor_rules_submodule(project_dir)
    
    print("\n✅ Project setup complete!")
    
    # Check if we're using local rules or submodule
    repo_url = "{{ cookiecutter.cursor_rules_repo }}"
    if "cookiecutter-python-project" in repo_url:
        print("📋 Cursor rules are included directly in the project.")
        print("🌟 These rules are from the cookiecutter template itself.")
    else:
        print("📋 Cursor rules have been added as a git submodule.")
        print("🔄 To update cursor rules in the future, run: git submodule update --remote")

if __name__ == "__main__":
    main()
