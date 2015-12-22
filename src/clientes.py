#! /usr/bin/python
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from conexion import bd


def Grabarcli(dni, apel, nom, dire, loc, prov, cp, mov, tel, mail, si):
    dni = dni.get_text()
    apel = apel.get_text()
    print(apel)
    nom = nom.get_text()
    dire = dire.get_text()
    loc = loc.get_text()
    prov = prov.get_text()
    cp = cp.get_text()
    mov = mov.get_text()
    tel = tel.get_text()
    mail = mail.get_text()



def validoDNI(dni):
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    dig_ext = "XYZ"
    reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in dig_ext:
            dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23] == dig_control
    return False