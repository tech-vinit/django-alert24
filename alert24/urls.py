
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name ='home'),
    path('india/', views.india, name='india'),
    path('world/', views.world , name='world'),
    path('health/',views.health,name='health'),
    path('dynamic/<int:id>',views.dynamic, name='dynamic')

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)