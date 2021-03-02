# built-in packages
import os
import pip


def requirements_check(package):
    try:
        __import__("pandas")
        __import__("bs4")
        __import__("selenium")
        __import__("webdriver_manager")
        __import__("ftfy")
        __import__("numpy")
        __import__("calmap")
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
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "calmap"])
        __import__("calmap")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "requests"])
        __import__("requests")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "geopy"])
        __import__("geopy")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "seaborn"])
        __import__("seaborn")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "matplotlib"])
        __import__("matplotlib")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "folium"])
        __import__("folium")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "matplotlib"])
        __import__("matplotlib")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', "plotly"])
        __import__("plotly")


requirements_check("pandas")
requirements_check("bs4")
requirements_check("selenium")
requirements_check("webdriver_manager")
requirements_check("ftfy")
requirements_check("numpy")
requirements_check("calmap")
requirements_check("geopy")
requirements_check("seaborn")
requirements_check("matplotlib")
requirements_check("folium")
requirements_check("matplotlib")
requirements_check("plotly")

