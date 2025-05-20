from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


from utils.test.view_test_mixins import TemplateViewTestMixin
from utils.test.auth_test_mixins import StaffUserTestMixin
from ..views import DashboardTemplateView


User = get_user_model()


class TestDashboardTemplateView(
    TemplateViewTestMixin,
    StaffUserTestMixin,
    TestCase
):

    @classmethod
    def setUpTestData(cls):
        cls.view_class = DashboardTemplateView
        cls.template_name = 'demo/dashboard.html'
        cls.url = reverse('dashboard')
        cls.static_url = '/'

        # we need a user that has staff permissions for the client get
        #   request to succeed
        cls.user = User.objects.create(username='example', is_staff=True)
