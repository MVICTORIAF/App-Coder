

from App import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('profesor/', views.profesor, name='profesor'),
    path('curso/', views.curso, name='curso'),
]

