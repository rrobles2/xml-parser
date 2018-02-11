import os
import sys
from lxml import etree
from StringIO import StringIO
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk, GObject, Gdk

from src.Class import Class

CUSTOM_RELATIVE_DIRECTORY = os.getcwd()[:-6] + "Custom/"
BOX_SPACING = 5
PADDING = 5

class Part:
    def __init__(self, inName):
      self.filename = inName

class Session:
  def __init__(self):
    self.parts=[]
    self.types=[]
    self.classes=[]
      
  def loadFile(self, inFile):
      print "Loading "+inFile+" ..."
      file = CUSTOM_RELATIVE_DIRECTORY+inFile
      f = open(file)
      xml = f.read()
      f.close()
      
      tree = etree.parse(StringIO(xml))
      root = tree.getroot()
      
#      for rulesElement in root.findall('RulesElement'):
#        if not rulesElement.get('type') in self.types:
#          self.types.append(rulesElement.get('type'))
#          print rulesElement.get('type')
      for rulesElement in root.findall('RulesElement'):
        if rulesElement.get('type') == "Class":
          self.classParse(rulesElement)
        

  def classParse(self, classElement):
    print "\n\n------------\nFound class "+classElement.get('name')
    curClass=Class(classElement.get('name'))
    
    curClass.parseFields(classElement)
    self.classes.append(curClass)

  def loadFileConfig(self):
      file = CUSTOM_RELATIVE_DIRECTORY+"WotC.index"
      f = open(file)
      xml = f.read()
      f.close()

      tree = etree.parse(StringIO(xml))
      root = tree.getroot()
    
      for part in root.findall('Part'):
        self.parts.append(Part(part.find('Filename').text.rstrip().lstrip()))
        

class Application(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, application_id="char.build.editor",
                         flags=Gio.ApplicationFlags.FLAGS_NONE,
                         **kwargs)
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        Gtk.Application.do_activate(self)
        if not self.window:
            self.window = AppWindow(application=self, title="Character Builder Editor")
        self.window.present()
        self.window.show_all()

class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):
        super(AppWindow, self).__init__(*args, **kwargs)

        session = Session()
        print("Loading existing files...")
        session.loadFileConfig()
        for part in session.parts:
          session.loadFile(part.filename)
        
        self.windowBox = Gtk.Box(spacing=BOX_SPACING)
        self.windowBox.pack_start(Gtk.Label("WotC.index loaded successfully.  "+(str)(len(session.parts))+" files found."), False, False, PADDING)
        self.add(self.windowBox)
        self.show_all()
        
if __name__ == "__main__":
    
    app = Application()
    app.run(sys.argv)