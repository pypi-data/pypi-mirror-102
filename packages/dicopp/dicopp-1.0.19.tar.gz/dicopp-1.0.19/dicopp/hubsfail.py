
from . import sets
from . import base

import appdirs
import os.path
import pathlib
def get_client_dir():
	return pathlib.Path(appdirs.user_data_dir(base.pkgname))
def get_client():
	return os.path.join(get_client_dir(),'hublist.xml')

from gi.repository import Gtk

file=Gtk.EntryBuffer()
def get_file():
	f=file.get_text()
	if not f:
		return get_client()
	return os.path.expandvars(f)

def store(d):
	d['hub_file_fallback']=file.get_text()
def restore(d):
	f=d['hub_file_fallback']
	if not f:
		f=get_client()
		if not os.path.exists(f):
			d=get_client_dir()
			d.mkdir(exist_ok=True)
			with open(f, "w") as write_file: #"wb" writes 0
				from . import hublist
				write_file.write(hublist.a)
	else:
		file.set_text(f,-1)
def confs_loc():
	en=sets.entries(file)
	if file.get_text():
		return en
	bx=Gtk.Box()
	bx.append(en)
	bx.append(Gtk.Label(label=get_client()))
	return bx