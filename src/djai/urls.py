"""DjAI URLs."""


from collections.abc import Sequence

from django.urls.conf import include, path
from django.urls.resolvers import URLPattern

from .model import urls as model_urls


__all__: Sequence[str] = ('urlpatterns',)


urlpatterns: Sequence[URLPattern] = (
    path(route='model/',
         view=include(model_urls), kwargs=None, name=None),
    path(route='models/',
         view=include(model_urls), kwargs=None, name=None),
    path(route='modeling/',
         view=include(model_urls), kwargs=None, name=None),
)