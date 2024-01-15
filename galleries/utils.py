def folders_to_choices(folders: list[dict[str, str]]) -> str:
    return "".join([f"<option value='{f['id']}'>{f['name']}</option>" for f in folders])


def order_images(data: list[dict[str, str]], order: list[str]) -> list[str]:
    images: list[list[str]] = [[], [], []]
    for i, photo in enumerate(order):
        images[i % 3].append(photo)
    img = []
    for col in images:
        for c in col:
            img.append(c)
    print(img)
    return sorted(data, key=lambda x: img.index(x["id"]))
