import sys
import os
import re
import importlib.abc
import importlib.util
import argparse

class OuroborosEngine:
    """
    O motor da linguagem Ouroboros.
    Responsável por traduzir (.or -> .py) e formatar (.or -> .or bonito).
    """
    
    # Regex para detectar estruturas
    RX_END = re.compile(r'^\s*end\s*(#.*)?$')
    # Detecta estruturas intermediárias que devem recuar visualmente (else, elif, except, finally)
    RX_MID_BLOCK = re.compile(r'^\s*(else:|elif\s|except|finally:).*')

    @staticmethod
    def _process_lines(source_code, mode='transpile'):
        lines = source_code.splitlines()
        processed_lines = []
        indent_level = 0
        indent_str = "    " 

        for line in lines:
            stripped = line.strip()
            
            if not stripped:
                processed_lines.append("")
                continue

            is_end = OuroborosEngine.RX_END.match(stripped)
            is_mid_block = OuroborosEngine.RX_MID_BLOCK.match(stripped)

                       
            # Se for 'end', fechamos o bloco
            if is_end:
                indent_level = max(0, indent_level - 1)

            # Se for 'else/elif', nós TEMOS que fechar o escopo do 'if' anterior
            # antes de abrir o novo escopo do 'else'.
            if is_mid_block:
                indent_level = max(0, indent_level - 1)

            current_indent = indent_level

            # --- Geração de Código ---

            if mode == 'transpile':
                if is_end:
                    processed_lines.append(f"{indent_str * current_indent}# end")
                else:
                    processed_lines.append(f"{indent_str * current_indent}{stripped}")
            
            elif mode == 'format':
                processed_lines.append(f"{indent_str * current_indent}{stripped}")

            # --- Preparação para a Próxima Linha ---
            
            # Se a linha termina com ':', abrimos um novo bloco
            if stripped.endswith(":") and not stripped.startswith("#"):
                indent_level += 1

        return "\n".join(processed_lines)

    @staticmethod
    def transpile(source_code):
        return OuroborosEngine._process_lines(source_code, mode='transpile')

    @staticmethod
    def format(source_code):
        return OuroborosEngine._process_lines(source_code, mode='format')

# --- Sistema de Importação (Hooks) ---

class OuroborosLoader(importlib.abc.Loader):
    def __init__(self, filename):
        self.filename = filename

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        with open(self.filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Traduz on-the-fly para Python válido
        python_code = OuroborosEngine.transpile(source)
        
        # Compila e executa no namespace do módulo
        code_obj = compile(python_code, self.filename, 'exec')
        exec(code_obj, module.__dict__)

class OuroborosFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if path is None:
            path = sys.path
        
        module_name = fullname.split('.')[-1]
        
        for entry in path:
            filename = os.path.join(entry, f"{module_name}.or")
            if os.path.exists(filename):
                return importlib.util.spec_from_loader(
                    fullname,
                    OuroborosLoader(filename)
                )
        return None

def install():
    """Ativa o suporte a importação de .or"""
    if not any(isinstance(x, OuroborosFinder) for x in sys.meta_path):
        sys.meta_path.insert(0, OuroborosFinder())

# --- CLI (Interface de Linha de Comando) ---

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ferramenta da Linguagem Ouroboros (.or)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Comando: run
    run_parser = subparsers.add_parser("run", help="Executa um script .or")
    run_parser.add_argument("file", help="Arquivo .or para executar")

    # Comando: format
    fmt_parser = subparsers.add_parser("format", help="Corrige a indentação de um arquivo .or")
    fmt_parser.add_argument("file", help="Arquivo .or para formatar")

    args = parser.parse_args()

    if args.command == "run":
        # Ativa imports para dependências .or
        install()
        
        filepath = args.file
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        
        transpiled = OuroborosEngine.transpile(source)
        
        # Simula o ambiente __main__
        global_vars = {'__name__': '__main__', '__file__': filepath, '__doc__': None}
        exec(compile(transpiled, filepath, 'exec'), global_vars)

    elif args.command == "format":
        filepath = args.file
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        
        formatted = OuroborosEngine.format(source)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(formatted)
        
        print(f"✅ Ouroboros: '{filepath}' foi indentado com sucesso.")