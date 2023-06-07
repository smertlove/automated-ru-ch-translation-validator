from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('get_file', views.get_file, name='get_file' ),
    path('constructor', views.constructor, name='constructor'),
    path('get_regex', views.get_regex, name='get_regex')
]



# urlpatterns = [
#     path('', views.index, name='index' ),
#     path('exercise_list', views.exercises, name='exercises'),
#     path('entry_page', views.entry, name='entry'),
#     path('load-more-entries/', views.dynamic_entries_load, name='load-more-entries'),
#     path('entry-list', views.entry_list_load, name='load-entry-list'),
#     path('search', views.live_search, name='live-search'),
#     path('exercise', views.render_exercise_page, name='exercise'),
#     path('translate', views.get_translation_task, name='get-translate-task'),
#     path('choose', views.get_choose_task, name='get-choose-task'),
#     path('card', views.get_card, name='get-card')
# ]