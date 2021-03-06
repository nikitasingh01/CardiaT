from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_idea',views.add,name='idea-add'),
    path('<int:idea_id>/view_idea/',views.detail,name='idea-view'),
    path('search_result',views.search,name='search-result'),
    path('filter_result',views.filter,name='filter-result'),
    path('<str:tag>/tag_result',views.popularTag,name='tag-result'),
]
