def exists_word(word, instance):
    word_lower = word.lower()
    result = []
    for file in instance._data:
        lines = []
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word_lower in line.lower():
                lines.append({"linha": index + 1})
        if lines:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines
            })
    return result


def search_by_word(word, instance):
    word_lower = word.lower()
    result = []
    for file in instance._data:
        info = []
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word_lower in line.lower():
                info.append({"linha": index + 1, "conteudo": line})

        if info:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": info
            })
    return result
