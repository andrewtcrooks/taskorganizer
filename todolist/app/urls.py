from django.conf.urls import url
from .views import home, todo


urlpatterns = [
    url(r'^$', home.main_page),
    url(r'^signup$', home.signup),
    url(r'^login$', home.login),
    url(r'^logout$', home.logout),
    url(r'^add-todo$', todo.add_todo),
    url(r'^edit-todo/(?P<todo_id>\d+)$', todo.edit_todo),
    url(r'^delete-todo/(?P<todo_id>\d+)$', todo.delete_todo),
    # ... your url patterns
]
