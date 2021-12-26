from django.urls import path
from . import views
from django.contrib.auth import authenticate, login, views as auth_views
from .forms import LoginForm
from django.conf.urls.static import static
from django.conf import settings
from .forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm 


urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('semester/<int:id>/', views.semesterView, name='semester'),
    path('subject', views.subject, name='subject'),
    path('model-questions/<int:id>/', views.modelQuestion, name='modelquestions'),
    path('unitwise-questions/<int:id>/', views.unitwiseQuestion, name='unitwisequestions'),
    path('refrenced-books/<int:id>/', views.refrenced_books, name='refrenced-books'),
    path('tech-news/', views.tech_news, name='tech-news'),
    path('tech-detail/<int:id>/', views.tech_detail, name='tech-detail'),

    path('sports', views.sports, name='sports'),
    path('sports-detail/<int:id>/', views.sports_detail, name='sports_detail'),

    path('about/', views.about, name="about"),
    # ========================= PROGRAMMING URLS============================

    path('programming/' , views.programming , name = "programming"),
    path('learnhtml/' , views.learnhtml , name = 'learnhtml'),
    path('learncss/' , views.learncss , name = 'learncss'),
    path('learnbootstrap/' , views.learnbootstrap , name = 'learnbootstrap'),
    path('learnjavascript/' , views.learnjavascript , name = 'learnjavascript'),
    path('learnjquery/' , views.learnjquery , name = 'learnjquery'),
    path('learnphp/' , views.learnphp , name = 'learnphp'),
    path('learnpython/' , views.learnpython , name = 'learnpython'),
    path('learndjango/' , views.learndjango , name = 'learndjango'),
    path('learnsql/' , views.learnsql , name = 'learnsql'),
    path('intro/' , views.intro , name = "intro"),

    path('login/contact/' , views.ProfileView.as_view() , name = 'contact'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    # ==================registration=======================
    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    # ====================login ==============================
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
     
     path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html", form_class=MyPasswordChangeForm, success_url="/passwordchangedone/"), name="passwordchange"),

     path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name="app/password_change_done.html"), name="passwordchangedone"),

     path('password-reset/', auth_views.PasswordResetView.as_view(template_name="app/password_reset.html", form_class=MyPasswordResetForm), name="password_reset"),

     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"), name="password_reset_done"),

     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html' , form_class=MySetPasswordForm), name="password_reset_confirm"),

     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html') ,  name="password_reset_complete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
