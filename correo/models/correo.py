# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import time

class estudiante(osv.osv):
	_name='cfg.correo'
	
	_columns= {
		'remitente':fields.char(
					'Remitente',
					size=80,
					required=True,
					help='Aqui se coloca el nombre de la persona que envia el mensaje',
		),
		'receptor':fields.char(
					'Receptor',
					size=80,
					required=True,
					help='Aqui se coloca el nombre de la persona que recibe el mensaje',
		),
		'fecha_de_envio':fields.date(
					'Fecha de envio',
					required=True,
					help='Aqui se coloca la fecha de envio del correo',
		),
		'contenido':fields.html(
					'Contenido',
		),
		'archivos_adjuntos':fields.text(
					'Adjuntar',
		),
		'active':fields.boolean(
					'Activo',
					help='Si esta activo el motor lo incluira'
		),
	
	}
	
	_defaults={
		'active':True,
		'remitente':'Pablo Perez',
		'receptor':'Pedro Picapiedra',
		'contenido':'<h1>Hola</h1>',
		'fecha_de_envio':lambda *a: time.strftime('%Y-%m-%d'),
		'archivos_adjuntos':'Inserte un archivo (Cuando sepa como hacerlo)',
	
	}
