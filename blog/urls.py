
from django.urls import path
from . import views
app_name = 'blog'


from django.urls import include, path
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:id>', views.details, name='details'),

]

