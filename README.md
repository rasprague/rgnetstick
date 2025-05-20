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
$ python3 -m venv .venv
$ . .venv/bin/activate
$ cd netstick
$ cmake ./CMakeLists.txt
$ make
$ cd ..
$ pyxel package . rgnetstick.py
$ pyxel app2exe rgnetstick.pyxapp
```
