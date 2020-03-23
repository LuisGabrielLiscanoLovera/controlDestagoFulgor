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
    def handle_select(self, *args):
        print("Select:", args)
    def build(self):
        return Builder.load_file('pantalla/drawer.kv')# Builder.load_string(KV)
#run
if __name__ == '__main__':ControlDestajo().run()
