from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from .forms import HeroCreationCharacterForm, HeroCreationPersonalDetailsForm, \
    HeroCreationCharacterProfileForm, HeroSearchForm, GameMasterEditForm, \
    AssignExperienceForm, AddNewsForm
from .models import Hero, News


class HeroCreationView(View):
    def get(self, request):
        character_form = HeroCreationCharacterForm
        personal_details_form = HeroCreationPersonalDetailsForm
        character_profile_form = HeroCreationCharacterProfileForm
        return render(request, 'warhammer_hero_creation.html', {"character_form": character_form,
                                                                "personal_details_form": personal_details_form,
                                                                "character_profile_form": character_profile_form
                                                                })

    @method_decorator(login_required)
    def post(self, request):
        character_form = HeroCreationCharacterForm(request.POST)
        personal_details_form = HeroCreationPersonalDetailsForm(request.POST)
        character_profile_form = HeroCreationCharacterProfileForm(request.POST)
        if character_form.is_valid() & personal_details_form.is_valid() & character_profile_form.is_valid():
            # character form:
            name = character_form.cleaned_data['name']
            race = character_form.cleaned_data['race']
            gender = character_form.cleaned_data['gender']
            current_career = character_form.cleaned_data['current_career']
            # personal details form:
            previous_careers = personal_details_form.cleaned_data['previous_careers']
            age = personal_details_form.cleaned_data['age']
            eye_color = personal_details_form.cleaned_data['eye_color']
            hair_color = personal_details_form.cleaned_data['hair_color']
            weight = personal_details_form.cleaned_data['weight']
            height = personal_details_form.cleaned_data['height']
            star_sign = personal_details_form.cleaned_data['star_sign']
            number_of_siblings = personal_details_form.cleaned_data['number_of_siblings']
            birthplace = personal_details_form.cleaned_data['birthplace']
            distinguishing_marks = personal_details_form.cleaned_data['distinguishing_marks']
            # character profile form:
            weapon_skill = character_profile_form.cleaned_data['weapon_skill']
            ballistic_skill = character_profile_form.cleaned_data['ballistic_skill']
            strength = character_profile_form.cleaned_data['strength']
            toughness = character_profile_form.cleaned_data['toughness']
            agility = character_profile_form.cleaned_data['agility']
            intelligence = character_profile_form.cleaned_data['intelligence']
            will_power = character_profile_form.cleaned_data['will_power']
            fellowship = character_profile_form.cleaned_data['fellowship']
            attacks = character_profile_form.cleaned_data['attacks']
            wounds = character_profile_form.cleaned_data['wounds']
            strength_bonus = character_profile_form.cleaned_data['strength_bonus']
            toughness_bonus = character_profile_form.cleaned_data['toughness_bonus']
            movement = character_profile_form.cleaned_data['movement']
            magic = character_profile_form.cleaned_data['magic']
            insanity_points = character_profile_form.cleaned_data['insanity_points']
            fate_points = character_profile_form.cleaned_data['fate_points']
            user = request.user
            new_hero = Hero.objects.create(
                name=name,
                race=race,
                gender=gender,
                current_career=current_career,
                previous_careers=previous_careers,
                age=age,
                eye_color=eye_color,
                hair_color=hair_color,
                weight=weight,
                height=height,
                star_sign=star_sign,
                number_of_siblings=number_of_siblings,
                birthplace=birthplace,
                distinguishing_marks=distinguishing_marks,
                weapon_skill=weapon_skill,
                ballistic_skill=ballistic_skill,
                strength=strength,
                toughness=toughness,
                agility=agility,
                intelligence=intelligence,
                will_power=will_power,
                fellowship=fellowship,
                attacks=attacks,
                wounds=wounds,
                strength_bonus=strength_bonus,
                toughness_bonus=toughness_bonus,
                movement=movement,
                magic=magic,
                insanity_points=insanity_points,
                fate_points=fate_points,
                user=user
            )
            game_master_name = character_form.cleaned_data['game_master_name']
            if game_master_name != "":
                game_master = User.objects.get(username=game_master_name)
                new_hero.game_master = game_master
            if request.FILES['portrait_file']:
                new_hero.portrait = request.FILES['portrait_file']
            new_hero.save()
            return redirect("/warhammer/hero/{}".format(new_hero.id))
        else:
            message = str("Wrong data. The news hasn't been created.")
            return render(request, 'warhammer_hero_creation.html', {"character_form": character_form,
                                                                    "personal_details_form": personal_details_form,
                                                                    "character_profile_form": character_profile_form,
                                                                    "message": message})


class HeroView(View):
    @method_decorator(login_required)
    def get(self, request, hero_id):
        game_master_form = GameMasterEditForm
        hero = Hero.objects.get(id=hero_id)
        hero.current_career = hero.current_career.replace('_', ' ')
        return render(request, "warhammer_hero.html", {"hero": hero,
                                                       "game_master_form": game_master_form})

    # def post(self, request, hero_id):
    #     form = GameMasterEditForm(request.Post)
    #     if form.is_valid():
    #         game_master_name = form.cleaned_data['game_master_name']
    #         game_master = User.objects.get(username=game_master_name)
    #         hero = Hero.objects.get(id=hero_id)
    #         hero.game_master = game_master


class HeroesSearchAndView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = HeroSearchForm
        user_heroes = Hero.objects.filter(user=request.user)
        game_master_heroes = Hero.objects.filter(game_master=request.user)
        return render(request, "warhammer_heroes.html", {"user_heroes": user_heroes,
                                                         "game_master_heroes": game_master_heroes,
                                                         "form": form})

    @method_decorator(login_required)
    def post(self, request):
        form = HeroSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            race = form.cleaned_data['race']
            gender = form.cleaned_data['gender']
            current_career = form.cleaned_data['current_career']
            user_heroes = Hero.objects.filter(name__icontains=name, race__icontains=race,
                                              current_career__icontains=current_career, user=request.user)
            game_master_heroes = Hero.objects.filter(name__icontains=name, race__icontains=race,
                                                     current_career__icontains=current_career, game_master=request.user)
            if gender != "":
                user_heroes = user_heroes.filter(gender=gender)
                game_master_heroes = game_master_heroes.filter(gender=gender)
            return render(request, "warhammer_heroes.html", {'user_heroes': user_heroes,
                                                             'game_master_heroes': game_master_heroes,
                                                             "form": form})


class HeroDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, hero_id):
        current_user = request.user
        hero = Hero.objects.get(id=hero_id)
        if current_user == hero.user:
            hero.delete()
            return redirect("/warhammer/heroes/")
        else:
            return render(request, 'access_denied.html', {})


class UserProfileView(View):
    @method_decorator(login_required)
    def get(self, request, user_id):
        current_user = request.user
        user_to_check = User.objects.get(id=user_id)
        user_heroes = Hero.objects.filter(user=user_to_check)
        game_master_heroes = Hero.objects.filter(game_master=user_to_check)
        if current_user == user_to_check:
            return render(request, 'user_profile.html', {'user': user_to_check,
                                                         'user_heroes': user_heroes,
                                                         'game_master_heroes': game_master_heroes})
        else:
            return render(request, 'user_profile.html', {'user': user_to_check,
                                                         'user_heroes': user_heroes,
                                                         'game_master_heroes': game_master_heroes})


class AssignExperienceView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        form = AssignExperienceForm(user)
        game_master_heroes = Hero.objects.filter(game_master=request.user)
        if not game_master_heroes:
            message = "Sorry, currently you aren't a game master for any character."
            return render(request, 'warhammer_assign_experience.html', {'message': message})
        else:
            return render(request, 'warhammer_assign_experience.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        user = request.user
        form = AssignExperienceForm(user, request.POST)

        if form.is_valid():
            hero_name = form.cleaned_data['hero']
            experience = form.cleaned_data['experience']
            game_master_heroes = Hero.objects.filter(game_master=request.user)
            message = str(experience) + " experience assigned to " + str(hero_name)
            hero = Hero.objects.get(name=hero_name)
            hero.experience += experience
            hero.save()
            return render(request, 'warhammer_assign_experience.html', {'form': form,
                                                                        'message': message})
        else:
            form = AssignExperienceForm(user)
            message = "You have to assign a number between 1 and 2000."
            return render(request, 'warhammer_assign_experience.html', {'form': form,
                                                                        'message': message})

class MainSiteView(View):
    def get(self, request):
        news = News.objects.all()
        news = news.order_by('-date_added')
        return render(request, 'main_site.html', {'news': news})


class AddNewsView(View):
    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_superuser:
            news_form = AddNewsForm
            return render(request, 'add_news.html', {'form': news_form})
        else:
            return render(request, 'access_denied.html', {})

    @method_decorator(login_required)
    def post(self, request):
        if request.user.is_superuser:

            news_form = AddNewsForm(request.POST, request.FILES)
            if news_form.is_valid():
                title = news_form.cleaned_data['title']
                content = news_form.cleaned_data['content']
                try:
                    if request.FILES['picture']:
                        new_news = News.objects.create(
                            title=title,
                            content=content,
                            added_by=request.user,
                            picture=request.FILES['picture'])
                        new_news.save()
                except KeyError:
                    new_news = News.objects.create(
                        title=title,
                        content=content,
                        added_by=request.user,)
                    new_news.save()
                return redirect("/")
            else:
                error_message = str("Wrong data. The news hasn't been created.")
                return render(request, 'add_news.html', {'news_form': news_form,
                                                         'error_message': error_message})
        else:
            return render(request, 'access_denied.html', {})


class DeleteNewsView(View):
    @method_decorator(login_required)
    def get(self, request, news_id):
        current_user = request.user
        news = News.objects.get(id=news_id)
        if current_user.is_superuser:
            news.delete()
            return redirect("/")
        else:
            return render(request, 'access_denied.html', {})


class EditNewsView(View):
    @method_decorator(login_required)
    def get(self, request, news_id):
        if request.user.is_superuser:
            news_form = AddNewsForm
            news_to_edit = News.objects.get(id=news_id)
            return render(request, 'edit_news.html', {'form': news_form,
                                                     'news': news_to_edit})
        else:
            return render(request, 'access_denied.html', {})

    @method_decorator(login_required)
    def post(self, request, news_id):
        if request.user.is_superuser:

            news_form = AddNewsForm(request.POST, request.FILES)
            if news_form.is_valid():
                title = news_form.cleaned_data['title']
                content = news_form.cleaned_data['content']
                news_to_edit = News.objects.get(id=news_id)
                try:
                    if request.FILES['picture']:
                        news_to_edit.title = title
                        news_to_edit.content = content
                        news_to_edit.added_by = request.user
                        news_to_edit.picture = request.FILES['picture']
                        news_to_edit.save()
                except KeyError:
                    news_to_edit.title = title
                    news_to_edit.content = content
                    news_to_edit.added_by = request.user
                    news_to_edit.save()
                return redirect("/")
            else:
                error_message = str("Wrong data. The news hasn't been changed.")
                return render(request, 'add_news.html', {'news_form': news_form,
                                                         'error_message': error_message})
        else:
            return render(request, 'access_denied.html', {})

