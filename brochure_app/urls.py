from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

import brochure_app.views as brochure_view

urlpatterns = [
    url(r'^api/answers/add$', brochure_view.Answer.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
