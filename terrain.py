#This is part of the setup for using lettuce to run our functional tests.  Some (read all) assembly may be required.
#These tests are entirely untested.  Use at your own peril until they are verified to be coded properly.

from django.core.management import call_command
from django.test.simple import DjangoTestSuiteRunner

from lettuce import before, after, world
from logging import getLogger
from selenium import webdriver

logger=getLogger(__name__)
logger.info("Loading terrain file.")

@before.runserver
def setup_database(real_server):
  '''
  Setup DB, sync DB
  '''
  logger.info("Setting up test database.")
  
  world.test_runner=DjangoTestSuiteRunner(interactive=False)
  djangoTestSuiteRunner.setup_test_environment(world.test_runner)'
  world.created_db=DjangoTestSuiteRunner.setup_databases(world.test_runner)
  
  call_command('syncdb', interactive=False, verbosity=0)
  
@after.runserver
def teardown_database(real_server):
  '''
  Destroys test database
  '''
  logger.info("Destroying test database.")
  
  DjangoTestSuiteRunner.teardown_databases(world.test_runner, world.creaded_db)
  
@before.all
def setup_browser():
  world.browser= webdriver.Firefox()

@after.all
def teardown_browser(total):
  World.browser.quit()
