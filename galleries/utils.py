def folders_to_choices(folders: list[dict[str, str]]) -> str:
    return "".join([f"<option value='{f['id']}'>{f['name']}</option>" for f in folders])
