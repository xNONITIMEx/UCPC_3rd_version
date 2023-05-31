from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('add_card/', views.AddCard.as_view(), name='add_card'),
    path('edit_card/<int:pk>', views.EditCard.as_view(), name='edit_card'),

]
