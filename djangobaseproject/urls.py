from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

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

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
handler404 = "webpage.views.handler404"
