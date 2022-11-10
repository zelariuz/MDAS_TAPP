#!/usr/bin/python
# -*- coding: utf-8 -*-

#twisted
from twisted.enterprise import adbapi
#jsonrpc
from txjsonrpc.web import jsonrpc
#asyncDB twistar
# from twistar.registry import Registry
#Diferidos
from twisted.internet.defer import inlineCallbacks

#modules
# from library.models import EndpointModels

#Utilidades
# from library.rutils import 

class ServerFactory(jsonrpc.JSONRPC):
	"""
		Back API Taller de Aplicaciones 2
	"""
	documentPath = ""

	def __init__(self, *args, **kwargs):
		"""
			Initial configuration for SherpaBackend jsonRPC server
			
		"""
		# inicializar caracteristicas del objeto JSONRPC
		super(jsonrpc.JSONRPC, self).__init__(*args, **kwargs)

	### Espacio de endpoints
	@inlineCallbacks
	def jsonrpc_alive(self):
		"""
			Para indicar si el reactor esta vivo.
		"""
		jsonResponse = {'response' : 1}
		yield 1+1 # condicion minima para que sea un diferido
		return jsonResponse