from django.urls import path
from . import views
urlpatterns = [
    path('view/',views.chooseUser ),
    path('signup/', views.SignUp.as_view(), name='signup'),
]