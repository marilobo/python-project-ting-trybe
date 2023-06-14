from ting_file_management.file_management import txt_importer
# import os


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


# def remove(instance):
#     if


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
