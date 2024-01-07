def folders_to_choices(folders: list[dict[str, str]]) -> str:
    return "".join([f"<option value='{f['id']}'>{f['name']}</option>" for f in folders])


def order_images(data: list[dict[str, str]], order: list[str]) -> list[dict[str, str]]:
    order_dict: dict[str, int] = {}
    for o in order:
        image_id, order_num = o.split(":")
        order_dict[image_id] = int(order_num)
    return sorted(data, key=lambda x: order_dict[x["id"]])
