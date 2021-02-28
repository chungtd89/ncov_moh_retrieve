def requirements_check(package):
    try:
        __import__("pandas")
        __import__("bs4")
        __import__("selenium")
        __import__("webdriver_manager")
        __import__("ftfy")
        __import__("numpy")
    except ImportError:
        import sys
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "pandas"])
        __import__("pandas")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "bs4"])
        __import__("bs4")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "selenium"])
        __import__("selenium")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "webdriver-manager"])
        __import__("webdriver_manager")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "ftfy"])
        __import__("ftfy")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "numpy"])
        __import__("numpy")


requirements_check("pandas")
requirements_check("bs4")
requirements_check("selenium")
requirements_check("webdriver_manager")
requirements_check("ftfy")
requirements_check("numpy")

# Import packages
import pandas as pd
from selenium import webdriver
from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ftfy import fix_encoding
import numpy as np
import time
import csv
import os