from django.urls import path
from . import views

urlpatterns = [
    path(route = '', view = views.contact_index, name = 'contact_index'),
    path(route = 'login', view = views.login, name = 'login'),
    path(route = 'register', view = views.register, name = 'register'),
    path(route = 'home', view = views.home, name = 'home'),
    path(route = 'contact', view = views.contact, name = 'contact'),
    path('<int:contact_id>/', views.contact_detail, name = 'contact_detail')
]
