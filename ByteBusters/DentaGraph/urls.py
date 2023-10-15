from django.urls import path
from ByteBusters.DentaGraph.views import login_view

urlpatterns = [
    path('loginView/', login_view),
]