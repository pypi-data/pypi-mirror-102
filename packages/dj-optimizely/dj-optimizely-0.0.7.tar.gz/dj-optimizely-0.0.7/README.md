# dj-optimizely

## Introduction

Database-backed storage for your Optimizaly datafile and utilities for using Rollouts in Django. 

Features:
* Database-backed storage for Optimizaly datafile
* Webhook endpoint to recieve datafile updates
  * The webhook payload contains the datafile for the primary environment. If the current environment is not the primary environment, the webhook call will trigger a fetch of your current environment's datafile. Only your current environment's datafile is stored locally at this time.
  * On server start the datafile will be initialized via a pull based on the provided datafile url
* Currently only supports Rollouts. Check if a featuee flag is enabled. 

## Quickstart

Install:

```
pip install dj-optimizely
```

Add `djoptimizely` to `INSTALLED_APPS`:

```
INSTALLED_APPS = [
    ...
    'djoptimizely',
    ...
]
```

Add `djoptimizely.middleware.optimizely_middleware` to `MIDDLEWARE`:

```
MIDDLEWARE = [
    ...
    'djoptimizely.middleware.optimizely_middleware',
    ...
]
```

Specify additional required settings:

```
OPTIMIZELY_ENVIRONMENT = 'staging'
OPTIMIZELY_WEBHOOK_SECRET = os.getenv('OPTIMIZELY_WEBHOOK_SECRET')
OPTIMIZELY_DATAFILE_URL = os.getenv('OPTIMIZELY_DATAFILE_URL')
```

Specify optional callbacks. Both functions take the `request` as the first parameter:

```
OPTIMIZELY_USER_ID_CALLBACK = 'myapp.module.get_user_id'
OPTIMIZELY_USER_ATTRIBS_CALLBACK = 'myapp.module.get_user_attribs'
```

Default callbacks:

```
def get_user_id_default(request):
    if request.user.is_authenticated:
        return request.user.pk
    else:
        return request.session._get_or_create_session_key()

def get_user_attribs_default(request):
    attribs = {
        'is_authenticated': False,
        'is_staff': False
    }
    if request.user.is_authenticated:
        attribs['is_authenticated'] = True
        if request.user.is_staff:
            attribs['is_staff'] = True
        
    return attribs
```

Add the webhook to urls.py:

```
path('webhooks/', include('djoptimizely.urls')),
```

### Check if a feature should be enabled:

```
from djoptimizely.services import get_feature_enabled

if get_feature_enabled(request, 'cool_stuff'):
    print('Cool!')
```

### Check in a template

```
{% load djoptimizely_tags %}

{% show_feature 'cool_stuff' as show_cool_stuff %}
{% if show_cool_stuff %}
    <p>COOL Stuff!</p>
{% endif %}
```

### Generic view mixin:

If the specified `feature_key` is `not enabled` for `request.user` return a 404

```
from djoptimizely.mixins import OptimizelyFeatureViewMixin
from django.views.generic.base import TemplateView

class CoolView(OptimizelyFeatureViewMixin, TemplateView):
    feature_key = 'cool_stuff'
    ...
```
