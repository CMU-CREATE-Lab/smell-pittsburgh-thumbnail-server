# smell-pittsburgh-thumbnail-server

This is a thumbnail server for Smell Pittsburgh. The following assumes a system-wide install of python3 packages.

```sh
pip3 install flask
pip3 install uwsgi
sh production.sh
curl localhost:8080
# Should get the "Hey Paul!" message
```
