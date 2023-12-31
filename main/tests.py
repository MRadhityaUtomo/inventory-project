from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):  #Test pengecekan initiate suatu object model item
        Item.objects.create(name="Journal",amount="1",
                            description=
                            "Something to remind, vent to, and cherish",
                            omen=30)
        Item.objects.create(name="Fair ticket",amount="4",
                            description=
                            "A fair ticket to the comifuro festival, each one a different party and story",
                            omen=0)
        
    def test_items_can_created(self): #Test apakah attribute setelah inisiasi benar
        journal = Item.objects.get(name="Journal")
        fairTicket = Item.objects.get(name="Fair ticket")
        self.assertEqual(journal.name, "Journal")
        self.assertEqual(fairTicket.name, "Fair ticket")
        self.assertEqual(journal.amount, 1)
        self.assertEqual(fairTicket.amount, 4)