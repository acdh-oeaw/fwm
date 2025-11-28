"""djangobaseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("celery/", include("django_celery_results.urls")),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    # path('netvis/', include('netvis.urls', namespace="netvis")),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("archiv-ac/", include("archiv.dal_urls", namespace="archiv-ac")),
    path("infos/", include("infos.urls", namespace="infos")),
    path("plate/", include("django_spaghetti.urls")),
    path("vocabs-ac/", include("vocabs.dal_urls", namespace="vocabs-ac")),
    path("zotero-ac/", include("zotero_ac.dal_urls", namespace="zotero-ac")),
    path("", include("webpage.urls", namespace="webpage")),
]
handler404 = "webpage.views.handler404"
