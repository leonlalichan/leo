from.import views
from django.urls import path

urlpatterns = [
    path('',views.task_list,name='task'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('v/',views.Tasklistview.as_view(),name='v/'),
    path('c/<int:pk>/', views.Detailview.as_view(), name='c/'),
    path('cupdate/<int:pk>/', views.UpdateView.as_view(), name='cupdate'),
    path('vdelete/<int:pk>/',views.Deleteview.as_view(),name='vdelete/'),
]

