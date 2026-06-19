import re
from urllib.parse import parse_qs, urlsplit

from bs4 import NavigableString, Tag


def is_character_5_star(character_img_tag: Tag) -> bool:
    # There is a row placed as a header for when 5 star characters start
    return character_img_tag.find_next(string="5 STAR") is None


def get_character_name(character_img_tag: Tag) -> str:
    cell = character_img_tag.find_parent("td")
    assert isinstance(cell, Tag), "Image wasn't in a tag"

    img_row = cell.find_parent("tr")
    assert isinstance(img_row, Tag), "Image's cell wasn't in a row"

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
                return text.title()

    raise Exception("Failed to extract name")


def get_character_notes(character_img_tag: Tag) -> str:
    cell = character_img_tag.find_parent("td")
    assert isinstance(cell, Tag), "Image wasn't in a tag"

    img_row = cell.find_parent("tr")
    assert isinstance(img_row, Tag), "Image's cell wasn't in a row"

    cell_rowspan = int(cell.attrs["rowspan"]) or 1

    notes_row = img_row.find_all_next("tr")[cell_rowspan - 1]
    assert isinstance(notes_row, Tag), "notes_row wasn't a Tag"

    notes = notes_row.find_all("td")[2]
    assert isinstance(notes, Tag), "notes wasn't a Tag"

    notes_text = __extract_text(notes).strip()

    return notes_text


# TODO: would be nice if eventually we could get text with format metadata such as bold, italics, underline, etc.
# This would also help with links I think!
def __extract_text(element: Tag) -> str:
    text = ""
    for elem in element.children:
        if isinstance(elem, NavigableString):
            text += elem.text
            continue
        assert isinstance(elem, Tag), "element wasn't a Tag"

        if elem.name == "br":
            text += "\n"
            continue

        if elem.name == "a":
            google_url = urlsplit(elem.attrs["href"])

            url = parse_qs(google_url.query)["q"][0]
            text += url
            continue

        text += __extract_text(elem)

    return text.replace(" \n", "\n")  # Some lines have a trailing whitespace
