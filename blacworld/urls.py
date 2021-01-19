from django.urls import path
from . import views
from.views import MembersListView,MemberDetailView


urlpatterns = [
    path("", views.home, name="home"),
    path("member_search", views.member_search, name="member_search"),

    path("about/", views.about, name="about"),
    path('members/', MembersListView.as_view(), name='members'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member'),

]