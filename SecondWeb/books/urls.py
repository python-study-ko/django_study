from django.conf.urls import patterns,url
from books import views

urlpatterns = patterns('',
                       # 메인페이지
                       url(r'^$',views.BooksModelView.as_view(),name='index'),
                       # 목록페이지
                       url(r'^book/$',views.BookList.as_view(),name='book_list'),
                       url(r'author/$',views.AuthorList.as_view(),name='author_list'),
                       url(r'publisher/$',views.PublisherList.as_view(),name='publisher_list'),
                       # 세부페이지
                       url(r'book/(?P<pk>\d+)/$',views.BookDetail.as_view(),name='book_detail'),
                       url(r'author/(?P<pk>\d+)/$',views.AuthorDetail.as_view(),name='author_detail'),
                       url(r'publisher/(?P<pk>\d+)/$',views.PublisherDetail.as_view(),name='publisher_detail'),
                       )