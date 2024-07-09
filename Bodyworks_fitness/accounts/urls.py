from django.urls import path
from accounts import views
urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('enroll/',views.enroll,name='enroll'),
    path('profile/',views.user_profile,name='profile'),
    path('gallery/',views.gallery,name='gallery'),
    path('attendance/',views.attendance,name='attendance'),
]