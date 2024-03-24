from ninja import NinjaAPI

from cookiecutter_django_ninja_example.users.api.views import users_router

# Overrides to maintain consistency with the DRF url namespace in cookiecutter-django.
api = NinjaAPI(urls_namespace="api")

api.add_router("/users/", users_router)
