from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import os

RACES = (
    ("human", "Human"),
    ("dwarf", "Dwarf"),
    ("elf", "Elf"),
    ("halfling", "Halfling"),
)

GENDERS = (
    ("male", "Male"),
    ("female", "Female"),
)

CAREERS = (
    ("agitator", "Agitator"), ("apprentice_wizard", "Apprentice Wizard"), ("bailiff", "Bailiff"),
    ("barber-surgeon", "Barber-Surgeon"), ("boatman", "Boatman"), ("bodyguard", "Bodyguard"),
    ("bone_picker", "Bone Picker"), ("bounty_hunter", "Bounty Hunter"), ("burgher", "Burgher"),
    ("camp_follower", "Camp Follower"), ("charcoal-burner", "Charcoal-Burner"), ("coachman", "Coachman"),
    ("entertainer", "Entertainer"), ("envoy", "Envoy"), ("estalian_diestro", "Estalian Diestro"),
    ("ferryman", "Ferryman"), ("fieldwarden", "Fieldwarden"), ("fisherman", "Fisherman"),
    ("grave_robber", "Grave Robber"), ("hedge_wizard", "Hedge Wizard"), ("hunter", "Hunter"),
    ("initiate", "Initiate"), ("jailer", "Jailer"), ("kislevite_kossar", "Kislevite Kossar"),
    ("kithband_warrior", "Kithband Warrior"), ("marine", "Marine"), ("mercenary", "Mercenary"),
    ("messenger", "Messenger"), ("militiaman", "Militiaman"), ("miner", "Miner"), ("noble", "Noble"),
    ("norse_berserker", "Norse Berserker"), ("outlaw", "Outlaw"), ("outrider", "Outrider"),
    ("peasant", "Peasant"), ("pit_fighter", "Pit Fighter"), ("protagonist", "Protagonist"),
    ("rat_catcher", "Rat Catcher"), ("roadwarden", "Roadwarden"), ("rogue", "Rogue"),
    ("runebearer", "Runebearer"), ("scribe", "Scribe"), ("seaman", "Seaman"), ("servant", "Servant"),
    ("shieldbreaker", "Shieldbreaker"), ("smuggler", "Smuggler"), ("soldier", "Soldier"),
    ("squire", "Squire"), ("student", "Student"), ("thief", "Thief"), ("thug", "Thug"),
    ("toll_keeper", "Toll Keeper"), ("tomb_robber", "Tomb Robber"), ("tradesman", "Tradesman"),
    ("troll_slayer", "Troll Slayer"), ("vagabond", "Vagabond"), ("valet", "Valet"),
    ("watchman", "Watchman"), ("woodsman", "Woodsman"), ("zealot", "Zealot")
)

def portrait_path(instance, filename):
    return 'portraits/{0}/{1}'.format(instance.id, filename)

class Hero(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=32, blank=True, null=True)
    race = models.CharField(max_length=16, choices=RACES, default="Human")
    current_career = models.CharField(max_length=32, choices=CAREERS, default="Mercenary")
    previous_careers = models.CharField(max_length=32, null=True, blank=True)
    age = models.SmallIntegerField(null=True, blank=True)
    gender = models.CharField(choices=GENDERS, max_length=16, default="Male")
    # unimportant
    eye_color = models.CharField(max_length=16, null=True, blank=True)
    hair_color = models.CharField(max_length=16, null=True, blank=True)
    weight = models.SmallIntegerField(null=True, blank=True)
    height = models.SmallIntegerField(null=True, blank=True)
    star_sign = models.CharField(max_length=32, null=True, blank=True)
    number_of_siblings = models.SmallIntegerField(null=True, blank=True)
    birthplace = models.CharField(max_length=32, null=True, blank=True)
    distinguishing_marks = models.CharField(max_length=32, null=True, blank=True)
    # stats
    weapon_skill = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    ballistic_skill = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    strength = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    toughness = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    agility = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    intelligence = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    will_power = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    fellowship = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=20)
    attacks = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    wounds = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=5)
    strength_bonus = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    toughness_bonus = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    movement = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=1)
    magic = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default=0)
    insanity_points = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    fate_points = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], default=0)
    # functionalities
    user = models.ForeignKey(User, related_name='player', on_delete=models.CASCADE, blank=True, null=True)
    game_master = models.ForeignKey(User, related_name='game_master',  on_delete=models.CASCADE, blank=True, null=True)
    experience = models.SmallIntegerField(default=0)
    portrait = models.ImageField(upload_to=portrait_path, default='portraits/default.jpg',
                                blank=True, null=True)


class News(models.Model):
    title = models.CharField(max_length=32, default="News")
    content = models.TextField(null=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    added_by = models.ForeignKey(User, related_name='added_by', on_delete=models.CASCADE)
    category = models.CharField(max_length=32, blank=True, null=True)
    picture = models.ImageField(upload_to='news/%Y/%m/%d', default='news/default.jpg',
                                blank=True, null=True)
