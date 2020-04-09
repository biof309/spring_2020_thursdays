from pathlib import Path
import os
import shutil 

def create_package_dir(package_name='packaging_demo'):
    start_dir = Path.cwd()
    print(f"Starting in {start_dir}")

    if start_dir.name == package_name:
        os.chdir(start_dir.parent)
        package_dir = start_dir
    else:
        package_dir = start_dir / package_name
    
    if package_dir.exists():
        print("Removing old directory...")
        shutil.rmtree(package_dir)

    print(f"Creating {package_dir}...")
    package_dir.mkdir()
    print(f"The current working directory is now {package_dir}")
    os.chdir(package_dir)

        
