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
    
    # Ensure .cursor/ directory exists
    cursor_dir = os.path.join(project_dir, ".cursor")
    os.makedirs(cursor_dir, exist_ok=True)
    
    # Remove any existing rules directory (it should be empty from template)
    if os.path.exists(submodule_path):
        import shutil
        shutil.rmtree(submodule_path)
    
    print(f"Adding cursor-rules submodule from {repo_url}")
    
    # Add the submodule
    run(f"git submodule add {repo_url} .cursor/rules", cwd=project_dir)
    run("git submodule update --init --recursive", cwd=project_dir)
    
    # Commit the submodule addition
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
    print("📋 Cursor rules have been added as a git submodule.")
    print("🔄 To update cursor rules in the future, run: git submodule update --remote")

if __name__ == "__main__":
    main()
