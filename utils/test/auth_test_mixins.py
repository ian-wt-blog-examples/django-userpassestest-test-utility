import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as DjangoUser
from django.core.exceptions import ValidationError, ImproperlyConfigured


User = get_user_model()


# noinspection PyUnresolvedReferences
class StaffUserTestMixin:
    """
    Used to test that only users with 'is_staff=True' are able to access view
       as enforcd by UserPassesTestMixin.

    Note: Not compatible with user_passes_test_mixin!
    """
    def test_permission_denied(self):
        username = f'user-{str(uuid.uuid4())}'
        user = User()

        if isinstance(User, DjangoUser):
            # default user model, set username and move on
            user.username = username
            user.save()
        else:
            # not the default user model
            if User.USERNAME_FIELD == User.EMAIL_FIELD:
                setattr(user, User.EMAIL_FIELD, f'{username}@example.com')
            else:
                # try to insert username anyways and catch any problems
                setattr(user, User.USERNAME_FIELD, username)
            try:
                user.save()
            except ValidationError:
                raise ImproperlyConfigured('Unable to create user for test.')

        # if we're this far, we have a user
        self.client.force_login(user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
