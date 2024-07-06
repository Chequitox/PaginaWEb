from django.urls import path,include
from .views import SignupView,FirstPage 

urlpatterns=[

    path("account",include('django.contrib.auth.urls')),
    path("signup",SignupView.as_view(),name="signup"),
    path("",FirstPage.as_view(),name="first_page"),
] 