from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from utils.test.view_test_mixins import TemplateViewTestMixin
from ..views import DashboardTemplateView


User = get_user_model()


class TestDashboardTemplateView(TemplateViewTestMixin, TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.view_class = DashboardTemplateView
        cls.template_name = 'demo/dashboard.html'
        cls.url = reverse('dashboard')
        cls.static_url = '/'

        # we need a user that has staff permissions for the client get
        #   request to succeed
        cls.user = User.objects.create(username='example', is_staff=True)

    def test_permission_denied(self):
        # make sure usernames don't collide
        user = User.objects.create(username="different-user")
        self.client.force_login(user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
