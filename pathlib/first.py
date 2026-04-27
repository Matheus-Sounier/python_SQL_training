from pathlib import Path

print(Path.cwd())
for i in Path('../Downloads').iterdir():
    print(i)