from pathlib import Path
from threading import Thread

import niquests

from main import ELEMENT_IDS, BASE_URL

local_dir = Path("local")


def main():
    if not local_dir.exists():
        local_dir.mkdir()

    handlers = []
    for element in ELEMENT_IDS:
        handler = Thread(target=make_element_file, args=(element,))
        handler.start()
        handlers.append(handler)

    for handler in handlers:
        handler.join()


def make_element_file(element: str):
    element_path = local_dir / f"{element}.html"

    page = niquests.get(BASE_URL + ELEMENT_IDS[element]).text
    if page is None:
        raise Exception(f"Failed to fetch {element} page")
    with open(element_path, "w") as f:
        f.write(page)


if __name__ == "__main__":
    main()
