""" from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.theming import ThemeManager
Builder.load_string(
    '''
#:import toast kivymd.toast.toast
<MyRoot@BoxLayout>
    orientation: 'vertical'
    MDDropDownItem:
        id: dropdown_item
        items: app.items
        dropdown_bg: [1, 1, 1, 1]
    MDRaisedButton:
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        text: 'Chek Item'
        on_release: toast(dropdown_item.current_item)
''')
class Test(MDApp):
    def build(self):
        self.items = [f"Item {i}" for i in range(5)]
        return Factory.MyRoot()
Test().run()



"""
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


#from kivy.properties import ObjectProperty
from kivy.properties import (
    ObjectProperty,
    ListProperty,
    StringProperty,
    NumericProperty,
    BooleanProperty,
)
from kivymd.app import MDApp
import database as DB

Data=DB.dataBase()

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer     = ObjectProperty()

class ControlDestajo(MDApp):

    def integrante(self,NombreCompleto,NumDocumento,FotoIntegrante,FotoFirma):
        Data.AddIntegrante(NombreCompleto,NumDocumento,FotoIntegrante,FotoFirma)
    def lote(self,LoteTotal,LoteFaltante,op,NumReferencia,FotoPrenda1,FotoPrenda2,DetalleLote,Estado):
        Data.AddLote(LoteTotal,LoteFaltante,op,NumReferencia,FotoPrenda1,FotoPrenda2,DetalleLote,Estado)
    def tarea(self,Integrante,Operacion,Lote,CantidadTomada,Talla,CantidadNoFnalizada):
        Data.AddTarea(Integrante,Operacion,Lote,CantidadTomada,Talla,CantidadNoFnalizada)
    def estado(self,NombreEstado,DetalleEstado):
        Data.AddEstado(NombreEstado,DetalleEstado)
    def operacion(self,nombreOperacion,precioValor,duracionOperacion,aproxALDia,fotoOperacion,detalleOperacion):        
        #if len(nombreOperacion)==0 or len(precioValor) ==0 or len(duracionOperacion) ==0 or len(aproxALDia) ==0 or len (fotoOperacion) ==0 or len (detalleOperacion) ==0:print ("error")
        Data.AddOperacion(nombreOperacion,precioValor,duracionOperacion,aproxALDia,fotoOperacion,detalleOperacion)
    #select
    def selectEstado(self):return Data.slctEstado()
    
    def build(self):return Builder.load_file('pantalla/drawer.kv')# Builder.load_string(KV)
#run
if __name__ == '__main__':ControlDestajo().run()
