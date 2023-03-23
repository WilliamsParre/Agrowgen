from django.urls import path
from .views import Index, Home, Registration, Login, Logout

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Registration.as_view(), name='registration'),
    path('logout/', Logout.as_view(), name='logout')
]
