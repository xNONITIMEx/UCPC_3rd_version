from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('add_card/', views.AddCard.as_view(), name='add_card'),
    path('edit_card/<int:pk>', views.EditCard.as_view(), name='edit_card'),
]
