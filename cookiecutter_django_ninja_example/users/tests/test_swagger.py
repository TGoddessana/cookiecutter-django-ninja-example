from http import HTTPStatus

import pytest
from django.urls import reverse


def test_swagger_accessible_by_admin(admin_client):
    url = reverse("api:openapi-view")
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db()
def test_swagger_ui_not_accessible_by_normal_user(client):
    url = reverse("api:openapi-view")
    response = client.get(url)
    # Not like DRF, Ninja does not return a 403 Forbidden status code.
    # we can define custom decorators, to pass like this:
    # `api = NinjaAPI(urls_namespace="api", docs_decorator=staff_member_required)`
    # do we have to define custom decorators for Ninja, to reproduce DRF-like behavior?
    # see: https://django-ninja.dev/guides/api-docs/
    assert response.status_code == HTTPStatus.FOUND


def test_api_schema_generated_successfully(admin_client):
    url = reverse("api:openapi-json")
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK
