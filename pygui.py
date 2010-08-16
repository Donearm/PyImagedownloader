#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008, Gianluca Fiore
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,          
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            
#   GNU General Public License for more details.                           
#                                                                         
#   You should have received a copy of the GNU General Public License        
#   along with this program; if not, write to the Free Software              
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#############################################################################

__author__ = "Gianluca Fiore"
__license__ = "GPL"
__version__ = "1.3"
__date__ = "11082010"
__email__ = "forod.g@gmail.com"

import sys
from os.path import abspath
import threading
import gobject
# importing local modules
import http_connector
# importing config file variables
#from pyimagedownloader import download_url, basedir, embed, poster
from pyimagedownloader import ImageHostParser
from savesource import save_source

try:
    import pygtk
    # Gtk2 if possible
    pygtk.require("2.0")
    try:
        import gtk
        import gobject
        # Enable threading
        gobject.threads_init()
    except:
        print("Gtk was not available, install it or use command line mode...")
        sys.exit(1)
except:
    print("PyGtk was not available, install it or use command line mode...")
    sys.exit(1)





# PyGtk gui class
class Gui():
    def __init__(self, url, basedir, embed=False, poster=""):
        """ Main window class """
        
        self.url = url
        self.basedir = basedir
        self.embed = embed
        self.poster = poster

        self.window = gtk.Window()
        self.window.set_title("Pyimagedownloader %s" % __version__)
        self.window.set_size_request(500, 200)
        self.window.connect("delete-event", self.close)
        self.window.connect("destroy", self.close)

        # let's have a scrobllbar
        self.scrolledwindow = gtk.ScrolledWindow()
        self.scrolledwindow.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.scrolledwindow.set_size_request(400, 150)

        # ListStore and its TreeView
        self.liststore = gtk.ListStore(str)
        self.treeview = gtk.TreeView(self.liststore)
        self.treeview.set_fixed_height_mode(True) # all columns have same height
        # CellRender to render the data
        self.cell = gtk.CellRendererText()
        # TreeViewColumn to display text in a single column
        self.tvcolumn = gtk.TreeViewColumn('URL', self.cell, text=0)
        # this must be set for set_fixed_height_mode of TreeView to work
        self.tvcolumn.set_sizing(gtk.TREE_VIEW_COLUMN_FIXED)
        self.tvcolumn.set_clickable(False) # column header won't be clickable
        # add column to the treeview
        self.treeview.append_column(self.tvcolumn)
        # make treeview searchable and allow sorting
        self.treeview.set_search_column(0)
        self.tvcolumn.set_sort_column_id(0)
        # add grid lines
        self.treeview.set_grid_lines(gtk.TREE_VIEW_GRID_LINES_HORIZONTAL)
        # make the column header not clickable
        self.tvcolumn.set_clickable(False)
        


        # Clipboard
        self.clipboard = gtk.Clipboard(gtk.gdk.display_get_default(), "PRIMARY")

        # Buttons
        self.cut_button = gtk.Button("Cut")
        self.copy_button = gtk.Button("Copy")
        self.paste_button = gtk.Button("Paste")
        self.start_button = gtk.Button("Start")
        self.close_button = gtk.Button("Close")
        self.cut_button.set_size_request(50, 50)
        self.copy_button.set_size_request(50, 50)
        self.paste_button.set_size_request(50, 50)
        self.start_button.set_size_request(50, 50)
        self.close_button.set_size_request(50, 50)

        self.hbox = gtk.HBox(False, 5)
        self.vbox = gtk.VBox(False, 5)

        self.vbox.pack_start(self.scrolledwindow, True)
        self.hbox.pack_start(self.start_button)
        self.hbox.pack_start(self.cut_button)
        self.hbox.pack_start(self.copy_button)
        self.hbox.pack_start(self.paste_button)
        self.hbox.pack_start(self.close_button)
        self.vbox.pack_start(self.hbox)
        self.scrolledwindow.add(self.treeview)
        self.window.add(self.vbox)

        self.cut_button.connect("clicked", self.copy, "cut")
        self.copy_button.connect("clicked", self.copy, "copy")
        self.paste_button.connect("clicked", self.paste)
        self.start_button.connect("clicked", self.download_url, self.url, self.basedir, self.embed, self.poster)
        self.close_button.connect("clicked", self.close)

        # Tooltips
        self.cut_button.set_tooltip_text("Cut url(s)")
        self.copy_button.set_tooltip_text("Copy url(s) into the clipboard")
        self.paste_button.set_tooltip_text("Paste url(s) from the clipboard")

        self.window.show_all()

        gtk.main()

    def close(self, widget):
        gtk.main_quit()
        sys.exit(1)

    def copy(self, widget, mode):
        """ copy/cut function for the clipboard"""
        # get the current selection from TreeView
        selection = self.treeview.get_selection()
        result = selection.get_selected()
        if result:
            # tuple with the model (ListStore in this case) and TreeIter
            # referring to the selected row
            model, iter = result
        self.clipboard.set_text(model.get_value(iter, 0))

        if mode == "cut":
            model.remove(iter)

    def paste(self, widget):
        """ paste function for the clipboard"""
        text = self.clipboard.wait_for_text()
        if text != None:
            self.liststore.append([text])

    def download_url(self, widget, url, basedir="", embed="", poster=""):

        Rpage = http_connector.connector(url)

        # Parse the page for images
        parser = ImageHostParser(Rpage, 'a', 'href')
        if embed:
            # do we need to search for embedded images then?
            # Note: at the moment it downloads thumbnails too
            print("Searching for embedded images")
            print("")
            parser.which_host('img', 'src')

        # Generate the directory for the source file and the images downloaded
        save_source(url, basedir, creditor=poster)


class GThread(threading.Thread):
    def __init__(self):
        super(GThread, self).__init__()
        self.quit = False

    def run(self, func, *args, **kwargs):
        gobject.idle_add(func, *args, **kwargs)





if __name__ == "__main__":
    pygui = Gui()
    gtk.main()
