from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .router import router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
    #path('', include('blog.urls')),
]
