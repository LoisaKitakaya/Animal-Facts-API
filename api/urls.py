from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    # admin urls
    path('admin/all-facts/', views.ListAnimalFact.as_view()),
    path('admin/animal-fact/<int:pk>/', views.ListAnimalFactDetail.as_view()),
    # client urls
    path('all-facts/', views.list_animal_fact),
    path('animal-fact/<int:pk>/', views.list_animal_fact_detail),
    path('search-animal/', views.search_animal),
    path('random-fact/', views.random_fact),
]

urlpatterns = format_suffix_patterns(urlpatterns)