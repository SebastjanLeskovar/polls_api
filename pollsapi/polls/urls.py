from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import ChoiceList, CreateVote, PollDetail, PollList, PollViewSet
from .views import polls_detail, polls_list


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls
