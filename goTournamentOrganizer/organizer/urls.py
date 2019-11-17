from django.urls import path

from . import views

urlpatterns = [
    # ex: /organizer/
    path('', views.index, name='index'),
    # ex: /organizer/5
    path('<int:participants_id>/', views.detail, name='detail'),
    # ex: /organizer/5/participant
    path('<int:participants_id>/participants/', views.participants, name='participants'),
]