from django.urls import resolve, reverse

class TestUrls:

    def test_urls(self):
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail'