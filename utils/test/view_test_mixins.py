from django.views.generic import TemplateView


# noinspection PyUnresolvedReferences
class TemplateViewTestMixin:
    error_msg = 'The required attribute %s has not been set.'

    def _check_attr(self, attr_name):
        if not getattr(self, attr_name, None):
            raise AttributeError(self.error_msg % attr_name)

    def test_correct_template(self):
        self._check_attr('view_class')
        self._check_attr('template_name')

        if not issubclass(getattr(self, 'view_class'), TemplateView):
            raise TypeError("Attr 'view_class' not a subclass of 'TemplateView.'")

        view = self.view_class()
        self.assertEqual(view.template_name, self.template_name)

    def test_good_status_code(self):
        self._check_attr('url')

        # check if there's a user attached to the test that may have
        #   required permissions
        if hasattr(self, 'user'):
            # assumes user was already assigned required permissions
            self.client.force_login(getattr(self, 'user'))

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_good_location(self):
        self._check_attr('url')
        self._check_attr('static_url')

        self.assertEqual(self.url, self.static_url)
