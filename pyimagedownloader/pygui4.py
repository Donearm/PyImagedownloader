#!/usr/bin/env python2
# -*- coding: utf-8 -*-
###############################################################################
# Copyright (c) 2008-2013, Gianluca Fiore
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
__version__ = "1.6"
__date__ = "15072011"
__email__ = "forod.g@gmail.com"

import sys
from PyQt4 import QtGui, QtCore

# importing local modules
import http_connector
import savesource
from pyimagedownloader import ImageHostParser

app = QtGui.QApplication(sys.argv)

# PyQt4 gui class
class Gui(QtGui.QWidget):
    """Main window class"""
    def __init__(self, basedir, embed, poster):
        QtGui.QWidget.__init__(self)
        
        self.basedir = basedir
        self.embed = embed
        self.poster = poster

        self.resize(500, 200)
        self.setWindowTitle("PyImagedownloader %s" % __version__)

        # make a statusbar
        self.statusbar = QtGui.QStatusBar()

        # connect to system's clipboard
        self.clip = QtGui.QApplication.clipboard()

        # let's build the menu
        self.exit_action = QtGui.QAction('Exit', self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setStatusTip('Exit application')
        self.connect(self.exit_action, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.basedir_action = QtGui.QAction('Choose directory', self)
        self.basedir_action.setShortcut("Ctrl+d")
        self.basedir_action.setStatusTip('Choose output directory')
        self.connect(self.basedir_action, QtCore.SIGNAL('triggered()'), self.dir_dialog)

        self.filelist_action = QtGui.QAction('Load file', self)
        self.filelist_action.setShortcut("Ctrl+O")
        self.filelist_action.setStatusTip('Load a file with a list of links')
        self.connect(self.filelist_action, QtCore.SIGNAL('triggered()'), self.filelist_dialog)

        self.about_action = QtGui.QAction('About', self)
        self.about_action.setStatusTip('About the program')
        self.connect(self.about_action, QtCore.SIGNAL('triggered()'), self.about_dialog)

        self.menubar = QtGui.QMenuBar()
        self.filemenu = self.menubar.addMenu('&File')
        self.filemenu.addAction(self.basedir_action)
        self.filemenu.addAction(self.filelist_action)
        self.filemenu.addAction(self.exit_action)
        self.helpmenu = self.menubar.addMenu('&Help')
        self.helpmenu.addAction(self.about_action)

        # ListView
        self.listview = QtGui.QListWidget()
        self.listview.Flow(QtGui.QListWidget.TopToBottom)
        self.listview.Movement(QtGui.QListWidget.Free) # items can be freely moved
        self.listview.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        # Buttons
        self.start_button = QtGui.QPushButton("Start")
        self.cut_button = QtGui.QPushButton("Cut")
        self.paste_button = QtGui.QPushButton("Paste")
        self.close_button = QtGui.QPushButton("Close")

#        self.connect(self.start_button, QtCore.SIGNAL('clicked()'), self.listview_iterator)
#        self.connect(self.start_button, QtCore.SIGNAL('clicked()'), self.sequential_downloader)
        self.connect(self.start_button, QtCore.SIGNAL('clicked()'), self.sequential_downloader)
        
        self.connect(self.cut_button, QtCore.SIGNAL('clicked()'), self.cut)
        self.connect(self.paste_button, QtCore.SIGNAL('clicked()'), self.paste)
        self.connect(self.close_button, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))

        # Layouts
        self.hbox = QtGui.QHBoxLayout()
        self.vbox = QtGui.QVBoxLayout()

        self.hbox.addWidget(self.start_button)
        self.hbox.addWidget(self.cut_button)
        self.hbox.addWidget(self.paste_button)
        self.hbox.addWidget(self.close_button)

        self.vbox.addWidget(self.menubar)
        self.vbox.addWidget(self.listview)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.statusbar)
        self.setLayout(self.vbox)

        # create a threads pool
        self.thread_pool = []

        # show gui and start QApplication loop
        self.show()
        sys.exit(app.exec_())

    def cut(self):
        """Cut selection and put into system's clipboard"""
        for i in self.listview.selectedItems():
            txt = self.listview.takeItem(self.listview.row(i))
            self.clip.setText(txt.text(), mode=QtGui.QClipboard.Selection)
        self.statusbar.showMessage("Cut!", 500)
    
    def paste(self):
        """Paste clipboard's contents into the application"""
        contents = self.clip.mimeData(mode=QtGui.QClipboard.Selection)
        if unicode(QtCore.QString.fromUtf8(contents.text())).isspace() or not contents.text():
            # contents are either empty or containing only spaces/newlines/tabs
            self.statusbar.showMessage("Nothing to paste", 500)
            return
        else:
            if contents.hasText:
                self.listview.addItem(contents.text())
                self.statusbar.showMessage("Clipboard pasted!", 1000)
            elif contents.hasUrls:
                self.listview.addItem(contents.urls())
                self.statusbar.showMessage("Clipboard pasted!", 1000)
            else:
                return

    def dir_dialog(self):
        """Choose basedir dialog"""
        self.basedir = str(QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory', 
            self.basedir, QtGui.QFileDialog.ShowDirsOnly))

    def filelist_dialog(self):
        """Import a file with a list of urls dialog"""
        filelist = QtGui.QFileDialog.getOpenFileName(self, 'Select file', 
                self.basedir)
        try:
            with open(filelist, "r") as f:
                for line in f:
                    self.listview.addItem(line.strip("\r\n"))
        except IOError:
            # don't do anything for IO errors
            return
    
    def about_dialog(self):
        """A message box showing info about the program"""
        msgbox = QtGui.QMessageBox()
        msgbox.about(self, 'About: PyImagedownloader', "PyImagedownloader " + __version__ + "\nCopyright 2008-2011\nGianluca Fiore")

    def clean_listview_item(self, row):
        """remove the row from a listview"""
        self.listview.takeItem(row)

    def download_url(self, url, savedirectory="", embed="", poster=""):
        
        connector = http_connector.Connector()
        r_page = connector.reqhandler(url, 1)
        print(r_page)
        if r_page == '':
            raise IOError("Url not valid or nonexistent")

        # be sure to have a url as a string and not as a list for savesource.py
        url_string = connector.check_string_or_list(url)
        # Generate the directory for the source file and the images downloaded
        # Plus, return savedirectory as basedir + page title, so to save images
        # on a per-site basis
        source_saver = savesource.SaveSource(r_page, savedirectory, url_string, creditor=poster)
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
        
#        self.emit(QtCore.SIGNAL('downloadDone(QString)'), row)
    

    def sequential_downloader(self):
#        self.sqdownloader = SequentialDownloader(self.listview, self.basedir, 
#                self.embed, self.poster)
#        self.sqdownloader.start()

        for r in range(0, self.listview.count()):
            url = self.listview.item(r).text()
#            t = GenericThread(self.download_url, url, r, self.basedir, self.embed, self.poster)
#            self.thread_pool.append(GenericThread(self.download_url, url, r, self.basedir, self.embed, self.poster))
            self.thread_pool.append(SequentialDownloader(self.listview, self.basedir, self.embed, self.poster))
#            self.thread_pool.append(GenericThread(self.test, url, r, self.basedir, self.embed, self.poster))
#            self.disconnect(self, QtCore.SIGNAL('downloadDone(QString)'), self.clean_listview_item)
#            self.connect(self, QtCore.SIGNAL('downloadDone(QString)'), self.clean_listview_item)

#            self.thread_pool[len(self.thread_pool)-1].start()
            try:
                self.thread_pool[r].start()
            except KeyboardInterrupt:
                waiting = self.thread_pool[r].wait()
                while not waiting:
                    self.statusbar.showMessage("Waiting to stop current executing download...")
#            t.start()

        print(self.thread_pool)



class GenericThread(QtCore.QThread):
#class GenericThread(threading.Thread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
#        threading.Thread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()

    def run(self):
        self.function(*self.args, **self.kwargs)
        return



class SequentialDownloader(QtCore.QThread):
    def __init__(self, listview, basedir="", embed="", poster="", parent=None):
        QtCore.QThread.__init__(self)
        self.listview = listview
        self.basedir = basedir
        self.embed = embed
        self.poster = poster

    def __del__(self):
        self.wait()

    def run(self):
        for i in range(0, self.listview.count()):
            url = self.listview.item(i).text()
            print(url)
            self.download_url(url, self.basedir, self.embed)
            self.emit(QtCore.SIGNAL("downloadDone(int)"), i)
#            self.listview.takeItem(i)


    def download_url(self, url, savedirectory, embed="", poster=""):
        
        connector = http_connector.Connector()
        r_page = connector.reqhandler(url, 1)
        if r_page == '':
            raise IOError("Url not valid or nonexistent")

#        # be sure to have a url as a string and not as a list for savesource.py
#        url_string = connector.check_string_or_list(url)
        # Generate the directory for the source file and the images downloaded
        # Plus, return savedirectory as basedir + page title, so to save images
        # on a per-site basis
#        source_saver = savesource.SaveSource(r_page, savedirectory, url_string, creditor=poster)
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
    pygui.show()

    sys.exit(app.exec_())
