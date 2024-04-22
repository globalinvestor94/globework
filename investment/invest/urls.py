from django.urls import path
from .views import  GlobalView,Signup,Profile, AboutView,Login,logoutUser,detailView, beginnerPlan, professionalPlan, representativePlan, promoPlan, finalePlan
from django.views.generic import ListView
from django.contrib.auth import views as auth_views
# from . views import *
	

app_name = 'invest'
urlpatterns =[ 
path(r'', GlobalView, name='home'),
path(r'<str:ref_code>/', GlobalView, name='home'),
path(r'learn_more', detailView, name='learnmore'),
path(r'user_profile', Profile, name='profile'), 
path(r'register', Signup, name='register'),
path(r'login', Login, name='login'),
path('logout', logoutUser, name='logout'),
path(r'beginner_plan', beginnerPlan, name='beginner'),
path(r'professional_plan', professionalPlan, name='professional'),
path(r'representative_plan', representativePlan, name='representative'),
path(r'promo_plan', promoPlan, name='promo'),
path(r'finale_plan', finalePlan, name='finale'),
path(r'about_us', AboutView, name='about'),

path(r'reset_password/', 
	auth_views.PasswordResetView.as_view(template_name="folder/password_reset.html"), 
	name='reset_password'),
path(r'reset_password_sent/', 
	auth_views.PasswordResetDoneView.as_view(template_name="folder/password_reset_sent.html"), 
	name='password_reset_done'),
path(r'reset/<uidb64>/<token>/', 
	auth_views.PasswordResetConfirmView.as_view(template_name="folder/password_reset_form.html"), 
	name='password_reset_confirm'),
path(r'reset_password_complete/', 
	auth_views.PasswordResetCompleteView.as_view(template_name="folder/password_reset_done.html"), 
	name='password_reset_complete'),


]
