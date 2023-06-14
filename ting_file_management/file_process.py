from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # file_name = os.path.basename(path_file)
    for i in instance._data:
        if i["nome_do_arquivo"] == path_file:
            return

    file_lines = txt_importer(path_file)

    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }

    instance.enqueue(file_dict)
    print(file_dict)


def remove(instance):
    if not instance.is_empty():
        path_file = instance.dequeue()
        print(f"Arquivo {path_file['nome_do_arquivo']} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        sys.stderr.write("Posição inválida")
