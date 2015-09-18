# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from blog.models import Post
import urllib.request

class TestPostModel(TestCase):
    def _create_post(self):
        Post.objects.create(title=u'테스트', content=u'내용')

    def test_check_url(self):
        res = urllib.request.urlopen('http://www.google.com').getcode()
        assert(res == 200, res)

    def test_create_post_model(self):
        self._create_post()
        posts = Post.objects.all()
        self.assertEqual(len(posts), 1)
        post = posts[0]
        self.assertEqual(post.title, u'테스트')
        self.assertEqual(post.content, u'내용')

    def test_basic_listing(self):
        self._create_post()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 1)
        object_list = response.context['object_list']
        post = object_list[0]
        self.assertEqual(post.title, u'테스트')