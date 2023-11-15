# Django Template Dashboard

A dashboard based on Django template.

## Installation

Install the package via pip:

```bash
pip install django-template-dashboard
```

## Configuration

After installing the package, add it to your `INSTALLED_APPS` in the `settings.py` file of your Django project:

```python
INSTALLED_APPS = [
    # ... other apps,
    'dashboard',
]
```

Include the dashboard urls in your project's `urls.py` file:

```python
from django.urls import include, path

urlpatterns = [
    # ... other urls,
    path('dashboard/', include('dashboard.urls')),
]
```

## Usage

Navigate to `/dashboard/` in your browser to access the dashboard.

## Development

To contribute or report issues, please visit
the [dashboard](https://github.com/django-libraries/dashboard).

## License

This project is licensed under the [MIT License](LICENSE).