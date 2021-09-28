from django.test import RequestFactory, TestCase
from mysite import views

class IndexPageTest(TestCase):
    def test_index(self):
        request = RequestFactory().get('/')
        assert(type(request).__name__ == 'WSGIRequest')
        assert(type(request.GET).__name__ == 'QueryDict')
        resp = views.index(request)
        assert resp.status_code == 200
