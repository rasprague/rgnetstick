# rgnetstick
simple frontend for netstick

Built on top of
- netstick https://github.com/moslevin/netstick
- pyxel https://github.com/kitao/pyxel
- pyxel_menu https://son-link.github.io/PyxelMenu/

Building:
```
$ git clone https://github.com/rasprague/rgnetstick.git
$ cd rgnetstick
$ # compile netstick binary
$ # do a cross-compile here as needed
$ cd netstick
$ cmake ./CMakeLists.txt
$ make
$ cd ..
$ # build rgnetstick
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
$ pyxel package . rgnetstick.py
$ # output is rgnetstick.pyxelapp
```
