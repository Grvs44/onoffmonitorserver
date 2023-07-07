# On/Off Monitor Server
## Installation
Install from PyPI:
```cmd
pip install onoffmonitorserver
```
## Setup
* Add to project `urls.py`:
  ```python
  urlpatterns = [
    ...
    path('api/onoffmonitor/', include('onoffmonitorserver.urls')),
    path('api/', include('knox.urls')),
    ...
  ]
  ```
* Add to project `settings.py`:
  ```python
  INSTALLED_APPS = [
    'onoffmonitorserver',
    ...
    'rest_framework',
    'knox'
  ]
  ```
* Migrate database changes:
  ```cmd
  python manage.py migrate
  ```
