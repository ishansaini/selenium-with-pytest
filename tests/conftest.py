"""
This module contains shared fixtures.
"""

import json
import pytest
from selenium import webdriver

@pytest.fixture
def config(scope='session'):

  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome', 'Headless Firefox']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config

@pytest.fixture
def browser(config):

  # Initialize the WebDriver instance
  if config['browser'] == 'Firefox':
    b = webdriver.Firefox()
  elif config['browser'] == 'Chrome':
    b = webdriver.Chrome()
  elif config['browser'] == 'Headless Chrome':
    opts = webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = webdriver.Chrome(options=opts)
  elif config['browser'] == 'Headless Firefox':
    opts = webdriver.FirefoxOptions()
    opts.add_argument('-headless')
    b = webdriver.Firefox(options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')
  
  # Make its calls wait up to 10 seconds for elements to appear
  b.implicitly_wait(10)

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
