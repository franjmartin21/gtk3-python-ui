import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from servicio.desbloqueame import Desbloqueame


class Handlers:
    def move_car(self):
        print("This method has to move the car")


class TableroUI:

    CSS_CLASS_COCHE_OBJETIVO = 'red-car'

    CSS_CLASS_COCHES_ESTACIONADOS = 'blue-car'

    def __init__(self):
        self.desbloqueame = Desbloqueame()
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/pytemp3.glade")
        self.builder.connect_signals(Handlers())
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_path('css/style.css')
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        self.load_cars()
        window = self.builder.get_object("window1")
        window.show_all()
        Gtk.main()


    def load_cars(self):
        '''
        Este metodo deberia de cargar los coches de la clase
        :return: 
        '''
        coche_objetivo = self.desbloqueame.recuperar_coche_objectivo()
        self.load_car(coche_objetivo[0], coche_objetivo[1], coche_objetivo[2], coche_objetivo[3], self.CSS_CLASS_COCHE_OBJETIVO)
        coches_estacionados = self.desbloqueame.recuperar_coches_estacionados()
        for coche in coches_estacionados:
            self.load_car(coche[0], coche[1], coche[2], coche[3], self.CSS_CLASS_COCHES_ESTACIONADOS)

    def load_car(self, horientacion, columna, fila, tamanio, css_class):
        tablero_grid = self.builder.get_object("tablero_grid")
        button = Gtk.Button()
        ctx = button.get_style_context()
        ctx.add_class(css_class)
        if(horientacion == 'V'):
            tablero_grid.attach(button, int(columna), int(fila), 1, int(tamanio))

        if(horientacion == 'H'):
            tablero_grid.attach(button, int(columna), int(fila), int(tamanio), 1)



tablero_ui = TableroUI()

'''
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
'''