from django.contrib import admin
from django.urls import path
import ootdApp.views

from django.conf import settings
from django.conf.urls.static import static

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
    path('feedback/', ootdApp.views.feedback, name="feedbackPage"),
    path('createPage', ootdApp.views.createPage, name="createPage"),
    path('create', ootdApp.views.createFuction, name="createFuction"),
    path('detail/<int:detail_id>', ootdApp.views.detailPage, name="detailPage"),
    path('updatePage/<int:update_id>', ootdApp.views.updatePage, name="updatePage"),
    path('update/<int:update_id>', ootdApp.views.updateFuction, name="updateFuction"),
    path('delete/<int:delete_id>', ootdApp.views.deleteFuction, name="deleteFuction"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)