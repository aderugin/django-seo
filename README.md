# Installation and setup

```
pip install git+git://github.com/aderugin/django-seo.git
```

```
# admin.py

from seo import SeoAdmin
from django.contrib import admin

admin.site.register(Model, SeoAdmin)


# settings.py

CONTEXT_PROCESSORS = (
    ...
    'seo.context_processors.metatags'
    ...
)
```
