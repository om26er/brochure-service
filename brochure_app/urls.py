from django.conf.urls import url

import brochure_app.views as brochure_view

urlpatterns = [
    url(r'^api/answers/add$', brochure_view.Answer.as_view()),
    url(r'^api/brochure$', brochure_view.BrochureView.as_view()),
]
