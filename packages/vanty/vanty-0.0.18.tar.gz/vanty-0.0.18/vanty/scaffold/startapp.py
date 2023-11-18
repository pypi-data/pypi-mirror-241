import typer
import shutil
import subprocess
from pathlib import Path

app = typer.Typer(name="scaffold", help="Scaffold new Django apps", no_args_is_help=True)


TEMPLATE_DIR = Path(__file__).resolve().parent

@app.command()
def startapp(app_name: str, destination: str = "apps"):
    """
    Create a new Django app using a custom template.
    :param app_name: Name of the new Django app.
    :param destination: Destination directory for the new app.
    """
    try:
        # Path where the new app will be created
        new_app_path = Path.cwd() / destination / app_name
        
        # Ensure the destination directory exists
        new_app_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Temporary path for the template
        temp_template_path = Path.cwd() / "temp_template"
        
        # Copy the template to the temporary location
        shutil.copytree(TEMPLATE_DIR, temp_template_path, dirs_exist_ok=True)
        
        # Run the Django startapp command with the temporary template
        subprocess.run([
            "docker-compose", "run", "--rm", "django",
            "./manage.py", "startapp", app_name, str(new_app_path),
            "--template", str(temp_template_path)
        ], check=True)
        
        # Clean up: remove the temporary template directory
        shutil.rmtree(temp_template_path)
        
        typer.echo(f"Successfully created new app: {app_name} at {new_app_path}")
    
    
    except Exception as e:
        typer.echo(f"Error: {e}")
