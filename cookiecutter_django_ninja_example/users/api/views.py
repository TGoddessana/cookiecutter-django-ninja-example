from ninja import Router
from ninja.errors import HttpError

from cookiecutter_django_ninja_example.users.models import User

from .schemas import UserSchema
from .schemas import UserUpdateSchema

users_router = Router(tags=["users"])


# error handling in django-ninja is different from DRF
# see https://django-ninja.dev/guides/errors/
# do we need to add a custom error handler function in template?


@users_router.get("me/", response=UserSchema, url_name="user-me")
def user_me(request):
    return request.user


@users_router.get("/", response=list[UserSchema], url_name="user-list")
def user_list(request):
    return User.objects.all()


@users_router.get("{username}/", response=UserSchema, url_name="user-detail")
def user_detail(request, username: str):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist as exc:
        raise HttpError(404, "User not found") from exc


@users_router.put("{username}/", response=UserSchema, url_name="user-update")
def update_user(request, username: str, payload: UserUpdateSchema):
    try:
        user = User.objects.get(username=username)
        user.username = payload.username
        user.name = payload.name
        user.save()
    except User.DoesNotExist as exc:
        raise HttpError(404, "User not found") from exc

    return user


@users_router.patch("{username}/", response=UserSchema, url_name="user-partial-update")
def partial_update_user(request, username: str, payload: UserUpdateSchema):
    try:
        user = User.objects.get(username=username)
        user.username = payload.username
        user.name = payload.name
        user.save()
    except User.DoesNotExist as exc:
        raise HttpError(404, "User not found") from exc

    return user
