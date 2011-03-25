#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2011, Gianluca Fiore
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
__version__ = "1.5"
__date__ = "25032011"
__email__ = "forod.g@gmail.com"

import sys
import threading
# importing local modules
import http_connector
import savesource
from os import rename
from os.path import abspath, dirname
# importing config file variables
#from pyimagedownloader import download_url, basedir, embed, poster
from pyimagedownloader import ImageHostParser

try:
    import pygtk
    # Gtk2 if possible
    pygtk.require("2.0")
    try:
        import gtk
        import gobject
        # Enable threading
        gobject.threads_init()
        gtk.gdk.threads_init()
    except:
        print("Gtk was not available, install it or use command line mode...")
        sys.exit(1)
except:
    print("PyGtk was not available, install it or use command line mode...")
    sys.exit(1)





# PyGtk gui class
class Gui():
    def __init__(self, basedir, embed=False, poster=""):
        """ Main window class """
        
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
        self.basedir_button = gtk.Button("Set save directory")
        self.filelist_button = gtk.Button("Load file")
        self.cut_button = gtk.Button("Cut")
        self.copy_button = gtk.Button("Copy")
        self.paste_button = gtk.Button("Paste")
        self.start_button = gtk.Button("Start")
        self.close_button = gtk.Button("Close")
        self.basedir_button.set_size_request(30, 30)
        self.filelist_button.set_size_request(30, 30)
        self.cut_button.set_size_request(50, 50)
        self.copy_button.set_size_request(50, 50)
        self.paste_button.set_size_request(50, 50)
        self.start_button.set_size_request(50, 50)
        self.close_button.set_size_request(50, 50)

        self.hbox1 = gtk.HBox(False, 5)
        self.hbox2 = gtk.HBox(False, 5)
        self.vbox = gtk.VBox(False, 5)

        self.hbox1.pack_start(self.basedir_button)
        self.hbox1.pack_start(self.filelist_button)
        self.vbox.pack_start(self.hbox1)
        self.vbox.pack_start(self.scrolledwindow)
        self.hbox2.pack_start(self.start_button)
        self.hbox2.pack_start(self.cut_button)
        self.hbox2.pack_start(self.copy_button)
        self.hbox2.pack_start(self.paste_button)
        self.hbox2.pack_start(self.close_button)
        self.vbox.pack_start(self.hbox2)
        self.scrolledwindow.add(self.treeview)
        self.window.add(self.vbox)

        self.basedir_button.connect("clicked", self.basedir_dialog)
        self.filelist_button.connect("clicked", self.filelist_dialog)
        self.cut_button.connect("clicked", self.copy, "cut")
        self.copy_button.connect("clicked", self.copy, "copy")
        self.paste_button.connect("clicked", self.paste)
        self.start_button.connect("clicked", self.sequential_downloader, self.liststore, self.basedir, self.embed, self.poster)
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
        model, treeiter = selection.get_selected()
        self.clipboard.set_text(model.get_value(treeiter, 0))

        if mode == "cut":
            model.remove(treeiter)

    def paste(self, widget):
        """ paste function for the clipboard"""
        text = self.clipboard.wait_for_text()
        if text != None:
            self.liststore.append([text])

    def basedir_dialog(self, widget):
        # make a FileChooserDialog
        self.chooser_dialog = gtk.FileChooserDialog(title="Select download directory...",
                action=gtk.FILE_CHOOSER_ACTION_CREATE_FOLDER,
                buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        self.chooser_dialog.set_current_folder(str(self.basedir))

        self.chooser_dialog.set_default_response(gtk.RESPONSE_OK)
        # run it
        if self.chooser_dialog.run() == gtk.RESPONSE_OK:
            print(self.chooser_dialog.get_current_folder())
            self.basedir = self.chooser_dialog.get_current_folder()
        else:
            print(self.chooser_dialog.get_current_folder())

        self.chooser_dialog.destroy()

    def filelist_dialog(self, widget):
        self.filelist_dialog = gtk.FileChooserDialog(title="Load file with URLs...",
                action=gtk.FILE_CHOOSER_ACTION_OPEN,
                buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        
        response = self.filelist_dialog.run()
        if response == gtk.RESPONSE_OK:
            filelist = self.filelist_dialog.get_filename()
            # call the method to add every url from filelist to the liststore
            self.populate_liststore(self.filelist_dialog, self.liststore, filelist)
            self.filelist_dialog.destroy()
            return filelist
        elif response == gtk.RESPONSE_CANCEL:
            self.filelist_dialog.destroy()
        else:
            self.filelist_dialog.destroy()

    def populate_liststore(self, widget, liststore, filelist):
        """populate the given liststore with elements from filelist"""
        bckp_f = dirname(abspath(filelist)) + '/' + 'list.bckp'
        with open(filelist, "r") as f:
            line = f.readlines()
            with open(bckp_f, "w") as b:
                for u in line:
                    if u.startswith('#'):
                        # write back commented lines
                        b.write(u)
                    else:
                        # write as commented lines added to the liststore
                        liststore.append([u.strip('\n')])
                        b.write('#' + u)
    
        rename(abspath(b.name), abspath(f.name))


    def sequential_downloader(self, widget, liststore, basedir="", embed="", poster=""):
        """instantiate a SequentialDownloader object and execute run()"""
        self.sqdownloader = SequentialDownloader(widget, liststore, basedir, embed, poster)
        self.sqdownloader.start()



class SequentialDownloader(threading.Thread):
    """We use a class, inheriting from threading.Thread, to handle all the 
    downloads and liststore updating indipendently from the Gui"""
    def __init__(self, widget, liststore, basedir="", embed="", poster=""):
        threading.Thread.__init__(self)
        self.widget = widget
        self.liststore = liststore
        self.basedir = basedir
        self.embed = embed
        self.poster = poster

    def run(self):
        r = 0
        col = 0
        for row in self.liststore:
            self.download_url(self.liststore[r][col], self.basedir, self.embed, self.poster)
            self.liststore[r][col] = ""
            r += 1
        self.liststore.clear()

    def download_url(self, url, savedirectory, embed="", poster=""):
        
        connector = http_connector.Connector()
        r_page = connector.reqhandler(url, 1)


        # Generate the directory for the source file and the images downloaded
        # Plus, return savedirectory as basedir + page title, so to save images
        # on a per-site basis
        source_saver = savesource.SaveSource(r_page, savedirectory, url, creditor=poster)
        savedirectory = source_saver.link_save()

        # Parse the page for images
        parser = ImageHostParser(r_page, 'a', 'href', savedirectory)
        if embed:
            # do we need to search for embedded images then?
            # Note: at the moment it downloads thumbnails too
            print("Searching for embedded images")
            print("")
            embed_links = parser.get_all_links('img', 'src')
            parser.which_host(embed_links, 'src')



if __name__ == "__main__":
    pygui = Gui()
