# -*- coding: utf-8 -*-

from rptpdfnormal import PDF
import xlrd
import os

class Readxlsold(object):
	"""docstring for Readxlsold"""
	def __init__(self):
		self.ingresos = ['0114','0121','0201','0312','0313','0406','0407','0904']
		self.descuentos = ['0705']
		self.aportes = ['0601','0605','0606','0607','0608']
		self.emp = ['0804']
		self.meses = {'01':'ENERO','02':'FEBRERO','03':'MARZO','04':'ABRIL','05':'MAYO','06':'JUNIO','07':'JULIO','08':'AGOSTO','09':'SETIEMBRE','10':'OCTUBRE','11':'NOVIEMBRE','12':'DICIEMBRE'}
	def read_xls(self,lista=[]):
		#QMessageBox.warning(self, "Mensaje",str(lista))
		#Declarando variables
		path_work = os.getcwd() # Directorio donde nos encontranos
		dst = '/file-v1/'
		path_work = path_work + dst

		if os.path.isdir(path_work):
			for x in lista: # Leemos los archivos que se encuentran dentro del directorio
				"""
				### Declaracion de Variables pre lectura de celdas
				"""
				ruc=''
				empleador=''
				periodo=''
				dni=''
				nombre=''
				situacion=''
				fecing=''
				tipot=''
				regimen=''
				cuspp=''
				dlaborados=''
				dnolaborados=''
				dsubsidiados=''
				condicion=''
				jothoras=''
				sothoras=''
				msltipo=''
				mslmotivo=''
				msldias=''
				otrosemp=''
				ingcodigo=''
				ingconcepto=''
				ingsoles=''
				ingdescuento=''
				ingneto=''
				descodigo=''
				desconcepto=''
				desdescuento=''
				## Descuente de afp
				aptcodigoafp=''
				aptconceptoafp=''
				aptdescuentoafp=''
				## Descuento de Quinta Categoria
				aptcodigoqc=''
				aptconceptoqc=''
				aptdescuentoqc=''
				## Descuento de Prima de Seguro
				aptcodigopsafp=''
				aptconceptopsafp=''
				aptdescuentopsafp=''
				## Aportacion Obligatoria SPP
				aptcodigoapspp=''
				aptconceptoapspp=''
				aptdescuentoapspp=''
				## Neto a pagar
				netoapagar=''
				## Aportes del Empleador
				aecodigoess=''
				aeconceptoess=''
				aenetoess=''
				dic_ingresos = {}
				dic_descuentos = {}
				dic_aportes = {}
				dic_empleador = {}
				"""
				### Fin de Declaracion de Variables
				"""
				book = xlrd.open_workbook(''+path_work+x+'',encoding_override='utf-8')
				sheet = book.sheet_by_index(0)
				# obteniendo RUC
				cell = sheet.cell(2,0) # obteniendo e ruc
				cell = str(cell.value)
				#print cell
				c = cell.split(':')
				ruc = str(c[1]).strip()
				#print ruc
				# Obteniendo Empleador
				cell = sheet.cell(3,0)
				cell = cell.value
				c = cell.split(':')
				empleador = str(c[1]).strip()
				# Obtener Periodo
				cell = sheet.cell(4,0)
				cell = cell.value
				#print cell
				c = cell.split(':')
				#print c
				periodo = str(c[1]).strip()
				#obtener dni
				cell = sheet.cell(11,2)
				dni = str(cell.value).strip()
				#obtener nombre
				ape1 = sheet.cell(8,1)
				ape2 = sheet.cell(8,2)
				nom =  sheet.cell(8,3)
				nombre = '%s %s %s'%(nom.value,ape1.value,ape2.value)
				#situacion
				#cell = sheet.cell(12,7)
				situacion = 'ACTIVO O SUBSIDIADO' # str(cell.value)
				#fecha de ingreso
				cell = sheet.cell(11,3)
				fecing = cell.value
				#tipo de trabajador
				cell = sheet.cell(8,5)
				tipot = cell.value
				#Regimen pensionario
				cell = sheet.cell(13,0)
				regimen = cell.value
				if regimen == "":
					regimen = 'SIS. NAC. PEN. ONP'

				#CUSPP
				cell = sheet.cell(13,1)
				cuspp = cell.value
				#dias laborados
				cell = sheet.cell(15,0)
				dlaborados = cell.value
				#dias no laborados
				cell = sheet.cell(15,1)
				dnolaborados = cell.value
				# Dias subsidiados
				cell = sheet.cell(15,2)
				dsubsidiados = cell.value
				#Condicion
				#cell = sheet.cell(17,4)
				condicion = 'Domiciliado' # str(cell.value)
				#Jornadas Ordinaria t horas
				cell = sheet.cell(15,3)
				jothoras = str(cell.value)
				# Jornadas Sobre Tiempos
				cell = sheet.cell(15,4)
				sothoras = str(cell.value)
				"""
				#Motivo de suspencion laboral
				cell = sheet.cell(20,1)
				msltipo = str(cell.value)
				#concepto MSL
				cell = sheet.cell(20,2)
				mslmotivo = str(cell.value)
				#dias de MSL
				cell = sheet.cell(20,6)
				msldias = str(cell.value)
				#otros empleadores
				cell = sheet.cell(20,7)
				otrosemp = str(cell.value)
				"""
				#print 'Numero de filas '+str(sheet.nrows) # Borrame

				for x in range(19,int(sheet.nrows)):
					cell = sheet.cell(int(x),0)
					# busqueda de ingresos
					for itemi in self.ingresos:
						if itemi == str(cell.value).strip():
							#print '----->Ingresos<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),4)
							#print pre.value
							dic_ingresos[itemi] = str(pre.value).strip()

					# busqueda de descuento
					for itemd in self.descuentos:
						if itemd == str(cell.value).strip():
							#print '----->Descuentos<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),5)
							#print pre.value
							dic_descuentos[itemd] = str(pre.value).strip()

					# busqueda de aportes
					for itema in self.aportes:
						if itema == str(cell.value).strip():
							#print '----->Aportes<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),5)
							#print pre.value
							dic_aportes[itema] = str(pre.value).strip()

					# busqueda de empleador
					for iteme in self.emp:
						if iteme == str(cell.value).strip():
							#print '----->Empleador<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),6)
							#print pre.value
							dic_empleador[iteme] = str(pre.value).strip()

					if str(cell.value).strip() == u'Neto a Pagar S/.':
						pre = sheet.cell(int(x),6)
						netoapagar = str(pre.value)


				#print 'RUC '+ruc
				#print 'Empleador '+empleador
				pdf = PDF('P','mm','A4')
				pdf.set_auto_page_break(True,margin=0)
				pdf.add_page(orientation='P')
				pdf.set_margins(0.5,0.5,0.5)
				pdf.cab_principal(ruc,empleador,periodo)
				pdf.cabecera(dni,nombre,situacion,fecing,tipot,regimen,cuspp,dlaborados,dnolaborados,dsubsidiados,condicion,jothoras,sothoras,msltipo,mslmotivo,msldias,otrosemp,netoapagar,dic_ingresos,dic_descuentos,dic_aportes,dic_empleador)
				pdf.cab_principal_copy(ruc,empleador,periodo)
				pdf.cabecera_copy(dni,nombre,situacion,fecing,tipot,regimen,cuspp,dlaborados,dnolaborados,dsubsidiados,condicion,jothoras,sothoras,msltipo,mslmotivo,msldias,otrosemp,netoapagar,dic_ingresos,dic_descuentos,dic_aportes,dic_empleador)
				path_out = os.getcwd()
				dbl = '/boletas/'
				periodo = periodo.split('/')
				per_m = str(periodo[0])
				per_mes = self.meses[per_m]
				per_anio = str(periodo[1])
				nnom = nombre.split(' ')
				print nnom
				print len(nnom)
				if len(nnom) == 4:
					nombre = nnom[0]+'_'+nnom[2]+'_'+nnom[3]
				elif len(nnom) == 3:
					nombre = nnom[0]+'_'+nnom[1]+'_'+nnom[2]

				if os.path.exists(path_out+dbl+per_anio):
					if os.path.exists(path_out+dbl+per_anio+'/'+per_mes):
						pdf.output(path_out+dbl+per_anio+'/'+per_mes+'/'+dni+'_'+nombre+'.pdf', 'F')
					else:
						os.mkdir(path_out+dbl+per_anio+'/'+per_mes)
						pdf.output(path_out+dbl+per_anio+'/'+per_mes+'/'+dni+'_'+nombre+'.pdf', 'F')
				else:
					os.mkdir(path_out+dbl+per_anio)
					if os.path.exists(path_out+dbl+per_anio+'/'+per_mes):
						pdf.output(path_out+dbl+per_anio+'/'+per_mes+'/'+dni+'_'+nombre+'.pdf', 'F')
					else:
						os.mkdir(path_out+dbl+per_anio+'/'+per_mes)
						pdf.output(path_out+dbl+per_anio+'/'+per_mes+'/'+dni+'_'+nombre+'.pdf', 'F')
		else:
			print 'No es un directorio'
		#print lista

	def eliminarAcentos(self,cadena):

	    d = {u'\xc1':'A',u'\xc9':'E',u'\xcd':u'I',u'\xd3':u'O',u'\xda':u'U',u'\xdc':u'U',u'\xd1':u'N',u'\xc7':u'C',u'\xed':u'i',u'\xf3':u'o',u'\xf1':u'n',u'\xe7':u'c',u'\xba':u'',
	        u'\xb0':u'',u'\x3a':u'',u'\xe1':u'a',u'\xe2':u'a',u'\xe3':u'a',u'\xe4':u'a',u'\xe5':u'a',u'\xe8':u'e',u'\xe9':u'e',u'\xea':u'e',u'\xeb':u'e',u'\xec':u'i',u'\xed':u'i',
	        u'\xee':u'i',u'\xef':u'i',u'\xf2':u'o',u'\xf3':u'o',u'\xf4':u'o',u'\xf5':u'o',u'\xf0':u'o',u'\xf9':u'u',u'\xfa':u'u',u'\xfb':u'u',u'\xfc':u'u',u'\xe5':u'a'}

	    nueva_cadena = cadena
	    for c in d.keys():
	        nueva_cadena = nueva_cadena.replace(c,d[c])

	    auxiliar = nueva_cadena.encode('utf-8')
	    return nueva_cadena