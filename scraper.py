import re

from bs4 import Tag


def is_character_5_star(character_img_tag: Tag):
    # There is a row placed as a header for when 5 star characters start
    return character_img_tag.find_next(string="5 STAR") is None


def get_character_name(character_img_tag: Tag):
    cell = character_img_tag.find_parent("td")
    if not isinstance(cell, Tag):
        raise ValueError("Image wasn't in a tag")

    img_row = cell.find_parent("tr")
    if not isinstance(img_row, Tag):
        raise ValueError("Image's cell wasn't in a row")

    found_last_updated = False
    for row in img_row.previous_siblings:
        if not isinstance(row, Tag):
            continue

        if not found_last_updated:
            if row.find(string=re.compile("Last Updated.*", re.IGNORECASE)) is not None:
                found_last_updated = True
            continue

        for cell in row.find_all("td"):
            if not isinstance(cell, Tag):
                continue

            if len(text := cell.get_text(strip=True)) > 0:
                return text.lower()

    raise Exception("Failed to extract name")
