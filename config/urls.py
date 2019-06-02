from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.urls import include, path
from .settings import base as settings
from rpg_hero_creator.warhammer_hero_creator.views import HeroCreationView, HeroView,UserProfileView, \
    HeroesSearchAndView, MainSiteView, HeroDeleteView, AssignExperienceView, AddNewsView, DeleteNewsView, EditNewsView
from rpg_hero_creator.user_login import views
from rpg_hero_creator.user_login.views import UserLoginView, AddUserView,  UserLogoutView


# urlpatterns = [
#     path('', TemplateView.as_view(template_name='myapp/home.html'),
#         name='home'),
#
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainSiteView.as_view(), name="index"),
    url(r'^warhammer/hero-creation/', HeroCreationView.as_view(), name='warhammer-hero-creation'),
    url(r'^warhammer/hero/(?P<hero_id>(\d+))$', HeroView.as_view(), name="warhammer-hero-view"),
    url(r'^warhammer/heroes/', HeroesSearchAndView.as_view(), name='warhammer-heroes'),
    url(r'^warhammer/hero/delete/(?P<hero_id>(\d+))$', HeroDeleteView.as_view(), name='warhammer-hero-delete'),
    url(r'^warhammer/assign-experience/', AssignExperienceView.as_view(), name='warhammer-assign-experience'),

    url(r'^warhammer/add-news/', AddNewsView.as_view(), name='warhammer-add-news'),
    url(r'^warhammer/delete-news/(?P<news_id>(\d+))$', DeleteNewsView.as_view(), name='warhammer-news-delete'),
    url(r'^warhammer/edit-news/(?P<news_id>(\d+))$', EditNewsView.as_view(), name='warhammer-news-edit'),

    url(r'^user-profile/(?P<user_id>(\d+))$', UserProfileView.as_view(), name='user-profile'),
    url(r'^user-login/', UserLoginView.as_view(), name='user-login'),
    url(r'^user-logout/', UserLogoutView.as_view(), name='user-logout'),
    url(r'^add-user/', AddUserView.as_view(), name='add-user'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
