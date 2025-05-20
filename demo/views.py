from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class DashboardTemplateView(UserPassesTestMixin, TemplateView):
    template_name = 'demo/dashboard.html'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff
