from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_idea',views.add,name='idea-add'),
    path('<int:idea_id>/view_idea/',views.detail,name='idea-view'),
    path('search_result',views.search,name='search-result'),
]
