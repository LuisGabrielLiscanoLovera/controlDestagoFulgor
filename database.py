# -*- coding: utf-8 -*-
from os import path
from sqlalchemy import create_engine,Table, Column,ForeignKey, Integer, Binary,DateTime,String, MetaData
from sqlalchemy.sql import text, select 
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker as SM
from datetime import datetime as DT

engine          = create_engine('sqlite:///data/ctrlDestajo.db', echo=True)
conn            = engine.connect()
session_factory = SM(bind=engine)
session         = session_factory()

if not path.exists('/data/ctrlDestajo.db'):
    meta   = MetaData()
    estado =    Table('estado', meta, 
                Column('id_estado', Integer, primary_key=True),
                Column('fecha',DateTime),
                Column('estado', String), 
                Column('detalle', String),)
                    
    lote   =    Table('lote',meta,
                Column('id_lote', Integer, primary_key=True),
                Column('loteTotal', String),
                Column('loteFaltante',String),
                Column('fecha',DateTime),
                Column('op', String),
                Column('referencia', String),
                Column('fotoPrenda1', String),#<----- thi's Binary
                Column('fotoPrenda2', String),#<----- thi's Binary
                Column('DetalleLote', String),
                Column('id_estado', Integer,ForeignKey('estado.id_estado')),)
    #integrante lista inser
    integrante =Table('integrante',meta,
                Column('id_integrante' ,Integer,primary_key=True),
                Column('fecha', DateTime),
                Column('nombreCompleto', String),
                Column('NumDocumento', Integer),
                Column('sexo', String),
                Column('fotoIntegrante', String),#<--- column field Binary
                Column('fotoFirma', String))#<--- column field Binary
    #operacion lista
    operacion = Table('operacion',meta,
                Column('id_operacion', Integer,primary_key=True),
                Column('fecha', DateTime),
                Column('nombreOperacion', String),
                Column('precioValor',String),
                Column('duracionOperacion', String),
                Column('aproxALDia', String),
                Column('fotoOperacion', String),
                Column('detalleOperacion', String))
    
    tarea   =   Table ('tarea',meta,
                Column('id_tarea', Integer,primary_key=True),
                Column('fecha', DateTime),
                Column('id_integrante', Integer,ForeignKey('integrante.id_integrante')),
                Column('id_operacion', Integer,ForeignKey('operacion.id_operacion')),
                Column('id_lote',Integer,ForeignKey('lote.id_lote')),
                Column('cantTomada', Integer),
                Column('talla', Integer),
                Column('cantNofinalizada', Integer))
    meta.create_all(engine)    
else:pass

def selectorRTList(self,tabla,pos):
    slct_tabla= tabla.select()
    result     = conn.execute(slct_tabla)
    row=result.fetchone()
    try:
        lista = [row[pos]]
        for row in result:lista.append(row[pos])
    except :
        lista = ["cargue datos!"]
    return lista

class dataBase():
    def AddOperacion(self,Nombre_Operacion,Precio_Operacion,Duracion_Operacion,Cantidad_Dia,Foto_Operacion,Detalle_Operacion):
        global engine,operacion,conn
        insert_operacion = operacion.insert().values(
            fecha             = DT.now(),
            nombreOperacion   = Nombre_Operacion,
            precioValor       = Precio_Operacion,
            duracionOperacion = Duracion_Operacion,
            aproxALDia        = Cantidad_Dia,
            fotoOperacion     = Foto_Operacion,
            detalleOperacion  = Detalle_Operacion)
        result = conn.execute(insert_operacion)        
        
       
        #select operacion
        slct_Operacion = operacion.select()
        result  = conn.execute(slct_Operacion)
        row     = result.fetchone()
        for row in result:print (row)
        
    def AddIntegrante(self,nombre_Completo,Num_Documento,foto_Integrante,foto_Firma):
        global conn, integrante
        insert_integrante     = integrante.insert().values(
            fecha             = DT.now(),
            nombreCompleto    = nombre_Completo,
            NumDocumento      = Num_Documento,
            fotoIntegrante    = foto_Integrante,
            fotoFirma         = foto_Firma)
        result = conn.execute(insert_integrante)   

        #select operacion
        slct_tIntegrante = integrante.select()
        result           = conn.execute(slct_tIntegrante)
        row              = result.fetchone()
        for row in result:print (row)

    def AddEstado(self,Nombre_Estado,Detalle_Estado):
        global conn, estado
        insert_estado      = estado.insert().values(
            fecha          = DT.now(),
            estado         = Nombre_Estado,
            detalle        = Detalle_Estado)

        result = conn.execute(insert_estado)   

    #select
    def slctEstado(self):return selectorRTList(self,estado,2)
    def slctIntegrante(self):return selectorRTList(self,integrante,2)
    def slctOperacion(self):return selectorRTList(self,operacion,2)
    def slctLote(self):return selectorRTList(self,lote,2)

    

    def AddTarea(self,integrante,operacion,lote,cant_Tomada,talla,cant_Nofinalizada):
        global conn,tarea            
        insert_tarea         = tarea.insert().values( 
            fecha            = DT.now(),
            id_integrante    = integrante,
            id_operacion     = operacion,
            id_lote          = lote,
            cantTomada       = cant_Tomada,
            talla            = talla,
            cantNofinalizada = cant_Nofinalizada)
        
        result = conn.execute(insert_tarea)
        #select tarea
        slct_Tarea=tarea.select()
        result=conn.execute(slct_Tarea)
        row=result.fetchone()
        for row in result:print (row)

        

    def AddLote(self,Lote_Total,Lote_Faltante,op,Num_Referencia,
                Foto_Prenda1,Foto_Prenda2,Detalle_Lote,Estado):
        global conn, lote
        insert_lote       = lote.insert().values(
            loteTotal     = Lote_Total,
            loteFaltante  = Lote_Faltante,
            fecha         = DT.now(),
            op            = op,
            referencia    = Num_Referencia,
            fotoPrenda1   = Foto_Prenda1,
            fotoPrenda2   = Foto_Prenda2,
            DetalleLote   = Detalle_Lote,
            id_estado     = Estado)
        
        result     = conn.execute(insert_lote)
        #select lote
        slct_Lote  = lote.select()
        result     = conn.execute(slct_Lote)
        row        = result.fetchone()
        for row in result:print (row)
   
    def Consulta(self):
        global conn
        pass 
    def Conf(self):
        global conn
        pass
    def close(self):
        global conn
        conn.close()