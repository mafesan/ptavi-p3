#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":
    """
    Programa principal
    """
    lista = sys.argv
    if len(lista) != 2:
        print "Usage: python karaoke.py file.smil"
    else:
        fich = lista[1]
        parser = make_parser()
        KHandler = SmallSMILHandler()
        parser.setContentHandler(KHandler)
        parser.parse(open(fich))
        print "hola"