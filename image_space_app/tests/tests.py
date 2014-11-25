import datetime
from django.test.client import Client
from django.utils import timezone
from django.test import TestCase
from signups.models import SignUp, Event
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver


c=Client()
class ImageSpaceTests(TestCase):
        def testsignup(self):
		response=c.get('/signup/')
	def setUP(self):
		self.user== User.objects.create_user(username='Adam',email='meh@meh.net',password='password')
		user.save()
		admin=User.objects.create_superuser('root', 'test@test.test', 'testing')
	def testauthview(self):
		response=c.get('/authview/')
	def test1(self):
		test1=c.login(username='Adam',password='password')
	def testinvalid(self):
		response=c.get('/invalid/')
	def test2(self):
		if(c.login(username='Adam',password='wrongpassword')==False):
			test2=True
	def test3(self):
		if(c.login(username='Wrongname',password='password')==False):
			test3=True
	def testrootpage(self):
		response=c.get('/root/')
	def testroot(self):
		if(c.login(username='root',password='testing')==True):
			testroot=True

class Seleniumtests(LiveServerTestCase):
	def setUp(self):
		User.objects.create_superuser(username='admin',password='admin',email='admin@example.com')
		self.selenium = webdriver.Firefox()
		self.selenium.implicitly_wait(3)
	        self.selenium.maximize_window()
        	super(Seleniumtests, self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(Seleniumtests, self).tearDown()

	def test_root(self):
		self.selenium.get('%s%s' % (self.live_server_url,  "/admin/"))
		username = self.selenium.find_element_by_id("id_username")
        	username.send_keys("admin")
		password = self.selenium.find_element_by_id("id_password")
        	password.send_keys("admin")


		self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
		self.selenium.get('%s%s' % (self.live_server_url, "/admin/auth/user/add/"))

	def test_create_Event(self):
                self.selenium.get('%s%s' % (self.live_server_url,  "/admin/signups/event/add/"))
                username = self.selenium.find_element_by_id("id_username")
                username.send_keys("admin")
                password = self.selenium.find_element_by_id("id_password")
                password.send_keys("admin")


                self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
#		self.selenium.get('%s%s' % (self.live_server_url, "/admin/signups/event/add/"))
                title = self.selenium.find_element_by_name("title")
                title.send_keys("Monster Trucks")
                eventtype = self.selenium.find_element_by_name("type")
                eventtype.send_keys("Motor Sport?")
                venue = self.selenium.find_element_by_name("venue")
                venue.send_keys("Wild Horse Pass")
                thedate = self.selenium.find_element_by_name("date")
                thedate.send_keys("2014-12-25")
                thetime = self.selenium.find_element_by_name("time")
                thetime.send_keys("00:42:42")
                num1 = self.selenium.find_element_by_name("current_avail")
                num1.send_keys("42")
                num2 = self.selenium.find_element_by_name("total_avail")
                num2.send_keys("424242")
                self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

	def test_signup(self):
		self.selenium.get('%s%s' % (self.live_server_url,  "/"))
                self.selenium.get('%s%s' % (self.live_server_url,  "/signup/"))

                username = self.selenium.find_element_by_name("username")
                username.send_keys("test")
                password = self.selenium.find_element_by_name("password1")
                password.send_keys("test")
                password = self.selenium.find_element_by_name("password2")
                password.send_keys("test")
                email = self.selenium.find_element_by_name("email")
                email.send_keys("test@test.test")
                self.selenium.find_element_by_xpath('//input[@value="Submit"]').click()

	def test_login(self):
                self.selenium.get('%s%s' % (self.live_server_url,  "/"))
                username = self.selenium.find_element_by_name("username")
                username.send_keys("test")
                password = self.selenium.find_element_by_name("password")
                password.send_keys("test")
                self.selenium.find_element_by_xpath('//input[@value="Log In"]').click()
