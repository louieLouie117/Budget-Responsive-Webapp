from django.urls import path, include
from . import views

urlpatterns = [
    #rendering paths
    path('', views.index),
    path('app', views.show_dashboard),

    #redirecting paths
    path('resgister', views.register_user),
    path('login', views.login_user),
    path('logout', views.logout),
    path('add/budget', views.add_budget),
    #traction froms---------------------------------
    path('add/home', views.add_home),
    path('add/bill', views.add_bill),
    path('add/personal', views.add_personal),
    path('add/eating', views.add_eating),
    path('add/car', views.add_car),
    path('add/giving', views.add_giving),
    # delete
    path('delete/<int:budget_id>', views.delete_budget),
    path('remove/<int:transaction_id>', views.delete_transaction)
    
]

