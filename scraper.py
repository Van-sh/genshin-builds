import itertools
import re
from dataclasses import dataclass
from typing import cast
from urllib import parse as urlparse

from bs4 import NavigableString, Tag

LAST_UPDATED_HEADER_REGEX = re.compile("Last Updated.*", re.IGNORECASE)
STAR_ICON = "✩"


@dataclass
class CharacterBuild:
    role: str
    is_recommended: bool
    # TODO: I wanna make these either a list of strings or a list of list of strings to handle equivalents better, not sure though!
    weapons: str
    artifacts: str
    # TODO: This should also be made into a named tuple for Sands, Goblet, Circlet, Extra/Tips
    main_stats: str
    sub_stats: str
    talent_priority: str
    ability_tips: str


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
            if row.find(string=LAST_UPDATED_HEADER_REGEX) is not None:
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

    cell_rowspan = __get_rowspan(cell)

    notes_row = img_row.find_all_next("tr")[cell_rowspan - 1]
    assert isinstance(notes_row, Tag), "notes_row wasn't a Tag"

    notes = notes_row.find_all("td")[2]
    assert isinstance(notes, Tag), "notes wasn't a Tag"

    notes_text = __extract_text(notes).strip()

    return notes_text


def get_character_builds(character_img_tag: Tag) -> list[CharacterBuild]:
    cell = character_img_tag.find_parent("td")
    assert isinstance(cell, Tag), "Image wasn't in a tag"

    role_cell_maybe = cell.find_next_sibling("td", string="ROLE")

    img_row = cell.find_parent("tr")
    assert isinstance(img_row, Tag), "Image's cell wasn't in a row"

    img_rowspan = __get_rowspan(cell)

    build_rows = itertools.islice(
        itertools.chain([img_row], img_row.next_siblings), img_rowspan
    )
    if isinstance(role_cell_maybe, Tag):
        role_cell_rowspan = __get_rowspan(role_cell_maybe)
        build_rows = itertools.islice(build_rows, role_cell_rowspan, None)

    builds = []

    (
        role_rowspan,
        weapon_rowspan,
        artifact_rowspan,
        main_stat_rowspan,
        sub_stat_rowspan,
        talent_priority_rowspan,
        ability_tip_rowspan,
    ) = 0, 0, 0, 0, 0, 0, 0

    for row in build_rows:
        role: str
        is_recommended: bool
        weapons: str
        artifacts: str
        main_stats: str
        sub_stats: str
        talent_priority: str
        ability_tips: str

        assert isinstance(row, Tag), "row should be a Tag"

        row_number = row.find("th")
        assert isinstance(row_number, Tag), "Row nuber should be the only th in a row"

        row_iterator = iter(cast(Tag, row_number.next_sibling).next_siblings)

        # Merge with previous row
        # if role_rowspan:
        #     role_rowspan -= 1

        #     previous_row = builds[-1]
        #     continue

        maybe_image = next(row_iterator)
        assert isinstance(maybe_image, Tag), "Expected a Tag"

        role_cell = (
            maybe_image if maybe_image.find("img") is None else next(row_iterator)
        )
        assert isinstance(role_cell, Tag), "Expected role cell to be a Tag"
        # role_rowspan = __get_rowspan(role_cell) - 1

        role = __extract_text(role_cell).strip()
        is_recommended = False
        if STAR_ICON in role:
            role = role.replace(STAR_ICON, "").strip()
            is_recommended = True

        role = role.replace("\n", " ")

        print(f"{role = }\n{is_recommended = }")

        if weapon_rowspan:
            weapon_rowspan -= 1

            weapons = builds[-1].weapons
            print(f"copy {weapons = }")
        else:
            weapon_cell = next(row_iterator)
            assert isinstance(weapon_cell, Tag)
            weapon_rowspan = __get_rowspan(weapon_cell) - 1

            weapons = __extract_text(weapon_cell).strip()
            print(f"new {weapons = }")

        if artifact_rowspan:
            artifact_rowspan -= 1

            artifacts = builds[-1].artifacts
            print(f"copy {artifacts = }")
        else:
            artifact_cell = next(row_iterator)
            assert isinstance(artifact_cell, Tag)
            artifact_rowspan = __get_rowspan(artifact_cell) - 1

            artifacts = __extract_text(artifact_cell).strip()
            print(f"new {artifacts = }")

        if main_stat_rowspan:
            main_stat_rowspan -= 1

            main_stats = builds[-1].main_stats
            print(f"copy {main_stats = }")
        else:
            main_stat_cell = next(row_iterator)
            assert isinstance(main_stat_cell, Tag)
            main_stat_rowspan = __get_rowspan(main_stat_cell) - 1

            main_stats = __extract_text(main_stat_cell).strip()
            print(f"new {main_stats = }")

        if sub_stat_rowspan:
            sub_stat_rowspan -= 1

            sub_stats = builds[-1].sub_stats
            print(f"copy {sub_stats = }")
        else:
            sub_stat_cell = next(row_iterator)
            assert isinstance(sub_stat_cell, Tag)
            sub_stat_rowspan = __get_rowspan(sub_stat_cell) - 1

            sub_stats = __extract_text(sub_stat_cell).strip()
            print(f"new {sub_stats = }")

        if talent_priority_rowspan:
            talent_priority_rowspan -= 1

            talent_priority = builds[-1].talent_priority
            print(f"copy {talent_priority = }")
        else:
            talent_priority_cell = next(row_iterator)
            assert isinstance(talent_priority_cell, Tag)
            talent_priority_rowspan = __get_rowspan(talent_priority_cell) - 1

            talent_priority = __extract_text(talent_priority_cell).strip()
            print(f"new {talent_priority = }")

        if ability_tip_rowspan:
            ability_tip_rowspan -= 1

            ability_tips = builds[-1].ability_tips
            print(f"copy {ability_tips = }")
        else:
            ability_tip_cell = next(row_iterator)
            assert isinstance(ability_tip_cell, Tag)
            ability_tip_rowspan = __get_rowspan(ability_tip_cell) - 1

            ability_tips = __extract_text(ability_tip_cell).strip()
            print(f"new {sub_stats = }")

        # if weapon_rowspan > 0:
        builds.append(
            CharacterBuild(
                role,
                is_recommended,
                weapons,
                artifacts,
                main_stats,
                sub_stats,
                talent_priority,
                ability_tips,
            )
        )

    return builds


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
            google_url = urlparse.urlsplit(elem.attrs["href"])

            url = urlparse.parse_qs(google_url.query)["q"][0]
            text += url
            continue

        text += __extract_text(elem)

    return text.replace(" \n", "\n")  # Some lines have a trailing whitespace


def __get_rowspan(cell: Tag) -> int:
    return int(cell.attrs.get("rowspan") or "1")
