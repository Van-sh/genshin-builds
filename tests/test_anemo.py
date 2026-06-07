from pathlib import Path
from typing import cast
from unittest import TestCase

from bs4 import BeautifulSoup, NavigableString, Tag

from scraper import get_character_name, is_character_5_star

_soup: BeautifulSoup


def setUpModule():
    global _soup
    with open(Path("local/anemo.html")) as f:
        _soup = BeautifulSoup(f.read(), "html.parser")


class Sucrose(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="SUCROSE"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "sucrose")


class Sayu(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="SAYU"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "sayu")


class ShikanoinHeizou(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="SHIKANOIN HEIZOU"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "shikanoin heizou")


class Faruzan(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="FARUZAN"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "faruzan")


class Lynette(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="LYNETTE"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "lynette")


class LanYan(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="LAN YAN"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "lan yan")


class Ifa(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="IFA"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "ifa")


class Jahoda(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="JAHODA"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "jahoda")


class Prune(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="PRUNE"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "prune")


class Traveler(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="TRAVELER"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "traveler")


class Jean(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="JEAN"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "jean")


class Venti(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="VENTI"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "venti")


class Xiao(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="XIAO"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "xiao")


class KaedeharaKazuha(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="KAEDEHARA KAZUHA"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "kaedehara kazuha")


class Wanderer(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="WANDERER"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "wanderer")


class Xianyun(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="XIANYUN"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "xianyun")


class Chasca(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="CHASCA"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "chasca")


class YumemizukiMizuki(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="YUMEMIZUKI MIZUKI"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "yumemizuki mizuki")


class Varka(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="VARKA"))
        cls.img = cast(Tag, name.find_next("img"))

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "varka")
