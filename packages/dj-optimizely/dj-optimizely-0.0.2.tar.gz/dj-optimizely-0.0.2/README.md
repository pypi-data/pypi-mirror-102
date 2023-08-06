# dj-optimizely

Store optimizely datafile in a Django model

## WORK IN PROGRESS

This app is in the very early stages and I'll be fleshing it out over the coming weeks. 
Though it is currently in use. 


## Usage
-----------------

### Settings

```
INSTALLED_APPS = [
    ...
    'djoptimizely',
    ...
]

MIDDLEWARE = [
    ...
    'djoptimizely.middleware.optimizely_middleware',
    ...
]

OPTIMIZELY_ENVIRONMENT = 'staging'
OPTIMIZELY_WEBHOOK_SECRET = os.getenv('OPTIMIZELY_WEBHOOK_SECRET')
OPTIMIZELY_DATAFILE_URL = os.getenv('OPTIMIZELY_DATAFILE_URL')
OPTIMIZELY_USER_ID = 'myapp.module.get_user_id' # Specify a function to get user id (required)
OPTIMIZELY_USER_ATTRIBS = 'myapp.module.get_user_attribs' # Specify a function to get user attribs (optional)
```

### Urls

```
urlpatterns = [
    ...
    path('webhooks/', include('djoptimizely.urls')),
    ...
]
```

### Check if a feature should be enabled:

```
from djoptimizely.services import get_feature_enabled
...
if get_feature_enabled(request, 'cool_stuff'):
    print('Cool!')
```

### With a template tag

```
{% load optimizely_tags %}
...
{% show_feature 'cool_stuff' as show_cool_stuff %}
{% if show_cool_stuff %}
    <p>COOL Stuff!</p>
{% endif %}
```

### View mixin: (serve if enabled else 404)

```
from djoptimizely.mixins import OptimizelyFeatureViewMixin
from django.views.generic.base import TemplateView

class CoolView(OptimizelyFeatureViewMixin, TemplateView):
    feature_key = 'cool_stuff'
    ...
```
