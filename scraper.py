from bs4 import Tag


def is_character_5_star(img: Tag):
    return img.find_next(string="5 STAR") is None


def get_character_name(img: Tag): ...
