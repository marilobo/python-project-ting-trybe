import sys
import os


def txt_importer(path_file):
    if not os.path.exists(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido")
    with open(path_file, mode="r") as file:
        lines = file.read().split("\n")
        return lines
