from ninja.testing import TestClient

from cookiecutter_django_ninja_example.users.api.views import users_router
from cookiecutter_django_ninja_example.users.models import User


class TestUserAPI:
    def test_user_me(self, user: User):
        client = TestClient(users_router)
        response = client.get("/me/", user=user)

        # there is no `status` in django-ninja,
        # do we need to add enum for status codes?
        assert response.status_code == 200  # noqa: PLR2004

        assert response.json() == {
            "username": user.username,
            # note that drf creates urls with `testserver`,
            # but django-ninja uses `testlocation`
            "url": f"http://testlocation/api/users/{user.username}/",
            "name": user.name,
        }
