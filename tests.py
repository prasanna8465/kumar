

# Create your tests here.
from django.test import TestCase
from .models import seller

class Basictests(TestCase):
    def setup(self):
        seller.objects.create(NAME='kinley',
                            DESCRIPTION='in each drop has honesty',
                            COSTPERITEM= 20.000,
                            STOCKQUANTITIY= 200.000,
                            VOLUME= 4000.000)
    def test_get_method(self):
        url="http://127.0.0.1:12300/stduents"
        response=self.client.get(url)
        self.assertEqual(response.status_code,301)
        qs=seller.objects.filter(NAME='kinley')
        self.assertEqual(qs.count(),0)