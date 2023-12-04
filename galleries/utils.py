def folders_to_choices(folders: list[dict[str, str]]) -> list[tuple[str, str]]:
    choices = []
    for folder in folders:
        choices.append((folder["id"], folder["name"]))
    return choices
