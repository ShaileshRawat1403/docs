import pathlib, sys

def title_case(filename):
    words = filename.replace('_','-').split('-')
    return ' '.join(w.capitalize() for w in words)

def check_file(path):
    expected = f"# {title_case(path.stem)}"
    with open(path, encoding='utf-8') as f:
        first_line = f.readline().strip()
    if first_line != expected:
        print(f"{path}: '{first_line}' != '{expected}'")
        return False
    return True

if __name__ == '__main__':
    md_files = [pathlib.Path(p) for p in sys.argv[1:]]
    ok = True
    for p in md_files:
        if not check_file(p):
            ok = False
    if not ok:
        sys.exit(1)
