import subprocess

def run(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def current_branch():
    return run("git rev-parse --abbrev-ref HEAD")

def has_changes():
    return bool(run("git status --porcelain"))

def get_changed_files():
    """Get list of changed files"""
    return run("git status --porcelain")

def stage_files():
    run("git add .")

def commit(message):
    return run(f'git commit -m "{message}"')

def push():
    branch = current_branch()
    return run(f"git push origin {branch}")
