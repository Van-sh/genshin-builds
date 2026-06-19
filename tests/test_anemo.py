from pathlib import Path
from typing import cast
from unittest import TestCase

from bs4 import BeautifulSoup, NavigableString, Tag

from scraper import get_character_name, get_character_notes, is_character_5_star

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
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Sucrose")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "EM SUPPORT",
                    "Sucrose's Ascension 4 Talent boosts the entire team's EM by 20% of Sucrose's total EM, this is why you want to stack as much Elemental Mastery as possible in her artifacts. As a support, most of Sucrose's value lies on her Ascension 1 and 4 talents, hence leveling her other talents (Normal Attack, Skill, Burst) is not required.",
                    "",
                    "Regarding Weapon Choices:",
                    "Thrilling Tales of Dragon Slayers: This weapon does not provide any EM, however it overtakes the other weapons on the list when it comes to buffing your team. It offers 48% ATK boost to the character you swap to which is equivalent to 1 main stat. This buffs your DPS more compared to Sacrificial Fragments which gives ~44EM, equivalent to only 2 substats.",
                    "Hakushin Ring: This weapon is a good option for teams where Sucrose can swirl Electro to trigger its damage-boosting passive. In Electro-Charged teams, she can buff Hydro DMG% as well.",
                    "Favonius Codex: This weapon can be useful if you value the extra energy generation from the passive. You may need to get a few Crit Rate substats to trigger the passive reliably.",
                    "",
                    "There are some team compositions in which Sucrose's Elemental Mastery is not a priority, such as Freeze teams or an Anemo battery for Xiao. In such situations it's better for Sucrose to use Thrilling Tales of the Dragon Slayers.",
                )
            ),
        )


class Sayu(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="SAYU"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Sayu")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "SUPPORT",
                    "Sayu does more damage with EM builds and heals more with ATK hybrid builds, Healing Bonus circlet's can be used for better heals while maintaining respectable damage. Note that Sayu wants a large amount of Energy Recharge when used as the only Anemo slot on the team.",
                    "",
                    "Regarding Weapon Choices:",
                    "Wolf's Gravestone: This is a universal claymore that is capable of buffing your teammates along with providing more healing in Sayu's case. It is best used once you achieve your ER threshold.",
                    "Forest Regalia: When used in its niche with aggravate teams it can outperform Katsuragikiri Nagamasa. Outside of that its just an Energy Recharge% stat stick.",
                    "",
                    "Regarding Artifact Sets:",
                    "Viridescent Venerer (4): The bread and butter artifact set for Anemo units, this set provides the ability to shred the enemy's elemental resistance while also buffing Sayu's Swirl damage output.",
                    "Ocean-Hued Clam (4): This artifact set trades Sayu's utility in favor of stronger healing and some extra damage. It is generally not recommended to farm this set for Sayu specifically.",
                )
            ),
        )


class ShikanoinHeizou(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="SHIKANOIN HEIZOU"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Shikanoin Heizou")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "Regarding Support Weapon Options:",
                    "In teams where Heizou's damage is less potent, or his goal is to support the team with 4VV and his A4, he can choose to run one of the following weapons.",
                    "Favonius Codex: This weapon can help lower ER requirements for the team, as well as allow Heizou to run less ER on himself.",
                    "Thrilling Tales of Dragon Slayers: This weapon offers a colossal 48% ATK buff to a party member at the expense of Heizou's damage.",
                    "Hakushin Ring: In Electro-Charged teams, this can be used to buff both Anemo, Hydro, and Electro damage, and scales well with refines. It is recommended to run Anemo DMG based artifacts on this build.",
                    "Prototype Amber: In teams where there is no healer, Shikanoin Heizou can use this weapon to help the team's survivability.",
                    "",
                    "ANEMO DPS",
                    "Shikanoin Heizou's Anemo DPS build is roughly equal to his Elemental Mastery build assuming he isn't being used in an Electro-Charged team. He has very low Energy Recharge needs; At [C4] he can run 100% Energy Recharge.",
                    "",
                    "Regarding Weapon Choices:",
                    "Lost Prayer to the Sacred Winds: In teams where Shikanoin Heizou and Bennett are used in the same team, this weapon is better than Skyward Atlas.",
                    "The Widsith: The Widsith provides the highest possible critical hit single strike damage for Heizou. However, its long cooldown leads it to lack consistency, and it has a chance of obtaining the relatively useless EM buff for Anemo DPS Heizou.",
                    "",
                    "Regarding Artifact Sets:",
                    "Viridescent Venerer (4): Heizou should use this set unless someone else in the team has it.",
                    "",
                    "REACTION DPS",
                    "Shikanoin Heizou does not get the same benefits from an EM build as other Anemo users do. He still has to level his talents, and allocate substats into offensive substats such as attack and crit to equal Anemo DPS. However it is notably better than Anemo DPS build if used in Electro-Charged teams.",
                    "",
                    "Regarding Artifact Sets:",
                    "Noblesse Oblige (4): Only use this set if you already have a Viridescent Venerer (4) user on your team",
                    "",
                    "Detailed weapon comparisons https://docs.google.com/spreadsheets/d/1U_P36PHD51-Yd8kgwvbd2AfR_fT0L1JTN8QueuUPtdE/edit?usp=sharing.",
                )
            ),
        )


class Faruzan(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="FARUZAN"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Faruzan")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "SUPPORT",
                    "As the premier Anemo support unit for Anemo dps based teams, Faruzan combines both high Anemo damage buffing with Anemo resistance shredding to become a cornerstone of any team that wants to focus on Anemo damage. Though building her means primarily focusing on dealing with her high Energy Requirements.",
                    "",
                    "Regarding Weapon Choices:",
                    "Elegy for the End: Usually only a better option at higher constellation levels such as [C6] where her energy needs can be met without Favonius passive particles.",
                    "Sacrificial Bow: It's worth mentioning that the extra Pressurized Collapse from a second E wont give you any extra particles if it's within her 5.5 second particle generation cooldown.",
                    "",
                    "Regarding Artifact Sets:",
                    "Important Note: Faruzan's Energy Recharge requirements pre-C6 can be extremely high, so high that it can be difficult to build enough using a 4pc set bonus. As such, using Emblem of Severed Fate (2) with whatever artifact combination will give you the most Energy Recharge is a reasonable option.",
                    "Viridescent Venerer (4): This set should be used in teams which have a significant amount of Pyro/Hydro/Electro/Cryo damage. Note the resistance shred does not buff Anemo damage and the set wielder must Swirl the element(s) while on-field for the resistance shred.",
                    "Noblesse Oblige (4): This is her best option in teams that either won't benefit significantly from Viridescent Venerer (4) shred, or teams that already have another unit holding the aforementioned set.",
                    "Tenacity of the Millelith (4): This has similar usage cases to Noblesse Oblige (4), except in that it requires Faruzan C6 for improved uptime through extra Pressurized Collapse activations.",
                    "Emblem of Severed Fate (4): This set will give Faruzan her best personal damage output, assuming the team is already running Viridescent Venerer (4). Also if you're willing to invest more time farming substats it can potentially give you more Energy Recharge than running The Exile (2).",
                    "Golden Troupe: This set is better than Emblem of Severed Fate (4) if Faruzan is C6 because of the pressurized collapse damage.",
                )
            ),
        )


class Lynette(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="LYNETTE"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Lynette")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "OFF-FIELD DPS",
                    "Lynette serves as a burst-oriented Anemo unit, that unlike other Anemo units does not excel in any one category such as personal damage, crowd control and buffs. Her potential for crowd control is partially dependent on unlocking her [C1] and [C4], and neither her ATK buff nor her personal damage reach notably high levels. What truly distinguishes her among Anemo characters is her unique capability to utilize ousia-aligned attacks as a Fontaine character. This distinct trait enables her to neutralize specific enemy mechanics by triggering annihilation reactions, as part of the overall Arkhe mechanic.",
                    "",
                    "Regarding Weapon Choices:",
                    "Freedom-Sworn: While this is her best buffing weapon it would be extremely difficult to meet her Energy requirements without an Energy Recharge weapon especially while primarily using her as an off-field unit.",
                    "Sacrificial Sword: Ideally you would want higher refinement levels as in [R3]+ so its cooldown aligns better with your rotation.",
                    "",
                    "Regarding Artifact Sets:",
                    "Noblesse Oblige (4): This is a good option for her in teams that either won't benefit significantly from Viridescent Venerer (4) shred, or where putting it on her is the lowest total team damage loss.",
                    "Emblem of Severed Fate (4): This set will give Lynette her best personal damage output, assuming the team is already running Viridescent Venerer (4).",
                )
            ),
        )


class LanYan(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="LAN YAN"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Lan Yan")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "SUPPORT",
                    "Lan Yan supports her team through shields and grouping.",
                    "",
                    "Regarding Weapon Choices:",
                    "Hakushin Ring: This weapon excels when Lan Yan is in an Electro-based team.",
                    "",
                    "DRIVER",
                    "Lan Yan can also contribute some of her damage to the team as a driver through her EM scalings. Though it does sacrifice some of her shield strength.",
                )
            ),
        )


class Ifa(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="IFA"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Ifa")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "REACTION DPS",
                    "Ifa uses his Elemental Mastery scalings to provide teamwide healing while driving reactions on-field. He can assist in permanently tranquilizing his foes by buffing the Swirl and Electro-Charged reactions, based on the total number of Nightsoul Points shared across the entire team, up to a maximum of 150 points (200 if Ifa is [C2]). For this reason, it is highly recommended to pair Ifa with Ororon.",
                    "",
                    "Regarding Weapon Choices: Weapon options below Mappa Mare do not improve Ifa's healing capabilities.",
                    "Sacrificial Fragments: While having a similar DMG output as Mappa Mare, this weapon will provide more total healing over your rotations.",
                    "Thrilling Tales of Dragon Slayers: This weapon is a support option to help boost the ATK% of your other off-field DPS's, notably Fischl, Xingqiu, and Ororon.",
                    "",
                    "ANEMO DPS",
                    "This build focuses on Ifa's Anemo Damage.",
                    "",
                    "Regarding Weapon Choices:",
                    "Cashflow Supervision: When HP loss is present (notably with Furina), this weapon becomes Ifa's best in slot.",
                    "The Widsith: At [R5], this weapon will perform roughly equal to Surf's Up! and its similar ranking options.",
                    "",
                    "Regarding Artifact Choices:",
                    "Viridescent Venerer (4): Prioritize this set if no one else holds it.",
                    "",
                    "Detailed weapon comparisons https://docs.google.com/spreadsheets/d/1GrnCVW55RGOrPxBWq1sZkCqs6kvJrLFTVvpsz5uDGEA/edit?usp=sharing.",
                )
            ),
        )


class Jahoda(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="JAHODA"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Jahoda")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "OFF-FIELD DPS & SUPPORT",
                    "Jahoda offers continuous healing for the active character with her Elemental Burst, and Off-Field Elemental Application with her infused Elemental Skill and Burst. While Ascendant Gleam is active, her Elemental Skill can steal enemy auras and use it for herself.",
                    "",
                    "Regarding Artifact Choices:",
                    "Viridescent Venerer (4): Prioritize this set if no one else holds it.",
                    "Deepwood Memories (4): This set can be used in teams where there is a large amount of Dendro damage, such as in Nefer teams.",
                )
            ),
        )


class Prune(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="PRUNE"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertFalse(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Prune")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "BUFF SUPPORT",
                    "Prune is a support that relies on triggering the Swirl reaction to buff characters. Triggering Swirl will convert her Banehunter Oathhammer (Elemental Skill) into the element she Swirls, and as long as her A4 talent is unlocked, hitting opponents with a converted Banehunter Oathhammer or her Elemental Burst will activate the Tolling Rally effect, which will provide DMG buffs to the team based on Prune's ATK. In addition, when a Hexerei character under Tolling Rally triggers a reaction, Prune gains an ATK% boost, and if that reaction was Swirl, the triggering character also gains an ATK% boost.",
                    "",
                    "Prune's [C1] let's her restore 2 Energy every 1.8 seconds whenever a converted Banehunter Oathhammer hits opponents. How much total energy she can restore depends how often Prune is able to trigger Swirl during the duration of her Elemental Burst. Prune's [C6] increases her Elemental Burst duration by 4 seconds.",
                    "",
                    "Regarding Weapon Choices:",
                    "Favonius Codex: In teams where Energy isn't much of an issue for Prune or the team, it is better to use a weapon that provides more ATK.",
                    "Thrilling Tales of Dragon Slayers: While this weapon significantly decreases the value of Prune's buff due to its low Base Attack, it can provide a 48% ATK boost to the DPS, which can be valuable depending on the team she is in.",
                    "",
                    "Regarding Artifact Choices:",
                    "Viridescent Venerer (4) and Celestial Gift (4): These sets are interchangeable depending on if there are members in the team that are already holding one or the other set.",
                )
            ),
        )


class Traveler(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="TRAVELER"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Traveler")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "ANEMO DPS",
                    "This section is dedicated to utilising the Anemo Traveler's Elemental Skill / Burst. Due to how little field time this playstyle takes, the Traveler can also fulfill the role of a quickswap style Sub-DPS.",
                    "Anemo Traveler can require a significant amount of Energy Recharge.",
                    "",
                    "Regarding Weapon Choices:",
                    "Anemo Traveler can either go for a full Elemental Mastery build or a full ATK/Crit build without much difference in damage. The weapon rankings listed here will not change much between the two builds.",
                    "Sacrificial Sword: This weapon's ranking assumes you make use of the passive Elemental Skill reset, however doing so will require you to stay onfield for a much longer period of time which may not be ideal sometimes.",
                    "Amenoma Kageuchi: This weapon reduces your ER% requirements to depending on refinement. At [R5], this weapon will be better than Sacrificial Sword.",
                    "Favonius Sword: Although this weapon does not provide much damage, the Energy generated by the passive can sometimes be more beneficial to your team. Make sure to build some amount of Crit Rate to reliably trigger the passive.",
                )
            ),
        )


class Jean(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="JEAN"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Jean")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "SUPPORT AND DAMAGE",
                    "Jean's Elemental Skill can be used to fling smaller mobs into the air to deal fall damage, and to stagger bigger ones. Her healing scales with ATK.",
                    "",
                    "Regarding Weapon Choices:",
                    "Amenoma Kageuchi: This weapon can lower your ER% requirements, depending on the number of stacks on the passive and the refinement of this weapon. As such, at higher refines / more stacks on the passive, this weapon can perform better than Skyward Blade, while at lower refines / less stacks, it can perform worse.",
                    "Lion's Roar: Depending on passive uptime, it can be ranked much higher in terms of Jean's personal damage.",
                    "",
                    "Regarding Artifact Sets:",
                    "Viridescent Venerer (4): The bread and butter for Anemo characters in general, as it is commonly used for the 40% elemental resistance shred.",
                    "Noblesse Oblige (4): Another option for providing utilities to the team. This set gives a 20% partywide ATK boost after Jean casts her Elemental Burst.",
                    "Ocean-Hued Clam (4): The best set for Jean's personal damage, as the damage it deals scales with Jean's burst healing. However, because Jean's total damage output is on the low end, it is generally recommended to prioritize utility options such as Noblesse Oblige (4) or Viridescent Venerer (4) over this set.",
                    "",
                    "Regarding Main Stats Priority:",
                    "While typically Jean will heal enough that you do not need to try and build for as much healing as possible, when paired with Furina it can be beneficial swapping to an ATK% goblet and Healing Bonus circlet. This is to aid in building Fanfare points faster, and Jean's personal damage is not particularly significant to begin with. When building Jean in such a way, prioritize weapons which provide ATK% or Energy Recharge. If using Favonius Sword, a Crit Rate circlet can be taken to ensure more consistent procs.",
                    "",
                    "Regarding Talent Priorities:",
                    "If you prefer more damage than healing, prioritize Elemental Skill over Elemental Burst since it scales better.",
                    "For Support Jean, you can either go for more ATK for stronger heals, but relatively lower Burst uptime, or more ER for lower heals, but higher Burst uptime. Choosing between these two is up to personal preference, although if another Anemo character is on the team, Jean has very few energy problems and can potentially go for a full Sub DPS build.",
                    "",
                    "REACTION DPS",
                    "Reaction DPS Jean relies on her unique interaction regarding her Elemental Burst. If the active character if afflicted by Hydro / Pyro / Electro / Cryo, Jean's Burst will infuse them with Anemo and create a swirl trigger around the character. This interaction can be abused by using Bennett to consistently infuse the active character with Pyro. This allows for an extremely high amount of Pyro Swirl triggers. These swirl's damage scales off of Jean's Elemental Mastery.",
                )
            ),
        )


class Venti(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="VENTI"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Venti")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "OFF-FIELD DPS",
                    "Venti is a potent Off-Field DPS who can buff teammates through Viridescent Venerer, or buff Anemo teammates through his Hexerei passive. With the addition of his Hexerei talents, he is no longer a Reaction-Based Off-Field DPS, although the playstyle is still utilized in some teams.",
                    "",
                    "Regarding Weapon Choices:",
                    "The First Great Magic: With three Gimmick stacks, this weapon performs better than Astral Vulture's Crimson Plumage.",
                    "Mouun's Moon: At [R5], this weapon ranks similarly to Hunter's Path.",
                    "Song of Stillness: ranked under the assumption that Venti is healed, thus activating its passive.",
                    "",
                    "Detailed weapon comparison https://docs.google.com/spreadsheets/d/1fNEp15Fyj6gkJBmG0hW_bLhza-1Bm9zx6n0K3VNW4ZA/edit?usp=sharing.",
                    "",
                    "ON-FIELD DPS",
                    "Venti, when paired with another Hexerei character, can be used as a strong, Normal-attacking, On-Field DPS who has large amounts of damage from multiple sources.",
                    "",
                    "Regarding Weapon Choices:",
                    "Astral Vulture's Crimson Plumage: If there are three unique Elements on the team, this weapon ranks similarly to Thundering Pulse.",
                    "The First Great Magic: Assumes two stacks of the passive are active.",
                    "Song of Stillness: ranked under the assumption that Venti is healed, thus activating its passive.",
                    "Rust: At [R5] this weapon performs better than Amos' Bow.",
                    "",
                    "Regarding Artifact Sets:",
                    "Desert Pavillion Chronicle (4): Requires Venti to perform a quick Charged Attack at the beginning of his combo.",
                    "Echoes of an Offering (4): Loses value if you have high ping (>100).",
                    "Viridescent Venerer (4): Gains value if there are Pyro/Hydro/Electro/Cryo units that deal significant damage on the team.",
                    "",
                    "Detailed weapon comparison https://docs.google.com/spreadsheets/d/1fQcQ0WTt7bNE4C1DnqlpBJWLI6T2pfXh1BEhK8xynqc/edit?usp=sharing.",
                )
            ),
        )


class Xiao(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="XIAO"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Xiao")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "DPS",
                    "Xiao is a Hypercarry that is centered around plunge attacks. Due to his expensive elemental burst, Xiao usually requires a high amount of Energy Recharge and/or at least one Anemo battery (Sucrose, C6 Faruzan, Xianyun) on his team to help him recharge his burst.",
                    "",
                    "Regarding Weapon Choices:",
                    "Calamity Queller: In Teams with neither Bennett nor Xianyun, this weapon increases in value.",
                    "Crimson Moon's Semblance: While generally just a stat stick for the high base attack and Crit Rate substat, this weapon's passive can be utilized in teams with no or only Bennett's healing by performing a charged attack at the start of Xiao's burst.",
                    "Vortex Vanquisher: Assumes no shield on the team. In teams with a shield or without Xianyun or Bennett, this weapon performs slightly better.",
                    "Skyward Spine and Favonius Lance: These weapons become significantly better choices in teams with very high Energy Recharge Requirements.",
                    "Blackcliff Pole: In Teams with Bennett, this weapon performs similar to Calamity Queller. This weapon's passive is generally unreliable, but can lead to a slightly higher ranking when applicable.",
                    "Lithic Spear: This Ranking assumes 1 Stack. This weapon's performance varies greatly with refines and stacks. At [R5], this weapon performs similar to Blackcliff Pole with one stack and Calamity Queller with two stacks.",
                    "Missive Windspear [R5]: If Xiao can reliably trigger this weapon's passive, it performs closer to Blackcliff Pole.",
                    "Prospector's Drill: At [R5], this weapon performs similar to Skyward Spine given a reliable healer is present.",
                    "",
                    "Regarding Artifact Sets:",
                    "Marechaussee Hunter (4): This set pulls ahead of Vermillion Hereafter (4) with either Bennett or Xianyun on the Team. This set is hard to build around when using a Crit Rate Weapon, making other sets a better overall choice.",
                    "Long Night's Oath (4): While being a strong alternative to similar ranking sets, it is not recommended to farm this set currently as it combines an inefficient domain with a team- and skill- dependent damage performance.",
                    "Desert Pavilion Chronicle (4): Perform a charged attack at the start of Xiao's burst to utilize this set fully. With a low base attack weapon and Bennett on the team, this set performs close to Vermillion Hereafter (4). It is not recommended to farm this Domain specifically for Xiao.",
                    "",
                    "Detailed comparisons https://docs.google.com/spreadsheets/d/1AFQiNYl4ehha9WP986hgqaBDtSwuE7Gcu3xMf9vX8nc/edit?gid=848665920#gid=848665920.",
                )
            ),
        )


class KaedeharaKazuha(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="KAEDEHARA KAZUHA"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Kaedehara Kazuha")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "REACTION DPS & SUPPORT",
                    "Kazuha's 4th ascension passive provides an elemental DMG bonus buff depending on his Elemental Mastery, putting the main focus on his build on stacking Elemental Mastery while also having enough Energy Recharge to burst every rotation, as his burst extends the duration of his passive and deals respectable damage through swirls.",
                    "",
                    "Regarding Weapon Choices:",
                    "Favonius Sword: With this weapon, try to aim for some Crit Rate stats to trigger the weapon passive reliably.",
                    "Xiphos' Moonlight: At [R1], this weapon usually performs worse than Favonius Sword due to providing less effective energy to the team. At higher refinements, this weapon can rival Freedom-Sworn in terms of value due to how much Energy Recharge it provides to Kazuha and the team.",
                    "Sacrificial Sword: This weapon is mainly used for the Energy Recharge it provides. The skill reset should not be used unless the extra grouping is needed.",
                    "Iron Sting and Toukabou Shigure: These weapons can perform better than Sacrificial Sword if you can get enough Energy Recharge from substats.",
                    "",
                    "Regarding Artifact Sets:",
                    "Thundering Fury (4): This set is only used for a few specific teams, in which Kazuha is used on field to deal damage through aggravated swirl hits.",
                )
            ),
        )


class Wanderer(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="WANDERER"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Wanderer")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "DPS",
                    "External Buffs means the existence of a unit that provides ATK, or makes ATK less necessary (e.g. Bennett, Yun Jin)",
                    "Wanderer focuses on doing damage by activating his elemental skill and performing boosted normal attacks. It should be noted that in this state, he does not have knockback resistance so a shielder or other form of knockback immunity is recommended. It is not worth building ER to burst every rotation unless Wanderer is C2. Instead, bursting every other rotation is preferred.",
                    "",
                    "Regarding Weapon Choices:",
                    "Memory of Dust: This weapon can pull farther ahead than other options if Wanderer is shielded. If shielded, it maintains its ranking without Bennett, and performs better than The Widsith with Bennett.",
                    "Dodoco Tales [R5]: This weapon uses a different rotation of E N1 CAx6 N1 CAx6 to maximize its passive.",
                    "The Widsith: Because Wanderer doesn't focus on Swirl damage, this weapon can be inconsistent if you get the EM buff.",
                    "",
                    "Regarding Artifact Sets:",
                    "Shimenawa's Reminiscence (4): If Wanderer is [C2] or higher it is not recommended to run this set.",
                    "Echoes of an Offering (4): If your ping is above 100, it is not recommended to run this set specifically",
                    "Blizzard Strayer (4): This set synergizes well with the 20% Crit Rate that Wanderer gets from swirling Cryo. It is only recommended if you have close to 100% uptime on Freeze, which requires very specific teams. Despite this, with 100% Freeze uptime, this set is still worse than Desert Pavilion Chronicle (4).",
                    "Lavawalker (4): In teams with consistent Pyro application, this set is about equal to Echoes of an Offering (4).",
                    "Viridescent Venerer (4): In teams where the majority of the damage share is not linked to Wanderer, and there is no other viable holder of the set, he may use Viridescent Venerer (4).",
                )
            ),
        )


class Xianyun(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="XIANYUN"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Xianyun")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "PLUNGE ATTACK SUPPORT",
                    "Xianyun's main utilities are her jump height boost, healing, and Plunging Attack buff. While her healing is tied to her Burst Levels, the only way to increase her Plunging Attack buff is by increasing her total ATK.",
                    "",
                    "Regarding Weapon Choices:",
                    "Favonius Codex: With high team Energy Recharge Requirements, this weapon pulls ahead in value.",
                    "Hakushin Ring: In teams with Electro units to benefit from the passive, this weapon ranks higher than Ballad of the Boundless Blue.",
                    "Thrilling Tales of Dragon Slayers: The value of this weapon depends on who and how reliably they can obtain the buff.",
                    "Prototype Amber: At low refinements, this weapon is not worth using. The lower Xianyun's total Energy Recharge requirements, the worse this weapon performs. At [R5] this weapon is similar or better than Ballad of the Boundless Blue.",
                    "Wine and Song: Perform a dash to gain the ATK% from the passive.",
                    "",
                    "Regarding Artifact Sets:",
                    "Noblesse Oblige (4): Better than Viridescent Venerer if someone else already has the set or if Pyro/Hydro/Cryo/Electro damage is not a large source of the team's damage.",
                    "Ocean Hued Clam (4) / Song of Days Past (4): In Single Target scenarios, Song of Days Past can be better than Ocean Hued Clam. However, Clam is more consistent.",
                    "",
                    "Detailed comparisons https://drive.google.com/drive/folders/1ZXdPL0sMQe9MFmLO7TKnWf_8nksU5_8m?usp=sharing.",
                )
            ),
        )


class Chasca(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="CHASCA"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Chasca")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "DPS",
                    "Chasca is a DPS that focuses on dealing damage through her converted Shining Shadowhunt Shells. Her Anemo damage is considerably low, therefore she is best played with multiple different PHEC (Pyro/Hydro/Electro/Cryo) elements present on the team to enable reactions and convert as many Shells as possible.",
                    "",
                    "Regarding Weapon Choices:",
                    "Amos' Bow: As Chasca's Shining Shadowhunt Shells are not a projectile and therefore have no travel time, she does not benefit from any stacks of this weapon's passive. It is still a good Stat stick nonetheless.",
                    "Polar Star: In theory, this weapon performs slightly better than Amos' Bow. However, due to its high Crit Rate substat, optimizing builds around this weapon is very hard.",
                    "Scion of the Blazing Sun: At [R5], this weapon performs close to Skyward Harp.",
                    "Song of Stillness: Assumes permanent uptime on the passive. If the team cannot provide frequent heals, this weapon should not be considered.",
                    "Flower-Wreathed Feathers: At [R5], this weapon performs similarly to Skyward Harp.",
                    "Range Gauge: This weapon needs reliable healing to perform well. With frequent, guaranteed healing instances, this weapon performs slightly better than Song of Stillness [R5], and slightly better than Amos' Bow at [R5].",
                    "",
                    "Regarding Artifact Sets:",
                    "Marechaussee Hunter (4): Only useful when paired with Furina, in which case it performs very close to Obsidian Codex (4).",
                    "",
                    "Detailed comparisons https://docs.google.com/spreadsheets/d/1xMap4jlIkmUC3pfykrE89RvqqxcLOrwclSvm2OzV19g/edit?usp=sharing.",
                )
            ),
        )


class YumemizukiMizuki(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="YUMEMIZUKI MIZUKI"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Yumemizuki Mizuki")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "REACTION DPS",
                    "Yumemizuki Mizuki is a driver that focuses on enhancing and triggering the swirl reaction. Her only needed stats are Elemental Mastery, to strengthen her swirl buff as well as swirl damage, and Energy Recharge to be able to use her Burst every rotation for healing and more swirls.",
                    "",
                    "Regarding Weapon Choices:",
                    "Favonius Codex: A good choice in solo Anemo teams or teams with overall high Energy Recharge requirements.",
                    "Hakushin Ring: This weapon should only be used if there is an Electro DPS on the team.",
                    "Wandering Evenstar: This weapon is a great option if the team can use the attack buff. At higher refines, this weapon performs better than Sacrificial Fragments.",
                )
            ),
        )


class Varka(TestCase):
    img: Tag

    @classmethod
    def setUpClass(cls):
        name = cast(NavigableString, _soup.find(string="VARKA"))
        cls.img = cast(Tag, name.find_next("img"))
        cls.maxDiff = None

    def test_is_5_star(self):
        self.assertTrue(is_character_5_star(self.img))

    def test_get_character_name(self):
        self.assertEqual(get_character_name(self.img), "Varka")

    def test_get_character_notes(self):
        self.assertEqual(
            get_character_notes(self.img),
            "\n".join(
                (
                    "DPS",
                    "Varka is a dual element wielding DPS who adapts his weapon based on your team.",
                    "",
                    "Regarding Weapon Choices:",
                    "Song of Broken Pines: This weapon's performance is highly reliant on using the attack speed buff. If you are having issues with combo execution in general, this weapon is not recommended",
                    "Serpent Spine: At [R5], this weapon performs similar to Verdict.",
                    "Fang of the Mountain King: With this weapon, it is recommended to use Varka's special Skill instead of the special Charged Attack.",
                    "Tidal Shadow: Assumes Varka is healed to activate the passive. As this is not feasible in his current best teams, this weapon can quickly fall to the bottom of this list.",
                    "Talking Stick: Assumes the Pyro passive being active. At [R5], this weapon performs similarly to Fang of the Mountain King.",
                    '"Ultimate Overlord\'s Mega Magic Sword": While Energy Recharge is a useless stat for Varka, this weapon is one of the few accessible options that are actually reliable.',
                    "",
                    "Detailed Calculations can be found https://docs.google.com/spreadsheets/d/104igYmPqjx13P5cNdQ97r10ok-n1nyBRrtwTHN6U4Bs/edit?usp=sharing.",
                )
            ),
        )
