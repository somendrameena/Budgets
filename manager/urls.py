from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('addnew/', views.AddItemView.as_view(), name='addnew'),
    path('added/', views.AddedItemView.as_view(), name='added'),
    url(r'^viewall/$', views.ItemListView.as_view()),
    url(r'^detail/(?P<pk>\w+)/$', views.ItemDetailView.as_view(), name='detail'),
    url(r'^detail/(?P<pk>\w+)/edit$', views.EditItemView.as_view()),
    url(r'^detail/(?P<pk>\w+)/delete$', views.DeleteItemView.as_view()),
    url(r'^user/', views.UserDetailView.as_view()),
    url(r'^register/', views.register),
]
