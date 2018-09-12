from django.urls import path, re_path

from . import views

urlpatterns = [
    # API Patterns
    re_path(r'^api/(?P<user_id>[0-9]+)/gallery/$', views.RectangleListView.as_view(), name='rectangle_list_view'),
    re_path(r'^api/create_rectangle/$', views.RectangleCreateView.as_view(), name='rectangle_create_view'),
    re_path(r'^api/delete_rectangle/(?P<rectangle_id>[0-9]+)/$', views.rectangle_delete_view, name='rectangle_delete_view'),

    # Login Patterns
    path('login/', views.user_login, name='login'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('log-out/', views.log_out, name='log_out'),

    # All other URLs are directed to the SPA
    re_path(r'^.*$', views.home, name='home'),
]
