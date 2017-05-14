import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def printHola(self, button):
        print("Hello World!")

    def printPosition(self):
        print("endDrag")



builder = Gtk.Builder()
builder.add_from_file("glade/pytemp3.glade")
builder.connect_signals(Handler())
niveles_txt = builder.get_object("niveles_txt")
tablero_grid = builder.get_object("tablero_grid")
label1_1 = builder.get_object("label1_1")
label1_1.destroy()
button1_1 = Gtk.Button()
button1_4 = Gtk.Button()

cssProvider = Gtk.CssProvider()
cssProvider.load_from_path('css/style.css')
screen = Gdk.Screen.get_default()
styleContext = Gtk.StyleContext()
styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

tablero_grid.attach(button1_1,0,0,1,2)

tablero_grid.attach(button1_4,4,0,1,2)


niveles_txt.set_text("1234")
window = builder.get_object("window1")
window.show_all()

Gtk.main()