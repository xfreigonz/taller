#! /usr/bin/python
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from gi.repository import Gtk

from conexion import bd

import clientes

class main:

    def __init__(self):

#declaracion de widgets
        b = Gtk.Builder()
        b.add_from_file("taller.glade")
        self.ventanaPrincipal = b.get_object("ventanaPrincipal")
        self.ventanaNeocli = b.get_object("ventanaNeocli")
        self.btnSalircli = b.get_object("btnSalircli")
        self.btnNeocli = b.get_object("btnNeocli")
        self.btnGrabcli = b.get_object("btnGrabcli")
        self.btnSalir = b.get_object("btnSalir")
        self.listCliente = b.get_object("listCliente")
        self.ednicli = b.get_object("entDni")
        self.apelcli = b.get_object("entApel")
        self.nomcli = b.get_object("entNom")
        self.dircli = b.get_object("entDir")
        self.loccli = b.get_object("entLoc")
        self.provcli = b.get_object("entProv")
        self.cpcli = b.get_object("entCp")
        self.movcli = b.get_object("entMov")
        self.telcli = b.get_object("entTel")
        self.mailcli = b.get_object("entMail")
        self.sicli = b.get_object("rtbSi")
        self.nocli = b.get_object("rtbNo")
        self.avisodni = b.get_object("dlgAvis")
        self.btnAceptar = b.get_object("btnAceptar")
        self.ventanaPrincipal.show()

        dic = {"on_btnNeocli_clicked": self.on_btnNeocli_clicked,
            "on_btnSalir_clicked": self.on_btnSalir_clicked,
            "on_btnSalircli_clicked": self.on_btnSalircli_clicked,
            "on_btnGrabcli_clicked": self.on_btnGrabcli_clicked,
            "on_ventanaPrincipal_destroy": self.on_ventanaPrincipal_destroy,
            "on_ventanaNeocli_delete_event": self.on_ventanaNeocli_delete_event,
            "on_entDni_focus_out_event": self.on_entDni_focus_out_event,
            "on_btnAceptar_clicked": self.on_btnAceptar_clicked
            }

        b.connect_signals(dic)

#declaracion de funciones

    def on_btnNeocli_clicked(self, widget, data=None):
        self.ventanaNeocli.show()

    def on_btnSalir_clicked(self, widget):
        Gtk.main_quit()

    def on_ventanaPrincipal_destroy(self, widget):
        Gtk.main_quit()

    def on_ventanaNeocli_delete_event(self, widget, data=None):
        self.ventanaNeocli.hide()
        return True

    def on_btnAceptar_clicked(self, widget):
        self.ventanaNeocli.hide()

    def on_entDni_focus_out_event(self, widget, Data=None):
        self.dnicli = self.ednicli.get_text()
        self.dnicli = self.dnicli.upper()
        self.ednicli.set_text(self.dnicli)
        if (clientes.validoDNI(self.dnicli) is False and self.dnicli != ""):
            self.avisodni.show()
            self.ednicli.set_text("")

    def on_btnSalircli_clicked(self, widget, Data=None):
        self.ventanaNeocli.hide()

    def on_btnGrabcli_clicked(self, widget):
        clientes.Grabarcli(self.ednicli, self.apelcli, self.nomcli, self.dircli, self.loccli, self.provcli, self.cpcli, self.movcli, self.telcli, self.mailcli, 1)

if __name__ == "__main__":
    main = main()
    Gtk.main()