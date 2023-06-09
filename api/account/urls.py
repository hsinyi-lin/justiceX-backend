from django.urls import path
from api.account.views import *

urlpatterns = [
    path('picture_list/', picture_list, name='picture_list'),
    path('get_account/', get_account, name='get_account'),
    path('edit_account/', edit_account, name='edit_account'),
    path('change_password/', change_password, name='change_password'),
    path('add_quiz/', add_quiz, name='add_quiz'),
    path('collect_list/', collect_list, name='collect_list'),
    path('notice/', notice, name='notice'),
    path('add_eazy_quiz/', add_eazy_quiz, name='add_eazy_quiz')
]