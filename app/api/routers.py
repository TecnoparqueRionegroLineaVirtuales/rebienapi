from rest_framework.routers import DefaultRouter
from ..account.views import *
from ..survey.views import *

router = DefaultRouter()

router.register(r'accounts', AccountViewset, basename='accounts')
router.register(r'typeaccounts', TypeAccountViewset, basename='typeaccounts')
router.register(r'responses', ResponsesViewset, basename='responses')
router.register(r'survey', SurveyViewset, basename='survey')
router.register(r'questions', QuestionsViewset, basename='questions')



urlpatterns = router.urls
