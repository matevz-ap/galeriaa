def folders_to_choices(folders: list[dict[str, str]]) -> str:
    return "".join([f"<option value='{f['id']}'>{f['name']}</option>" for f in folders])


def order_images(data: list[dict[str, str]], order: list[str]) -> list[str]:
    images: list[str] = []
    for i in range(3):
        for j in range(4):
            inx = i * 4 + j
            att = (inx % 4) * (i + 1) + i
            images.insert(att, order[inx])
    return sorted(data, key=lambda x: images.index(x["id"]))
