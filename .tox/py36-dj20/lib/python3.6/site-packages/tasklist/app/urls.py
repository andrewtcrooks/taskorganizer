"""urls.py ."""
from django.conf.urls import url
# from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home, task
# from config import settings

urlpatterns = [
    url(r'^$', home.main_page),
    url(r'^signup$', home.signup),
    url(r'^login$', home.login),
    url(r'^logout$', home.logout),
    url(r'^add-task$', task.add_task),
    url(r'^edit-task/(?P<task_id>\d+)$', task.edit_task),
    url(r'^delete-task/(?P<task_id>\d+)$', task.delete_task),
    # ... your url patterns
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
