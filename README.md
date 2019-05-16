# smell-pittsburgh-thumbnail-server

This is a thumbnail server for Smell Pittsburgh. The following assumes a system-wide install of python3 packages.
```sh
sudo pip3 install flask
sudo pip3 install uwsgi
sh production.sh
curl localhost:8080
# Should get the "Hey Paul!" message
```

Download Chrome, install pending dependencies, and then install Chrome.
```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get -f install
sudo dpkg -i google-chrome-stable_current_amd64.deb
google-chrome-stable --version
```

Download Chrome driver from [here](https://sites.google.com/a/chromium.org/chromedriver/) that matches the installed Chrome version and move it to /usr/local/bin/.
```sh
wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/local/bin/
chromedriver --version
```

Install selenium and pyvirtualdisplay.
```sh
sudo pip3 install selenium
sudo pip3 install pyvirtualdisplay
```
