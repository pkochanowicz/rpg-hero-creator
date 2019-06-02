from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, validate_email
from .models import Hero

# warhammer hero creation forms


def	validate_age(value):
    if value < 16 or value > 200:
        raise ValidationError("Wrong age")


def	validate_weight(value):
    if value < 30 or value > 150:
        raise ValidationError("Wrong weight")


def	validate_height(value):
    if value < 80 or value > 200:
        raise ValidationError("Wrong height")


def	validate_experience_assignment(value):
    if value < 1 or value > 2000:
        raise ValidationError("You have to assign a number between 1 and 2000")


def	validate_positive(value):
    if value < 0:
        raise ValidationError("Must be a positive number")


def validate_if_user_exists(user_name):
    if user_name != "":
        try:
            user = User.objects.get(username=user_name)
        except:
            raise ValidationError("There is no such user")


class HeroCreationCharacterForm(forms.Form):
    name = forms.CharField(label='Hero name', max_length=32)
    game_master_name = forms.CharField(label="Game master user name (leave empty if you don't want to assign one)",
                                       validators=[validate_if_user_exists],
                                       required=False)
    race = forms.ChoiceField(choices=(("human", "Human"),
                                      ("dwarf", "Dwarf"),
                                      ("elf", "Elf"),
                                      ("halfling", "Halfling"),))
    gender = forms.ChoiceField(choices=(("male", "Male"),
                                        ("female", "Female"),))
    current_career = forms.ChoiceField(choices=(
        ("agitator", "Agitator"), ("apprentice_wizard", "Apprentice Wizard"), ("bailiff", "Bailiff"),
        ("barber-surgeon", "Barber-Surgeon"), ("boatman", "Boatman"), ("bodyguard", "Bodyguard"),
        ("bone_picker", "Bone Picker"), ("bounty_hunter", "Bounty Hunter"), ("burgher", "Burgher"),
        ("camp_follower", "Camp Follower"), ("charcoal-burner", "Charcoal-Burner"),  ("coachman", "Coachman"),
        ("entertainer", "Entertainer"),  ("envoy", "Envoy"),  ("estalian_diestro", "Estalian Diestro"),
        ("ferryman", "Ferryman"), ("fieldwarden", "Fieldwarden"),  ("fisherman", "Fisherman"),
        ("grave_robber", "Grave Robber"),  ("hedge_wizard", "Hedge Wizard"),  ("hunter", "Hunter"),
        ("initiate", "Initiate"), ("jailer", "Jailer"),  ("kislevite_kossar", "Kislevite Kossar"),
        ("kithband_warrior", "Kithband Warrior"),  ("marine", "Marine"),  ("mercenary", "Mercenary"),
        ("messenger", "Messenger"),  ("militiaman", "Militiaman"),  ("miner", "Miner"),  ("noble", "Noble"),
        ("norse_berserker", "Norse Berserker"),  ("outlaw", "Outlaw"),  ("outrider", "Outrider"),
        ("peasant", "Peasant"),  ("pit_fighter", "Pit Fighter"),  ("protagonist", "Protagonist"),
        ("rat_catcher", "Rat Catcher"),  ("roadwarden", "Roadwarden"),  ("rogue", "Rogue"),
        ("runebearer", "Runebearer"),  ("scribe", "Scribe"),  ("seaman", "Seaman"),  ("servant", "Servant"),
        ("shieldbreaker", "Shieldbreaker"),  ("smuggler", "Smuggler"),  ("soldier", "Soldier"),
        ("squire", "Squire"),  ("student", "Student"),  ("thief", "Thief"),  ("thug", "Thug"),
        ("toll_keeper", "Toll Keeper"),  ("tomb_robber", "Tomb Robber"),  ("tradesman", "Tradesman"),
        ("troll_slayer", "Troll Slayer"),  ("vagabond", "Vagabond"),  ("valet", "Valet"),
        ("watchman", "Watchman"),  ("woodsman", "Woodsman"),  ("zealot", "Zealot"),
    ))


class HeroCreationPersonalDetailsForm(forms.Form):
    previous_careers = forms.CharField(label='Previous careers', max_length=32, required=False)
    age = forms.IntegerField(label="Age", validators=[validate_age], required=False)
    eye_color = forms.CharField(label='Eye color', max_length=16, required=False)
    hair_color = forms.CharField(label='Hair color', max_length=16, required=False)
    weight = forms.IntegerField(label='Weight', validators=[validate_weight], required=False)
    height = forms.IntegerField(label='Height', validators=[validate_height], required=False)
    star_sign = forms.CharField(label='Star sign', max_length=32, required=False)
    number_of_siblings = forms.IntegerField(label='Number of siblings', validators=[validate_positive], required=False)
    birthplace = forms.CharField(label='Birthplace', max_length=32, required=False)
    distinguishing_marks = forms.CharField(label="Distinguishing marks", max_length=32, required=False)


class HeroCreationCharacterProfileForm(forms.Form):
    weapon_skill = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    ballistic_skill = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    strength = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    toughness = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    agility = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    intelligence = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    will_power = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fellowship = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    attacks = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    wounds = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    strength_bonus = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    toughness_bonus = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    movement = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    magic = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    insanity_points = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fate_points = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], widget=forms.TextInput(attrs={'readonly':'readonly'}))
    portrait_file = forms.ImageField(label='Portrait', required=False)

class HeroSearchForm(forms.Form):
    name = forms.CharField(label='Hero name', max_length=32, required=False)
    race = forms.ChoiceField(choices=(("", "Any"),
                                      ("human", "Human"),
                                      ("dwarf", "Dwarf"),
                                      ("elf", "Elf"),
                                      ("halfling", "Halfling")), required=False)
    gender = forms.ChoiceField(choices=(("", "Any"),
                                        ("male", "Male"),
                                        ("female", "Female"),), required=False)
    current_career = forms.CharField(label='Current career', max_length=32, required=False)


class AssignExperienceForm(forms.Form):
    hero = forms.ModelChoiceField(queryset=Hero.objects.filter(game_master=1))
    experience = forms.IntegerField(label="How much experience would you like to assign?",
                                    validators=[validate_experience_assignment])

    def __init__(self, user, *args, **kwargs):
        super(AssignExperienceForm, self).__init__(*args, **kwargs)
        self.fields['hero'].queryset = Hero.objects.filter(game_master=user)


class GameMasterEditForm(forms.Form):
    game_master_name = forms.CharField(label='New game master user name',
                                       validators=[validate_if_user_exists])


class AddNewsForm(forms.Form):
    title = forms.CharField(label='News title', max_length=32)
    content = forms.CharField(label='Content:', widget=forms.Textarea)
    picture = forms.ImageField(label='Picture', required=False)
