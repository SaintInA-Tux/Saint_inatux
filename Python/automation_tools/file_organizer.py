"""Organize files in a directory by extension."""
import sys
from pathlib import Path


EXT_MAP = {
'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
'docs': ['.pdf', '.docx', '.doc', '.txt', '.xlsx'],
'archives': ['.zip', '.tar', '.gz', '.rar'],
'code': ['.py', '.java', '.js', '.cpp', '.c', '.cs']
}




def folder_for(ext):
for k, v in EXT_MAP.items():
if ext.lower() in v:
return k
return 'others'




if __name__ == '__main__':
if len(sys.argv) < 2:
print('Usage: python file_organizer.py <dir>')
sys.exit(1)
base = Path(sys.argv[1])
if not base.is_dir():
print('Not a directory')
sys.exit(1)
for f in base.iterdir():
if f.is_file():
dest = base / folder_for(f.suffix)
dest.mkdir(exist_ok=True)
f.rename(dest / f.name)
print('Organizing complete')
