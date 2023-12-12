from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet  # CatList, CatDetail  # APICat, cat_list


# Создаётся роутер
router = SimpleRouter()
# Вызываем метод .register с нужными параметрами
router.register('cats', CatViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    # path('cats/', CatList.as_view()),
    # path('cats/<int:pk>/', CatDetail.as_view()),

    # path('cat/', CatViewSet.as_view(), name='cat-list'),
    # path('cat/<int:pk>/', CatViewSet.as_view(), name='cat-detail'),

    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]
