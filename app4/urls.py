from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('',include('app1.urls')),
    path('logout', views.logout, name='logout')
  #  path('app2',include('app2.urls'))

]