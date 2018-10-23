# from app.models import Blog,User
# from app import db
#
# def setUp(self):
#
#     self.user_tarek = User(username = 'tarek',password = 'tarek001', email = 'tarickaliabdi@gmail.com')
#     self.new_blog = Blog(title='Civilized country',blog_content="Love and Peace is the key for a success country",user = self.user_James )
#
# def tearDown(self):
#
#     Blog.query.delete()
#     User.query.delete()
#
# def test_check_instance_variables(self):
#
#     self.assertEquals(self.new_blog.title,'Civilized country')
#     self.assertEquals(self.new_blog.blog_content,"Love and Peace is the key for a success country")
#     self.assertEquals(self.new_blog.user,self.user_tarek)
#
# def test_save_blog(self):
#
#     self.new_blog.save_blog()
#     self.assertTrue(len(Blog.query.all())>0)
