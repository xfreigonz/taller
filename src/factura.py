# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from conexion import bd

def Grabarfac(dnifac, matrifac, marcafac, modelfac, fechafac):
    cursor = bd.cursor()
    registrofac = (dnifac, matrifac, marcafac, modelfac, fechafac)
    if dnifac != "" and  matrifac != "":
        cursor.executemany("""INSERT INTO facturas(dnifac,matrifac, modelfac,marcafac,fechafac) VALUES (?,?,?,?,?);""", (registrofac,))
        bd.commit()
    else:
       return False

def limpiarfac(idfac, dnifac, matrifac, marcafac, modelfac, fechafac):
    idfac.set_text("")
    dnifac.set_text("")
    matrifac.set_text("")
    marcafac.set_text("")
    modelfac.set_text("")
    fechafac.set_text("")
   
def mostrar(listafac, trewFactura):
    listafac.clear()
    cursor = bd.cursor()
    sql = """ SELECT idfac, dnifac, matrifac, marcafac, modelfac, fechafac FROM facturas ORDER BY dnifac"""
    cursor.execute(sql)
    datos = cursor.fetchall()
    datos = filter(None, datos)
    for fila in datos:
        if fila != None:
            listafac.append(fila)
        else:
            print"error"
        trewFactura.show()
