from django.contrib import admin
from django.urls import path
import ootdApp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ootdApp.views.home, name="home"),
    path('ranking/', ootdApp.views.ranking, name="ranking"),
    path('login/', ootdApp.views.login, name="login"),
    path('signup/', ootdApp.views.signup, name="signup"),
    path('findid/', ootdApp.views.findid, name="findid"),
    path('findidofphone/', ootdApp.views.findidofphone, name="findidofphone"),
    path('findpw/', ootdApp.views.findpw, name="findpw"),
    path('findpwofphone/', ootdApp.views.findpwofphone, name="findpwofphone"),

]
