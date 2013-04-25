# -*- coding: utf-8 -*-
import os
from fpdf import FPDF

class PDF(FPDF):

	def cab_principal(self,ruc='',empleador='',periodo=''):
		self.set_font('Arial','B',10)
		self.set_xy(10,10)
		self.cell(ln=0,h=0,align='C',w=180,txt='Boleta de Pago',border=0)
		self.set_font('Arial','B',8)
		self.set_xy(10,14)
		self.cell(ln=0,h=0,align='L',w=40,txt='RUC :'+ruc,border=0)
		self.set_xy(10,18)
		self.cell(ln=0,h=0,align='L',w=30,txt='Empleador: '+empleador,border=0)
		self.set_xy(10,22)
		self.cell(ln=0,h=0,align='L',w=30,txt='Periodo:'+periodo,border=0)
		self.image('resource/icrlogo.png', 180, 7.0, link='', type='', w=20.0, h=16.0)

	def cabecera(self,dni='',nombre='',situacion='',fecing='',tipot='',regimen='',cuspp='',dlaborados='',dnolaborados='',dsubsidiados='',condicion='',jothoras='',sothoras='',msltipo='',mslmotivo='',msldias='',otrosemp='',netoapagar='',dingreso={},ddescuento={},daportes={},dempleador={}):
		# Documentos de Identidad
		#self.rect(10.0, 35.0, 30.0, 10.0)
		self.set_font('Arial','',8)
		self.set_xy(10,24)
		self.cell(ln=0,h=4,align='C',w=55,txt='Documento de Identidad',border=1)
		self.set_xy(10,28)
		self.cell(ln=0,h=4,align='C',w=27.5,txt='Tipo',border=1)
		self.set_xy(37.5,28)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=u'Número' ,border=1)
		self.set_xy(65,24)
		self.cell(ln=0,h=8,align='C',w=85,txt='Nombre y Apellidos',border=1)
		self.set_xy(150,24)
		self.cell(ln=0,h=8,align='C',w=50,txt=u'Situación',border=1)
		#segunda fila
		self.set_xy(10,32)
		self.cell(ln=0,h=4,align='C',w=27.5,txt='DNI',border=1)
		self.set_xy(37.5,32)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=dni,border=1)
		self.set_xy(65,32)
		self.cell(ln=0,h=4,align='C',w=85,txt=u''+nombre,border=1)
		self.set_xy(150,32)
		self.cell(ln=0,h=4,align='C',w=50,txt=situacion,border=1)
		#tercera fila
		self.set_xy(10,36)
		self.cell(ln=0,h=4,align='C',w=55,txt='Fecha de Ingreso',border=1)
		self.set_xy(65,36)
		self.cell(ln=0,h=4,align='C',w=42.5,txt='Tipo de Trabajador',border=1)
		self.set_xy(107.5,36)
		self.cell(ln=0,h=4,align='C',w=42.5,txt='Regimen Pensionario',border=1)
		self.set_xy(150,36)
		self.cell(ln=0,h=4,align='C',w=50,txt='CUSPP',border=1)
		#Cuarta fila
		self.set_xy(10,40)
		self.cell(ln=0,h=4,align='C',w=55,txt=fecing,border=1)
		self.set_xy(65,40)
		self.cell(ln=0,h=4,align='C',w=42.5,txt=tipot,border=1)
		self.set_xy(107.5,40)
		self.cell(ln=0,h=4,align='C',w=42.5,txt=regimen,border=1)
		self.set_xy(150,40)
		self.cell(ln=0,h=4,align='C',w=50,txt=cuspp,border=1)
		#Quinta fila
		self.set_xy(10,44)
		self.multi_cell(w=27.5,h=8,txt=u'Días Laborados',border=1,align='C')
		self.set_xy(37.5,44)
		self.set_font('Arial','',7)
		self.multi_cell(w=27.5,h=8,txt=u'Días no Laborados',border=1,align='C')
		self.set_xy(65,44)
		self.multi_cell(w=21.5,h=8,txt=u'Días Subsidiados',border=1,align='C')
		self.set_xy(86.5,44)
		self.set_font('Arial','',8)
		self.multi_cell(h=8,align='C',w=21,txt='Condicion',border=1)
		self.set_xy(107.5,44)
		self.multi_cell(w=42.5,h=4,txt='Jornada Ordinaria',border=1,align='C')
		self.set_xy(107.5,48)
		self.multi_cell(w=21.5,h=4,txt='Total Horas',border=1,align='C')
		self.set_xy(129,48)
		self.multi_cell(w=21,h=4,txt='Minutos',border=1,align='C')
		self.set_xy(150,44)
		self.multi_cell(w=50,h=4,txt='Sobretiempo',border=1,align='C')
		self.set_xy(150,48)
		self.multi_cell(w=25,h=4,txt='Total Horas',border=1,align='C')
		self.set_xy(175,48)
		self.multi_cell(w=25,h=4,txt='Minutos',border=1,align='C')
		#Sexta Fila
		self.set_xy(10,52)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=dlaborados,border=1)
		self.set_xy(37.5,52)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=dnolaborados,border=1)
		self.set_xy(65,52)
		self.cell(ln=0,h=4,align='C',w=21.5,txt=dsubsidiados,border=1)
		self.set_xy(86.5,52)
		self.cell(ln=0,h=4,align='C',w=21,txt=condicion,border=1)
		self.set_xy(107.5,52)
		self.cell(ln=0,h=4,align='C',w=21.5,txt=jothoras,border=1)
		self.set_xy(129,52)
		self.cell(ln=0,h=4,align='C',w=21,txt='',border=1)
		self.set_xy(150,52)
		self.cell(ln=0,h=4,align='C',w=25,txt=sothoras,border=1)
		self.set_xy(175,52)
		self.cell(ln=0,h=4,align='C',w=25,txt='',border=1)
		#Septima fila
		self.set_xy(10,56)
		self.cell(ln=0,h=4,align='C',w=140,txt=u'Motivo de Suspensión Laborales',border=1)
		self.set_xy(150,56)
		self.set_font('Arial','',6)
		self.multi_cell(w=50,h=8,txt='Otros Empleadores por Renta de 5ta Categoria',border=1,align='C')
		self.set_font('Arial','',8)
		self.set_xy(10,60)
		self.cell(ln=0,h=4,align='C',w=27.5,txt='Tipo',border=1)
		self.set_xy(37.5,60)
		self.cell(ln=0,h=4,align='C',w=91.5,txt='Motivo',border=1)
		self.set_xy(129,60)
		self.cell(ln=0,h=4,align='C',w=21,txt=u'Nro Días',border=1)
		#octava fila
		self.set_xy(10,64)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=msltipo,border=1)
		self.set_xy(37.5,64)
		self.cell(ln=0,h=4,align='C',w=91.5,txt=mslmotivo,border=1)
		self.set_xy(129,64)
		self.cell(ln=0,h=4,align='C',w=21,txt=msldias,border=1)
		self.set_xy(150,64)
		self.cell(ln=0,h=4,align='C',w=50,txt=otrosemp,border=1)
		#novena fila
		self.set_xy(10,70)
		self.cell(ln=0,h=4,align='C',w=27.5,txt='Codigo',border=1)
		self.set_xy(37.5,70)
		self.cell(ln=0,h=4,align='C',w=91.5,txt='Conceptos',border=1)
		self.set_xy(129,70)
		self.cell(ln=0,h=4,align='C',w=21,txt=u'Ingresos S/.',border=1)
		self.set_xy(150,70)
		self.cell(ln=0,h=4,align='C',w=25,txt=u'Descuentos S/.',border=1)
		self.set_xy(175,70)
		self.cell(ln=0,h=4,align='C',w=25,txt=u'Neto S/.',border=1)
		#decimo
		self.set_xy(10,74)
		self.set_font('Arial','B',8)
		self.cell(ln=0,h=4,align='L',w=190,txt='Ingresos',border=1)
		#onceavo
		# aqui
		des_ingreso = {'0121':u'REMUNERACIÓN O JORNAL BASICO','0201':u'ASIGNACION FAMILIAR','0312':u'BONIF. EXTRAORD. TEMPORAL LEY 29351','0406':u'GRATIF. F.PATRIAS NAVIDAD LEY 29351','0904':u'CONPENSACION TIEMPO DE SERVICIO'}
		y=78
		for k,i in dingreso.items():
			#print k, i
			self.set_font('Arial','',8)
			self.set_xy(10,y)
			self.cell(ln=0,h=4,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=4,align='L',w=91.5,txt=des_ingreso[k],border=0)
			self.set_xy(129,y)
			self.cell(ln=0,h=4,align='R',w=21,txt=i,border=0)
			y = y + 4

		self.set_xy(10,y)
		self.set_font('Arial','B',8)
		self.cell(ln=0,h=4,align='L',w=190,txt='Descuentos',border=1)

		des_descuento = {'0705':u'INASISTENCIAS'}
		for k,i in ddescuento.items():
			y = y +4
			self.set_font('Arial','',8)
			self.set_xy(10,y)
			self.cell(ln=0,h=4,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=4,align='L',w=91.5,txt=des_descuento[k],border=0)
			self.set_xy(150,y)
			self.cell(ln=0,h=4,align='R',w=21,txt=i,border=0)

		y = y + 4
		self.set_xy(10,y)
		self.set_font('Arial','B',8)
		self.cell(ln=0,h=4,align='L',w=190,txt='Aportes del Trabajador',border=1)

		des_aporte = {'0601':u'COMISIÓN AFP PROCENTUAL','0605':u'RENTA DE QUINTA CATEGORIA RETENCIONES','0606':u'PRIMA DE SEGUROS AFP','0607':u'SISTEMA NAC. PENCIONES DL 19990','0608':u'SPP - APORTACIÓN OBLIGATORIA'}
		for k,i in daportes.items():
			y = y +4
			self.set_font('Arial','',8)
			self.set_xy(10,y)
			self.cell(ln=0,h=4,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=4,align='L',w=91.5,txt=des_aporte[k],border=0)
			self.set_xy(150,y)
			self.cell(ln=0,h=4,align='R',w=21,txt=i,border=0)


		y = y + 4
		self.set_xy(10,y)
		self.set_font('Arial','B',8)
		self.cell(ln=0,h=4,align='L',w=169,txt='Neto a Pagar',border='LTB')
		self.set_xy(179,y)
		self.cell(ln=0,h=4,align='R',w=21,txt=netoapagar,border='RTB')
		y = y + 5
		self.set_xy(10,y)
		self.set_font('Arial','B',8)
		self.cell(ln=0,h=4,align='L',w=190,txt='Aportes del Empleador',border=1)

		des_empleador = {'0804':'ESSALUD REGULAR CBSSP AGRAR/AC TRAB'}
		for k,i in dempleador.items():
			y = y + 4
			self.set_font('Arial','',8)
			self.set_xy(10,y)
			self.cell(ln=0,h=4,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=4,align='L',w=91.5,txt=des_empleador[k],border=0)
			self.set_xy(179,y)
			self.cell(ln=0,h=4,align='R',w=21,txt=i,border=0)

		y = y + 16
		self.set_xy(24,y)
		self.cell(ln=0,h=4,align='L',w=30,txt='Firma del Empleador',border=0)
		self.set_xy(140,y)
		self.cell(ln=0,h=4,align='L',w=30,txt='Firma del Trabajador',border=0)

	def cab_principal_copy(self,ruc='',empleador='',periodo=''):
		y = 167
		self.set_font('Arial','B',10)
		self.set_xy(10,y)
		self.cell(ln=0,h=0,align='C',w=180,txt='Boleta de Pago',border=0)
		self.set_font('Arial','B',8)
		y+=4
		self.set_xy(10,y)
		self.cell(ln=0,h=0,align='L',w=40,txt='RUC :'+ruc,border=0)
		y+=4
		self.set_xy(10,y)
		self.cell(ln=0,h=0,align='L',w=30,txt='Empleador: '+empleador,border=0)
		y+=4
		self.set_xy(10,y)
		self.cell(ln=0,h=0,align='L',w=30,txt='Periodo:'+periodo,border=0)
		self.image('resource/icrlogo.png', 180, 167, link='', type='', w=20.0, h=16.0)

	def cabecera_copy(self,dni='',nombre='',situacion='',fecing='',tipot='',regimen='',cuspp='',dlaborados='',dnolaborados='',dsubsidiados='',condicion='',jothoras='',sothoras='',msltipo='',mslmotivo='',msldias='',otrosemp='',netoapagar='',dingreso={},ddescuento={},daportes={},dempleador={}):
		# Documentos de Identidad
		#self.rect(10.0, 35.0, 30.0, 10.0)
		self.set_font('Arial','',8)
		self.set_xy(10,184)
		self.cell(ln=0,h=4,align='C',w=55,txt='Documento de Identidad',border=1)
		self.set_xy(10,188)
		self.cell(ln=0,h=4,align='C',w=27.5,txt='Tipo',border=1)
		self.set_xy(37.5,188)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=u'Número' ,border=1)
		self.set_xy(65,184)
		self.cell(ln=0,h=8,align='C',w=85,txt='Nombre y Apellidos',border=1)
		self.set_xy(150,184)
		self.cell(ln=0,h=8,align='C',w=50,txt=u'Situación',border=1)
		#segunda fila
		self.set_xy(10,192)
		self.cell(ln=0,h=4,align='C',w=27.5,txt='DNI',border=1)
		self.set_xy(37.5,192)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=dni,border=1)
		self.set_xy(65,192)
		self.cell(ln=0,h=4,align='C',w=85,txt=u''+nombre,border=1)
		self.set_xy(150,192)
		self.cell(ln=0,h=4,align='C',w=50,txt=situacion,border=1)
		#tercera fila
		self.set_xy(10,196)
		self.cell(ln=0,h=4,align='C',w=55,txt='Fecha de Ingreso',border=1)
		self.set_xy(65,196)
		self.cell(ln=0,h=4,align='C',w=42.5,txt='Tipo de Trabajador',border=1)
		self.set_xy(107.5,196)
		self.cell(ln=0,h=4,align='C',w=42.5,txt='Regimen Pensionario',border=1)
		self.set_xy(150,196)
		self.cell(ln=0,h=4,align='C',w=50,txt='CUSPP',border=1)
		#Cuarta fila
		self.set_xy(10,200)
		self.cell(ln=0,h=4,align='C',w=55,txt=fecing,border=1)
		self.set_xy(65,200)
		self.cell(ln=0,h=4,align='C',w=42.5,txt=tipot,border=1)
		self.set_xy(107.5,200)
		self.cell(ln=0,h=4,align='C',w=42.5,txt=regimen,border=1)
		self.set_xy(150,200)
		self.cell(ln=0,h=4,align='C',w=50,txt=cuspp,border=1)
		#Quinta fila
		self.set_xy(10,204)
		self.multi_cell(w=27.5,h=8,txt=u'Días Laborados',border=1,align='C')
		self.set_xy(37.5,204)
		self.set_font('Arial','',7)
		self.multi_cell(w=27.5,h=8,txt=u'Días no Laborados',border=1,align='C')
		self.set_xy(65,204)
		self.multi_cell(w=21.5,h=8,txt=u'Días Subsidiados',border=1,align='C')
		self.set_xy(86.5,204)
		self.set_font('Arial','',8)
		self.multi_cell(h=8,align='C',w=21,txt='Condicion',border=1)
		self.set_xy(107.5,204)
		self.multi_cell(w=42.5,h=4,txt='Jornada Ordinaria',border=1,align='C')
		self.set_xy(107.5,208)
		self.multi_cell(w=21.5,h=4,txt='Total Horas',border=1,align='C')
		self.set_xy(129,208)
		self.multi_cell(w=21,h=4,txt='Minutos',border=1,align='C')
		self.set_xy(150,204)
		self.multi_cell(w=50,h=4,txt='Sobretiempo',border=1,align='C')
		self.set_xy(150,208)
		self.multi_cell(w=25,h=4,txt='Total Horas',border=1,align='C')
		self.set_xy(175,208)
		self.multi_cell(w=25,h=4,txt='Minutos',border=1,align='C')
		#Sexta Fila
		self.set_xy(10,212)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=dlaborados,border=1)
		self.set_xy(37.5,212)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=dnolaborados,border=1)
		self.set_xy(65,212)
		self.cell(ln=0,h=4,align='C',w=21.5,txt=dsubsidiados,border=1)
		self.set_xy(86.5,212)
		self.cell(ln=0,h=4,align='C',w=21,txt=condicion,border=1)
		self.set_xy(107.5,212)
		self.cell(ln=0,h=4,align='C',w=21.5,txt=jothoras,border=1)
		self.set_xy(129,212)
		self.cell(ln=0,h=4,align='C',w=21,txt='',border=1)
		self.set_xy(150,212)
		self.cell(ln=0,h=4,align='C',w=25,txt=sothoras,border=1)
		self.set_xy(175,212)
		self.cell(ln=0,h=4,align='C',w=25,txt='',border=1)
		#Septima fila
		self.set_xy(10,216)
		self.cell(ln=0,h=4,align='C',w=140,txt=u'Motivo de Suspensión Laborales',border=1)
		self.set_xy(150,216)
		self.set_font('Arial','',6)
		self.multi_cell(w=50,h=8,txt='Otros Empleadores por Renta de 5ta Categoria',border=1,align='C')
		self.set_font('Arial','',8)
		self.set_xy(10,220)
		self.cell(ln=0,h=4,align='C',w=27.5,txt='Tipo',border=1)
		self.set_xy(37.5,220)
		self.cell(ln=0,h=4,align='C',w=91.5,txt='Motivo',border=1)
		self.set_xy(129,220)
		self.cell(ln=0,h=4,align='C',w=21,txt=u'Nro Días',border=1)
		#octava fila
		self.set_xy(10,224)
		self.cell(ln=0,h=4,align='C',w=27.5,txt=msltipo,border=1)
		self.set_xy(37.5,224)
		self.cell(ln=0,h=4,align='C',w=91.5,txt=mslmotivo,border=1)
		self.set_xy(129,224)
		self.cell(ln=0,h=4,align='C',w=21,txt=msldias,border=1)
		self.set_xy(150,224)
		self.cell(ln=0,h=4,align='C',w=50,txt=otrosemp,border=1)
		#novena fila
		self.set_font('Arial','',7)
		self.set_xy(10,228)
		self.cell(ln=0,h=3,align='C',w=27.5,txt='Codigo',border=1)
		self.set_xy(37.5,228)
		self.cell(ln=0,h=3,align='C',w=91.5,txt='Conceptos',border=1)
		self.set_xy(129,228)
		self.cell(ln=0,h=3,align='C',w=21,txt=u'Ingresos S/.',border=1)
		self.set_xy(150,228)
		self.cell(ln=0,h=3,align='C',w=25,txt=u'Descuentos S/.',border=1)
		self.set_xy(175,228)
		self.cell(ln=0,h=3,align='C',w=25,txt=u'Neto S/.',border=1)
		#decimo
		self.set_xy(10,231)
		self.set_font('Arial','B',7)
		self.cell(ln=0,h=3,align='L',w=190,txt='Ingresos',border=1)
		#onceavo
		# aqui
		des_ingreso = {'0121':u'REMUNERACIÓN O JORNAL BASICO','0201':u'ASIGNACION FAMILIAR','0312':u'BONIF. EXTRAORD. TEMPORAL LEY 29351','0406':u'GRATIF. F.PATRIAS NAVIDAD LEY 29351','0904':u'CONPENSACION TIEMPO DE SERVICIO'}
		y=234
		for k,i in dingreso.items():
			#print k, i
			self.set_font('Arial','',7)
			self.set_xy(10,y)
			self.cell(ln=0,h=3,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=3,align='L',w=91.5,txt=des_ingreso[k],border=0)
			self.set_xy(129,y)
			self.cell(ln=0,h=3,align='R',w=21,txt=i,border=0)
			y = y + 3

		self.set_xy(10,y)
		self.set_font('Arial','B',7)
		self.cell(ln=0,h=3,align='L',w=190,txt='Descuentos',border=1)

		des_descuento = {'0705':u'INASISTENCIAS'}
		for k,i in ddescuento.items():
			y = y + 3
			self.set_font('Arial','',7)
			self.set_xy(10,y)
			self.cell(ln=0,h=3,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=3,align='L',w=91.5,txt=des_descuento[k],border=0)
			self.set_xy(150,y)
			self.cell(ln=0,h=3,align='R',w=21,txt=i,border=0)

		y = y + 3
		self.set_xy(10,y)
		self.set_font('Arial','B',7)
		self.cell(ln=0,h=3,align='L',w=190,txt='Aportes del Trabajador',border=1)

		des_aporte = {'0601':u'COMISIÓN AFP PROCENTUAL','0605':u'RENTA DE QUINTA CATEGORIA RETENCIONES','0606':u'PRIMA DE SEGUROS AFP','0607':u'SISTEMA NAC. PENCIONES DL 19990','0608':u'SPP - APORTACIÓN OBLIGATORIA'}
		for k,i in daportes.items():
			y = y + 3
			self.set_font('Arial','',7)
			self.set_xy(10,y)
			self.cell(ln=0,h=3,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=3,align='L',w=91.5,txt=des_aporte[k],border=0)
			self.set_xy(150,y)
			self.cell(ln=0,h=3,align='R',w=21,txt=i,border=0)


		y = y + 3
		self.set_xy(10,y)
		self.set_font('Arial','B',7)
		self.cell(ln=0,h=3,align='L',w=169,txt='Neto a Pagar',border='LTB')
		self.set_xy(179,y)
		self.cell(ln=0,h=3,align='R',w=21,txt=netoapagar,border='RTB')
		y = y + 3.5
		self.set_xy(10,y)
		self.set_font('Arial','B',7)
		self.cell(ln=0,h=3,align='L',w=190,txt='Aportes del Empleador',border=1)

		des_empleador = {'0804':'ESSALUD REGULAR CBSSP AGRAR/AC TRAB'}
		for k,i in dempleador.items():
			y = y + 3
			self.set_font('Arial','',7)
			self.set_xy(10,y)
			self.cell(ln=0,h=3,align='C',w=27.5,txt=k,border=0)
			self.set_xy(37.5,y)
			self.cell(ln=0,h=3,align='L',w=91.5,txt=des_empleador[k],border=0)
			self.set_xy(179,y)
			self.cell(ln=0,h=3,align='R',w=21,txt=i,border=0)

		#y = y + 12
		self.set_xy(24,286)
		self.cell(ln=0,h=3,align='L',w=30,txt='Firma del Empleador',border=0)
		self.set_xy(140,286)
		self.cell(ln=0,h=3,align='L',w=30,txt='Firma del Trabajador',border=0)

"""
pdf = PDF('P','mm','A4')
pdf.set_auto_page_break(True,margin=0)
pdf.set_margins(0.5,0.5,0.5)
pdf.add_page('P')
pdf.cab_principal()
pdf.cabecera()
pdf.cab_principal_copy()
pdf.cabecera_copy()
pdf.output('F:/fpdf-python.pdf', 'F')
"""