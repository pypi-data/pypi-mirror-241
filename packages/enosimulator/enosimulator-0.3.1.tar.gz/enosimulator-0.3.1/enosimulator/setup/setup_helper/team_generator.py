from typing import Dict, List, Tuple

from aenum import extend_enum

from ...types_ import Config, Experience, Team
from .util import analyze_scoreboard_file

TEAM_NAMES = [
    "Edible Frog",
    "Jonah Crab",
    "English Cream Golden Retriever",
    "Vampire Squid",
    "Bolognese Dog",
    "Abyssinian Guinea Pig",
    "Eastern Racer",
    "Keta Salmon",
    "Korean Jindo",
    "Baiji",
    "Common Spotted Cuscus",
    "Indian python",
    "Kooikerhondje",
    "Gopher Tortoise",
    "Kamehameha Butterfly",
    "X-Ray Tetra",
    "Dodo",
    "Rainbow Shark",
    "Chihuahua Mix",
    "Flounder Fish",
    "Hooded Oriole",
    "Bed Bug",
    "Pacific Spaghetti Eel",
    "Yak",
    "Madagascar Hissing Cockroach",
    "Petite Goldendoodle",
    "Teacup Miniature Horse",
    "Arizona Blonde Tarantula",
    "Aye-Aye",
    "Dorking Chicken",
    "Elk",
    "Xenoposeidon",
    "Urutu Snake",
    "Hamburg Chicken",
    "Thorny Devil",
    "Venus Flytrap",
    "Fancy Mouse",
    "Lawnmower Blenny",
    "NebelungOrb Weaver",
    "Quagga",
    "Woolly Rhinoceros",
    "Radiated Tortoise",
    "De Kay's Brown Snake",
    "Red-Tailed Cuckoo Bumble Bee",
    "Japanese Bantam Chicken",
    "Irukandji Jellyfish",
    "Dogue De Bordeaux",
    "Bamboo Shark",
    "Peppered Moth",
    "German Cockroach",
    "Vestal Cuckoo Bumble Bee",
    "Ovenbird",
    "Irish Elk",
    "Southeastern Blueberry Bee",
    "Modern Game Chicken",
    "Onagadori Chicken",
    "LaMancha Goat",
    "Dik-Dik",
    "Quahog Clam",
    "Jack Russells",
    "Assassin Bug",
    "Upland Sandpiper",
    "Nurse Shark",
    "San Francisco Garter Snake",
    "Zebu",
    "New Hampshire Red Chicken",
    "False Water Cobra",
    "Earless Monitor Lizard",
    "Chicken Snake",
    "Walking Catfish",
    "Gypsy Cuckoo Bumble Bee",
    "Immortal Jellyfish",
    "Zorse",
    "Xerus",
    "Macaroni Penguin",
    "Taco Terrier",
    "Lone Star Tick",
    "Crappie Fish",
    "Yorkiepoo",
    "Lemon Cuckoo Bumble Bee",
    "Amano Shrimp",
    "German Wirehaired Pointer",
    "Cabbage Moth",
    "Huskydoodle",
    "Forest Cuckoo Bumble Bee",
    "Old House Borer",
    "Hammerhead Worm",
    "Striped Rocket Frog",
    "Zonkey",
    "Fainting Goat",
    "White Crappie",
    "Quokka",
    "Banana Eel",
    "Goblin Shark",
    "Umbrellabird",
    "Norwegian Elkhound",
    "Yabby",
    "Midget Faded Rattlesnake",
    "Pomchi",
    "Jack-Chi",
    "Herring",
]


class TeamGenerator:
    """
    Generates unique teams for the simulation.

    The distribution of experience levels differs depending on the simulation type.

    For basic-stress-test, there is only one team with the experience level HAXXOR.
    For stress-test and intensive-stress-test, there are as many teams with the experience level HAXXOR as there are teams in total.
    For all other simulation types, the distribution of experience levels is based on the number of teams and the experience distribution parameters derived from the analyze_scoreboard_file function.

    Attributes:
        config (Config): The configuration file provided by the user.
        team_distribution (Dict): A dictionary mapping experience levels to the number of teams with that experience level.
    """

    def __init__(self, config: Config):
        """
        Initialize the TeamGenerator class.

        If a scoreboard file is provided in the configuration, the team experience
        distribution will be derived from the scoreboard file. Otherwise, the team
        experience will be set according to default values returned by the
        analyze_scoreboard_file function.
        """

        experience_distribution = analyze_scoreboard_file(
            config.settings.scoreboard_file
        )
        try:
            for experience, distribution in experience_distribution.items():
                extend_enum(Experience, experience, distribution)
        except Exception:
            pass

        self.config = config
        if self.config.settings.simulation_type == "basic-stress-test":
            self.team_distribution = {Experience.HAXXOR: 1}

        elif self.config.settings.simulation_type in (
            "stress-test",
            "intensive-stress-test",
        ):
            self.team_distribution = {Experience.HAXXOR: self.config.settings.teams}

        else:
            self.team_distribution = {
                experience: int(experience.value[1] * self.config.settings.teams)
                for experience in [
                    Experience.NOOB,
                    Experience.BEGINNER,
                    Experience.INTERMEDIATE,
                    Experience.ADVANCED,
                    Experience.PRO,
                ]
            }

            while sum(self.team_distribution.values()) < self.config.settings.teams:
                self.team_distribution[Experience.NOOB] += 1
            while sum(self.team_distribution.values()) > self.config.settings.teams:
                self.team_distribution[Experience.NOOB] -= 1

    def generate(self) -> Tuple[List, Dict]:
        """
        Generate teams for the simulation.

        Returns:
            A tuple containing:
                - A list of teams that will be used to generate a ctf.json file for the engine
                - A dictionary mapping team names to Team objects containing the team's information.
        """

        ctf_json_teams = []
        setup_teams = dict()
        team_id_total = 0

        for experience, teams in self.team_distribution.items():
            for team_id in range(1, teams + 1):
                ctf_json_teams.append(self._generate_ctf_team(team_id_total + team_id))
                setup_teams.update(
                    self._generate_setup_team(team_id_total + team_id, experience)
                )
            team_id_total += teams

        return ctf_json_teams, setup_teams

    def _generate_ctf_team(self, id: int) -> Dict:
        """
        Generate a team for the ctf.json file.

        Args:
            id (int): The id of the team.

        Returns:
            A dictionary containing the team's information.
        """

        name = TEAM_NAMES[id - 1] if id <= len(TEAM_NAMES) else f"Team {id}"
        new_team = {
            "id": id,
            "name": name,
            "teamSubnet": "::ffff:<placeholder>",
            "address": "<placeholder>",
        }
        return new_team

    def _generate_setup_team(self, id: int, experience: Experience) -> Dict[str, Team]:
        """
        Generate a team for the setup.

        Args:
            id (int): The id of the team.
            experience (Experience): The experience level of the team.

        Returns:
            A dictionary mapping the team's name to a Team object containing the team's information.
        """

        name = TEAM_NAMES[id - 1] if id <= len(TEAM_NAMES) else f"Team {id}"
        new_team = {
            TEAM_NAMES[id - 1]: Team(
                id=id,
                name=name,
                team_subnet="::ffff:<placeholder>",
                address="<placeholder>",
                experience=experience,
                exploiting=dict(),
                patched=dict(),
                points=0.0,
                gain=0.0,
            )
        }
        return new_team
