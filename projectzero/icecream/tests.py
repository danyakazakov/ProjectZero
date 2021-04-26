from django.test import TestCase, Client
from .models import Icecream
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class testIce(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.icecream = Icecream.objects.create(
            name = 'клубничное мороженое',
            desc = 'мороженое со вкусом клубники',
            price = 100,
            rating = 4
        )

    def setUp(self):
        self.guest_client = Client()
        self.user=User.objects.create_user(username='test')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_homepage(self):
        response=self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_name_label(self):
        n = testIce.icecream
        verbose = n._meta.get_field('name').verbose_name
        self.assertEquals(verbose, 'имя')
    
    def test_name_help_text(self):
        n = testIce.icecream
        help_text = n._meta.get_field('name').help_text
        self.assertEquals(help_text, 'название мороженого')

    def test_desc_label(self):
        n = testIce.icecream
        verbose = n._meta.get_field('desc').verbose_name
        self.assertEquals(verbose, 'описание')
    
    def test_desc_help_text(self):
        n = testIce.icecream
        help_text = n._meta.get_field('desc').help_text
        self.assertEquals(help_text, 'описание мороженого')

    def test_price_label(self):
        n = testIce.icecream
        verbose = n._meta.get_field('price').verbose_name
        self.assertEquals(verbose, 'цена')

    def test_price_help_text(self):
        n = testIce.icecream
        help_text = n._meta.get_field('price').help_text
        self.assertEquals(help_text, 'цена мороженого')

    def test_icecreampage_guest(self):
        response=self.guest_client.get('/icecream/')
        self.assertEqual(response.status_code, 302)

    def test_icecreampage_authorized(self):
        response=self.authorized_client.get('/icecream/')
        self.assertEqual(response.status_code, 200)

    def test_icecreampage_list_correct_temp(self):
        response=self.authorized_client.get('/icecream/')
        self.assertTemplateUsed(response, 'icecream/icecream-list.html')
    
    def test_icecreamdetail_quest(self):
        response=self.guest_client.get('/icecream/1/')
        self.assertEqual(response.status_code, 302)
    
    def test_icecreamdetail_authorized(self):
        response=self.authorized_client.get('/icecream/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_icecreamdetail_correct_temp(self):
        response=self.authorized_client.get('/icecream/1/')
        self.assertTemplateUsed(response, 'icecream/icecream-detail.html')

    def test_icrecreamlist_correct_name(self):
        response=self.authorized_client.get(reverse('icecream-list'))
        self.assertTemplateUsed(response, 'icecream/icecream-list.html')
    
    def test_icecreamdetail_correct_name(self):
        response=self.authorized_client.get(
            reverse('detail', kwargs={'pk':1})
        )
        self.assertTemplateUsed(response, 'icecream/icecream-detail.html')
    
    def test_icecream_list_correct_context(self):
        response=self.authorized_client.get(reverse('icecream-list'))
        self.assertIn('icecreams', response.context)






