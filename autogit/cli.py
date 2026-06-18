import typer
from rich.console import Console
from rich.table import Table
from autogit.git_utils import *

console = Console()
app = typer.Typer()

@app.command()
def main(message: str = typer.Argument(None, help="Commit message")):
    """AutoGit: Automatic git add, commit, and push"""
    
    # Check if git repo exists
    try:
        current_branch()
    except:
        console.print("[red]✗ Not a git repository![/red]")
        raise typer.Exit(1)
    
    # Check for changes
    if not has_changes():
        console.print("[green]✓ Repository is clean. Nothing to commit.[/green]")
        raise typer.Exit()
    
    # Show changed files
    changed = get_changed_files()
    console.print("\n[cyan]📝 Changed files:[/cyan]")
    for line in changed.split("\n"):
        if line:
            console.print(f"  {line}")
    
    # Use default message if not provided
    if not message:
        message = "Update project files"
    
    console.print(f"\n[cyan]💬 Commit message: {message}[/cyan]")
    console.print(f"[cyan]🌿 Branch: {current_branch()}[/cyan]\n")
    
    # Stage files
    console.print("[cyan]➕ Staging files...[/cyan]")
    stage_files()
    
    # Create commit
    console.print("[cyan]📦 Creating commit...[/cyan]")
    commit(message)
    
    # Push to GitHub
    console.print("[cyan]🚀 Pushing to GitHub...[/cyan]")
    push()
    
    console.print("\n[bold green]✓ Done! Pushed successfully![/bold green]\n")

if __name__ == "__main__":
    app()
