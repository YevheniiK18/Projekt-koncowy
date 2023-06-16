def check_syntax(file_path):
    try:
        compile(open(file_path, "rb").read(), file_path, 'exec')
        return True
    except SyntaxError:
        return False
    
def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def save_xml(data, file_path):
    tree = ET.ElementTree(data)
    tree.write(file_path)

main_file = __file__
    if not check_syntax(main_file):
        print(f"Błąd składni w pliku: {main_file}")
        sys.exit(1)


    imported_modules = [argparse, json, yaml, ET]
    for module in imported_modules:
        module_file = module.__file__ if hasattr(module, '__file__') else None
        if module_file and not check_syntax(module_file):
            print(f"Błąd składni w pliku: {module_file}")
            sys.exit(1)


    if len(sys.argv) > 1:
        run_from_command_line()
    else:
        run_with_ui()
