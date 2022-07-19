from django.urls import path
from .views import registerPage, loginPage, validateUsername, validateEmail, logoutBtn, cUpdate_page, vUpdate_page
from django.views.decorators.csrf import csrf_exempt

app_name = 'account'

urlpatterns = [
    path('register/', registerPage, name = "register"),
    path('login/', loginPage, name = 'login'),
    path('logout/', logoutBtn, name = 'logout'),
    path('usernameValidation/', csrf_exempt(validateUsername), name = 'usernameValidation'),
    path('emailValidation/', csrf_exempt(validateEmail), name = 'emailValidation'),
    path('cUpdate_page/', cUpdate_page, name = "cUpdate-page"),
    path('vUpdate_page/', vUpdate_page, name = "vUpdate-page"),
]