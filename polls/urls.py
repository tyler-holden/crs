from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^courses/$', views.courses, name='polls_courses'),
    # Polls (begin)
    url(r'^courses/(?P<course_pk>\d+)/$', views.list_polls, name='list_polls'),
    url(r'^courses/(?P<course_pk>\d+)/new_poll$', views.new_poll, name='new_poll'),
    url(r'^courses/(?P<course_pk>\d+)/(?P<poll_pk>\d+)/$',
        views.list_pollquestions, name='list_pollquestions'),
    url(r'^courses/(?P<course_pk>\d+)/(?P<poll_pk>\d+)/admin/$',
        views.poll_admin, name='poll_admin'),
    url(r'^courses/(?P<course_pk>\d+)/(?P<poll_pk>\d+)/(?P<question_pk>\d+)/edit/$',
        views.edit_pollquestion, name='edit_pollquestion'),
    url(r'^courses/(?P<course_pk>\d+)/(?P<poll_pk>\d+)/new/$',
        views.new_pollquestion, name='new_pollquestion'),
    url(r'^courses/(?P<course_pk>\d+)/(?P<poll_pk>\d+)/new/(?P<question_pk>\d+)$',
        views.new_pollquestion, name='new_pollquestion'),
    url(r'^courses/(?P<course_pk>\d+)/(?P<poll_pk>\d+)/(?P<question_pk>\d+)/poll_history/(?P<poll_num>-?\d+)/$',
        views.poll_history, name='poll_history'),
    url(r'^courses/(?P<course_pk>\d+)/(?P<poll_pk>\d+)/(?P<question_pk>\d+)/who_voted/(?P<poll_num>\d+)/$',
        views.who_voted, name='who_voted'),
    url(r'^courses/(?P<course_pk>\d+)/live_poll/$', views.live_poll, name='live_poll'),
    # Polls end
    # Admin begin
    url(r'^administrative/$', 
        views.administrative, 
        name='poll_admin'),
    url(r'^administrative/create_course/$', 
        views.create_course, 
        name='polls_create_course'),
    url(r'^administrative/add_staff_member/$', 
        views.add_staff_member,
        name='polls_add_staff_member'),
    url(r'^administrative/add_students/$', 
        views.add_students, 
        name='polls_add_students'),
     url(r'^administrative/enroll_course/$', 
        views.enroll_course, 
        name='polls_enroll_course'),
    # Admin end
    # Ajax Begin
    url(r'^change_question_order/$', 
        views.change_question_order, 
        name='change_question_order'),
    url(r'^live_question/$', 
        views.live_question, 
        name='live_question'),
    url(r'^query_live/$', 
        views.query_live, 
        name='query_live'),
    url(r'^make_live/$', 
        views.make_live, 
        name='make_live'),
    url(r'^course_search/$', 
        views.course_search, 
        name='polls_course_search'),
    # Ajax End
    url(r'^delete/(?P<objectStr>.+)/(?P<pk>\d+)$', 
            views.delete_item,
            name='polls_delete_item'),
]
