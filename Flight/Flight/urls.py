from django.contrib import admin
from django.urls import path
from Flight import view

urlpatterns = [
    # path('admin/', admin.site.urls),
    # ex: /polls/
    # path('', view.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', view.detail, name='detail'),
]


