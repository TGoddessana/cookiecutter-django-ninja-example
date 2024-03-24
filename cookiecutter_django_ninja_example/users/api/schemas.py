from django.urls import reverse
from ninja import ModelSchema

from cookiecutter_django_ninja_example.users.models import User


class UserUpdateSchema(ModelSchema):
    class Meta:
        model = User
        fields = ["username", "name"]


class UserSchema(ModelSchema):
    url: str

    @staticmethod
    def resolve_url(obj: User, context):
        request = context["request"]
        return request.build_absolute_uri(
            reverse("api:user-detail", kwargs={"username": obj.username}),
        )

    class Meta:
        model = User
        fields = ["username", "name"]
