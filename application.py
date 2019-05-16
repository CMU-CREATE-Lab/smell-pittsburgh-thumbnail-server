from flask import Flask, send_file
from selenium import webdriver
import os
import time

app = Flask(__name__)

p_cache = "/var/www/smell-pittsburgh-thumbnail-server/cache/"

# Check if a file exists
def is_file_here(file_path):
    return os.path.isfile(file_path)

@app.route("/")
def hello_world():
    return "Hey Paul!"

@app.route("/thumbnail")
def thumbnail():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--hide-scrollbars")
    browser = webdriver.Chrome(chrome_options=options)
    browser.set_window_size(1920, 1080)
    browser.get("http://api.smellpittsburgh.org/visualization")
    file_name = "screenshot.png"
    time.sleep(5)
    play_btn = browser.find_element_by_id("playback-btn")
    play_btn.click()
    time.sleep(2)
    browser.save_screenshot(p_cache + file_name)
    browser.close()
    return send_file(p_cache + file_name, mimetype="image/png")
