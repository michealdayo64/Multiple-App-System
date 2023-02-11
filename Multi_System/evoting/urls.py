from django.urls import path
from .views import cHome_page, vHome_page, vDetail_page, voteCandidate, admimDashboard

app_name = 'evoting'

urlpatterns = [
    path('cHome_page/', cHome_page, name = "cHome-page"),
    path('vHome_page/', vHome_page, name = "vHome-page"),
    path('vDetail_page/<id>/', vDetail_page, name = "vDetail-page"),
    path('vote_candidate/<id>/', voteCandidate, name = "vote-candidate"),
    path('admimDashboard/', admimDashboard, name = "admimDashboard")
]