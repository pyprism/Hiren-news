from django.test import TestCase, TransactionTestCase
from .models import Bunny, Tag
from django.test import Client


class ModelTest(TransactionTestCase):
    """
    Test all models
    """
    reset_sequences = True

    def setUp(self):
        Bunny.objects.create(comment_url='https://news.ycombinator.com/item?id=11512455')
        Bunny.objects.create(comment_url='https://news.ycombinator.com/item?id=11511062')
        Tag.objects.create(name='Django')
        Tag.objects.create(name='python')

    def test_tag_model(self):
        tag_item = Tag.objects.all()
        self.assertEqual(tag_item.count(), 2)

        obj = Tag.objects.get(name='Django')
        obj.delete()

        tag_item = Tag.objects.all()
        self.assertEqual(tag_item.count(), 1)

    def test_bunny_model(self):
        bunny_item = Bunny.objects.all()
        self.assertEqual(bunny_item.count(), 2)

        obj = Bunny.objects.get(comment_url='https://news.ycombinator.com/item?id=11512455')
        obj.delete()

        bunny_item = Bunny.objects.all()
        self.assertEqual(bunny_item.count(), 1)


class TestViews(TestCase):

    def setUp(self):
        Bunny.objects.create(comment_url='https://news.ycombinator.com/item?id=11512455')
        Bunny.objects.create(comment_url='https://news.ycombinator.com/item?id=11511062')
        Tag.objects.create(name='Django')
        Tag.objects.create(name='python')
        self.c = Client()

    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.content, str.encode('Number of Bunny(s): ' + str(2)))