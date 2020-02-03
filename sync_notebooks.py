# coding: utf-8
from pathlib import Path
import shutil
my_notebooks = Path('my_notebooks')
if not my_notebooks.exists():
    my_notebooks.mkdir()
    
for d in Path('notebooks').iterdir():
    if d.is_dir:
        print(f"copying {d}")
        dest_dir  = Path('my_notebooks') / d.name
        if not dest_dir.exists():
            shutil.copytree(d,dest_dir)
            
            
        
        
