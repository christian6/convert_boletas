# -*- coding: utf-8 -*-

from rptpdfnormal import PDF
import xlrd
import os

class Readxls():
	def __init__(self):
		self.ingresos = ['0114','0118','0121','0201','0312','0313','0406','0407','0904','0916']
		self.descuentos = ['0707','0705','0704']
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
				###
				msltipo2=''
				mslmotivo2=''
				msldias2=''
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
				cell = sheet.cell(5,1)
				cell = str(cell.value)
				c = cell.split(':')
				ruc = str(c[1]).strip()
				# Obteniendo Empleador
				cell = sheet.cell(6,1)
				cell = str(cell.value)
				c = cell.split(':')
				empleador = str(c[1]).strip()
				# Obtener Periodo
				cell = sheet.cell(7,1)
				cell = str(cell.value)
				c = cell.split(':')
				periodo = str(c[1]).strip()
				#obtener dni
				cell = sheet.cell(12,2)
				dni = str(cell.value).strip()
				#obtener nombre
				cell = sheet.cell(12,3)
				nombre = cell.value
				#situacion
				cell = sheet.cell(12,7)
				situacion = cell.value
				#fecha de ingreso
				cell = sheet.cell(14,1)
				fecing = cell.value.strip()
				#tipo de trabajador
				cell = sheet.cell(14,3)
				tipot = cell.value
				#Regimen pensionario
				cell = sheet.cell(14,5)
				regimen = cell.value
				#CUSPP
				cell = sheet.cell(14,7)
				cuspp = cell.value
				#dias laborados
				cell = sheet.cell(17,1)
				dlaborados = str(cell.value)
				#dias no laborados
				cell = sheet.cell(17,2)
				dnolaborados = str(cell.value)
				# Dias subsidiados
				cell = sheet.cell(17,3)
				dsubsidiados = str(cell.value)


				#Condicion
				cell = sheet.cell(17,4)
				condicion = cell.value
				#Jornadas Ordinaria t horas
				cell = sheet.cell(17,5)
				jothoras = str(cell.value)
				# Jornadas Sobre Tiempos
				cell = sheet.cell(17,7)
				sothoras = str(cell.value)
				#Motivo de suspencion laboral
				cell = sheet.cell(20,1)
				msltipo = cell.value
######################
				##Motivo de suspencion laboral 2
				cell = sheet.cell(21,1)
				msltipo2 = cell.value
				cell = sheet.cell(21,2)
				mslmotivo2 = cell.value
				#dias de MSL
				cell = sheet.cell(21,6)
				msldias2 = str(cell.value)
########################
				#concepto MSL
				cell = sheet.cell(20,2)
				mslmotivo = cell.value
				#dias de MSL
				cell = sheet.cell(20,6)
				msldias = str(cell.value)
				#otros empleadores
				cell = sheet.cell(20,7)
				otrosemp = cell.value

				#print 'Numero de filas '+str(sheet.nrows) # Borrame

				for x in range(24,int(sheet.nrows)):
					cell = sheet.cell(int(x),1)
					# busqueda de ingresos
					for itemi in self.ingresos:
						if itemi == str(cell.value).strip():
							#print '----->Ingresos<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),6)
							#print pre.value
							dic_ingresos[itemi] = str(pre.value).strip()

					# busqueda de descuento
					for itemd in self.descuentos:
						if itemd == str(cell.value).strip():
							#print '----->Descuentos<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),7)
							#print pre.value
							dic_descuentos[itemd] = str(pre.value).strip()

					# busqueda de aportes
					for itema in self.aportes:
						if itema == str(cell.value).strip():
							#print '----->Aportes<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),7)
							#print pre.value
							dic_aportes[itema] = str(pre.value).strip()

					# busqueda de empleador
					for iteme in self.emp:
						if iteme == str(cell.value).strip():
							#print '----->Empleador<---------'
							#print x, '-->> '+cell.value
							pre = sheet.cell(int(x),8)
							#print pre.value
							dic_empleador[iteme] = str(pre.value).strip()

					if str(cell.value).strip() == 'Neto a Pagar':
						pre = sheet.cell(int(x),8)
						netoapagar = str(pre.value)


				#print 'RUC '+ruc
				#print 'Empleador '+empleador
				pdf = PDF('P','mm','A4')
				pdf.set_auto_page_break(True,margin=0)
				pdf.add_page(orientation='P')
				pdf.set_margins(0.5,0.5,0.5)
				pdf.cab_principal(ruc,empleador,periodo)
				pdf.cabecera(dni,nombre,situacion,fecing,tipot,regimen,cuspp,dlaborados,dnolaborados,dsubsidiados,condicion,jothoras,sothoras,msltipo,mslmotivo,msldias,msltipo2,mslmotivo2,msldias2,otrosemp,netoapagar,dic_ingresos,dic_descuentos,dic_aportes,dic_empleador)
				pdf.cab_principal_copy(ruc,empleador,periodo)
				pdf.cabecera_copy(dni,nombre,situacion,fecing,tipot,regimen,cuspp,dlaborados,dnolaborados,dsubsidiados,condicion,jothoras,sothoras,msltipo,mslmotivo,msldias,msltipo2,mslmotivo2,msldias2,otrosemp,netoapagar,dic_ingresos,dic_descuentos,dic_aportes,dic_empleador)
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
