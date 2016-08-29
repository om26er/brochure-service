from django.conf.urls import include, url
from django.contrib import admin

import brochure_app.urls as brochure_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(brochure_urls))
]
