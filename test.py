from time import sleep
from django.test import TestCase
from blog.views import PostDetail, PostList, PostCreate

class Test(TestCase):
    def test_1(self):  # read
        detail = PostDetail()
		#assert(False)
    def test_2(self):  # write
        list = PostList()
        # self.test_1()
    def test_3(self):
        create = PostCreate()	
		# assert 0
        # self.test_1()
