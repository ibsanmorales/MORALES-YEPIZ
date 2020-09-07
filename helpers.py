#Libreria de OS
import os
#Datos de Tienda
import lifestore_file as lifeStoreFile
#Datos de Usuarios
import users_system as userSystem 

#Validacion de Usuario
def findUser(password, nombre):
  for user in userSystem.users:
      if user[0] == nombre and user[1] == password: 
        return user
  return [] 
        
#Metodo para continuar o salir
def yes_or_no(question):
    while "the answer is invalid":
      os.system('clear')
      reply = str(input(question+' (y/n): ')).lower().strip()
      if reply[0] == 'y':
          return 'y'
      if reply[0] == 'n':
          return 'n'
#Metodo para regresar a menu
def yes_or_no_regresar(question):
    while "the answer is invalid":
      #os.system('clear')
      reply = str(input(question+' (y/n): ')).lower().strip()
      if reply[0] == 'y':
          return 'y'
      if reply[0] == 'n':
          return 'n'
#Metodos principales 
def top50MayorMenorVenta(sortMayorMenor):
  productos_mayor_ventas = []
  for producto in lifeStoreFile.lifestore_products:
    ventas_producto = 0
    for sale in lifeStoreFile.lifestore_sales:
      if (producto[0]== sale[1]):
        ventas_producto += 1
    productos_mayor_ventas.append([producto[0],producto[1],ventas_producto,producto[3]])
  if(sortMayorMenor == 1):
    productos_mayor_ventas.sort(key=lambda x: x[2], reverse = True)
    cantidad_productos = len(productos_mayor_ventas)
    if(cantidad_productos>50):
      for product_mayor in productos_mayor_ventas[0:50]:
        if(product_mayor[2] !=  0):
          print(" ID: ",product_mayor[0]," Ventas: ",product_mayor[2], " Categoria: ", product_mayor[3])
    else:
      for product_mayor in productos_mayor_ventas:
        if(product_mayor[2] !=  0):
          print(" ID: ",product_mayor[0]," Ventas: ",product_mayor[2], " Categoria: ", product_mayor[3])
  else:
    productos_mayor_ventas.sort(key=lambda x: x[2])
    cantidad_productos = len(productos_mayor_ventas)
    if(cantidad_productos>50):
      for product_mayor in productos_mayor_ventas[0:50]:
          print(" ID: ",product_mayor[0]," Ventas: ",product_mayor[2], " Categoria: ", product_mayor[3])
    else:
      for product_mayor in productos_mayor_ventas:
          print(" ID: ",product_mayor[0]," Ventas: ",product_mayor[2], " Categoria: ", product_mayor[3])
  
def top100MayorMenorBusqueda(sortMayorMenorBusqueda):
  productos_mayor_busqueda = []
  for producto in lifeStoreFile.lifestore_products:
    busquedas_producto = 0
    for search in lifeStoreFile.lifestore_searches:
      if (producto[0]== search[1]):
        busquedas_producto += 1
    productos_mayor_busqueda.append([producto[0],producto[1],busquedas_producto,producto[3]])
  if(sortMayorMenorBusqueda == 1):
    productos_mayor_busqueda.sort(key=lambda x: x[2], reverse = True)
    cantidad_productos = len(productos_mayor_busqueda)
    if(cantidad_productos>100):
      for product_mayor in productos_mayor_busqueda[0:100]:
        if(product_mayor[2] !=  0):
          print(" ID: ",product_mayor[0]," Busquedas: ",product_mayor[2], " Categoria: ", product_mayor[3])
    else:
      for product_mayor in productos_mayor_busqueda:
        if(product_mayor[2] !=  0):
          print(" ID: ",product_mayor[0]," Busquedas: ",product_mayor[2], " Categoria: ", product_mayor[3])
  else:
    productos_mayor_busqueda.sort(key=lambda x: x[2])
    cantidad_productos = len(productos_mayor_busqueda)
    if(cantidad_productos>100):
      for product_mayor in productos_mayor_busqueda[0:100]:
          print(" ID: ",product_mayor[0]," Busquedas: ",product_mayor[2], " Categoria: ", product_mayor[3])
    else:
      for product_mayor in productos_mayor_busqueda:
          print(" ID: ",product_mayor[0]," Busquedas: ",product_mayor[2], " Categoria: ", product_mayor[3])

def top50MayorMenorVentaPorCategoria(sortMayorMenor):
  productos_mayor_ventas = []
  categorias_productos = []
  categorias_productos_repetida =[]
  for producto in lifeStoreFile.lifestore_products:
    ventas_producto = 0
    for sale in lifeStoreFile.lifestore_sales:
      if (producto[0]== sale[1]):
        ventas_producto += 1
    productos_mayor_ventas.append([producto[0],producto[1],ventas_producto,producto[3]])
  if(sortMayorMenor == 1):
    productos_mayor_ventas.sort(key=lambda x: x[2], reverse = True)
    cantidad_productos = len(productos_mayor_ventas)
    if(cantidad_productos>50):
      find_categorias_producto = productos_mayor_ventas[0:50]
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_ventas[0:50]:
          if(producto_categorizado[2] !=  0):
            if(categoria_filtro == producto_categorizado[3]):
              print(' ID: ',producto_categorizado[0],' Ventas: ',producto_categorizado[2])
    else:
      find_categorias_producto = productos_mayor_ventas
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_ventas:
          if(producto_categorizado[2] !=  0):
            if(categoria_filtro == producto_categorizado[3]):
              print(' ID: ',producto_categorizado[0],' Ventas: ',producto_categorizado[2])
  else:
    productos_mayor_ventas.sort(key=lambda x: x[2])
    cantidad_productos = len(productos_mayor_ventas)
    if(cantidad_productos>50):
      find_categorias_producto = productos_mayor_ventas[0:50]
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_ventas[0:50]:
          if(categoria_filtro == producto_categorizado[3]):
            print(' ID: ',producto_categorizado[0],' Ventas: ',producto_categorizado[2])
    else:
      find_categorias_producto = productos_mayor_ventas
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_ventas:
          if(categoria_filtro == producto_categorizado[3]):
            print(' ID: ',producto_categorizado[0],' Ventas: ',producto_categorizado[2])
    
def top100MayorMenorBusquedaPorCategoria(sortMayorMenorBusqueda):
  productos_mayor_busqueda = []
  categorias_productos = []
  categorias_productos_repetida =[]
  for producto in lifeStoreFile.lifestore_products:
    busquedas_producto = 0
    for search in lifeStoreFile.lifestore_searches:
      if (producto[0]== search[1]):
        busquedas_producto += 1
    productos_mayor_busqueda.append([producto[0],producto[1],busquedas_producto,producto[3]])
  if(sortMayorMenorBusqueda == 1):
    productos_mayor_busqueda.sort(key=lambda x: x[2], reverse = True)
    cantidad_productos = len(productos_mayor_busqueda)
    if(cantidad_productos>100):
      find_categorias_producto = productos_mayor_busqueda[0:100]
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_busqueda[0:100]:
          if(categoria_filtro == producto_categorizado[3]):
            print(' ID: ',producto_categorizado[0],' Busquedas: ',producto_categorizado[2])
    else:
      find_categorias_producto = productos_mayor_busqueda
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_busqueda:
          if(categoria_filtro == producto_categorizado[3]):
            print(' ID: ',producto_categorizado[0],' Busquedas: ',producto_categorizado[2])
  else:
    productos_mayor_busqueda.sort(key=lambda x: x[2])
    cantidad_productos = len(productos_mayor_busqueda)
    if(cantidad_productos>100):
      find_categorias_producto = productos_mayor_busqueda[0:100]
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_busqueda[0:100]:
          if(categoria_filtro == producto_categorizado[3]):
            print(' ID: ',producto_categorizado[0],' Busquedas: ',producto_categorizado[2])
    else:
      find_categorias_producto = productos_mayor_busqueda
      for categoria in find_categorias_producto:
        categorias_productos_repetida.append(categoria[3])
      categorias_productos = list(dict.fromkeys(categorias_productos_repetida))
      '''for cate_product in categorias_productos:
        print(cate_product)'''
      for categoria_filtro in categorias_productos:
        print('-----',categoria_filtro,'-----')
        for producto_categorizado in productos_mayor_busqueda:
          if(categoria_filtro == producto_categorizado[3]):
            print(' ID: ',producto_categorizado[0],' Busquedas: ',producto_categorizado[2])

def top20MejorPeorcalificacion(menorMayorCalificacion):
  productos_calificacion = []
  for producto in lifeStoreFile.lifestore_products:
    suma_calificacion = 0
    cantidad_calificada = 0
    promedio_calificacion = 0
    for sale in lifeStoreFile.lifestore_sales:
      if (producto[0]== sale[1]):
        cantidad_calificada += 1
        suma_calificacion += sale[2]
    if(cantidad_calificada > 0 and suma_calificacion > 0):
      promedio_calificacion = suma_calificacion/cantidad_calificada
      productos_calificacion.append([producto[0],producto[1],promedio_calificacion,producto[3]])
    elif(cantidad_calificada > 0 and suma_calificacion == 0):
      promedio_calificacion = 0
      productos_calificacion.append([producto[0],producto[1],promedio_calificacion,producto[3]])
  cantidad_productos = len(productos_calificacion)
  if(cantidad_productos>20):
    if(menorMayorCalificacion == 1):
      productos_calificacion.sort(key=lambda x: x[2], reverse = True)
      for producto_calificado in productos_calificacion[0:20]:
        print(" ID: ",producto_calificado[0]," Calificacion: ",round(producto_calificado[2],2), " Categoria: ", producto_calificado[3])
    else:
      productos_calificacion.sort(key=lambda x: x[2])
      for producto_calificado in productos_calificacion[0:20]:
        print(" ID: ",producto_calificado[0]," Calificacion: ",round(producto_calificado[2],2), " Categoria: ", producto_calificado[3])
  else:
    if(menorMayorCalificacion == 1):
      productos_calificacion.sort(key=lambda x: x[2], reverse = True)
      for producto_calificado in productos_calificacion:
        print(" ID: ",producto_calificado[0]," Calificacion: ",round(producto_calificado[2],2), " Categoria: ", producto_calificado[3])
    else:
      productos_calificacion.sort(key=lambda x: x[2])
      for producto_calificado in productos_calificacion:
        print(" ID: ",producto_calificado[0]," Calificacion: ",round(producto_calificado[2],2), " Categoria: ", producto_calificado[3])

def resumenVentas():
  sumaTotalVentas()
  print('-------')
  ventaPromedioMensual()

def sumaTotalVentas():
  sumaTotalVentas = 0
  for producto in lifeStoreFile.lifestore_products:
    for sale_producto in lifeStoreFile.lifestore_sales:
      if(producto[0] == sale_producto[1]):
        sumaTotalVentas += producto[2]
  print('TOTAL INGRESOS: ',sumaTotalVentas)

def ventaPromedioMensual():
  ventas_producto = []
  anos_ventas = []
  meses_promedio_venta = []
  ordenar_meses_mayor_venta = []
  
  meses = ['01','02','03','04','05','06','07','08','09','10','11','12',]
  for producto in lifeStoreFile.lifestore_products:
    for sale_producto in lifeStoreFile.lifestore_sales:
      if(producto[0] == sale_producto[1]):
        ventas_producto.append([producto[0],producto[2],sale_producto[3]])
  print('VENTAS POR AÑO:')      
  for venta_p in ventas_producto:
    anos_ventas.append(venta_p[2][6:10])
  ano_ventas = list(dict.fromkeys(anos_ventas))
  
  for ano in ano_ventas:
    total_porano = 0
    for mes in meses:
      total_mes_venta = 0
      total_venta_real = 0
      for venta in ventas_producto:
        if(mes == venta[2][3:5] and ano == venta[2][6:10]):
          total_venta_real += 1
          total_mes_venta += venta[1]
      #print(' Mes: ',mes,' Total: ',total_mes_venta)
      meses_promedio_venta.append([mes, ano, total_mes_venta,total_venta_real])
      total_porano += total_mes_venta
    print('Año: ',ano,' Total: ',total_porano)
  print('-------')
  print('PROMEDIO DE VENTA POR MES:') 
  for mes in meses:
    total_mes_anos = 0
    numero_mes_ano = 0
    promedio_venta_mes_ano = 0
    promedio_ventas_mensual = 0
    total_venta_item_mes = 0
    for mes_prome in meses_promedio_venta:
      if(mes == mes_prome[0]):
        total_venta_item_mes += mes_prome[3]
        total_mes_anos += mes_prome[2]
        numero_mes_ano += 1
    if(total_mes_anos > 0):
      promedio_venta_mes_ano = total_mes_anos / numero_mes_ano
      promedio_ventas_mensual = total_venta_item_mes / numero_mes_ano
    else:
      promedio_venta_mes_ano = 0
      promedio_ventas_mensual = 0
    print('Mes',mes,'Promedio Venta: ', round(promedio_venta_mes_ano,2), ' N° Ventas Promedio: ', round(promedio_ventas_mensual,2))
    ordenar_meses_mayor_venta.append([mes, promedio_venta_mes_ano,promedio_ventas_mensual])

  print('-------')
  print('MESES CON MAYOR VENTA:') 
  ordenar_meses_mayor_venta.sort(key=lambda x : x[2], reverse = True)
  for mes_order in ordenar_meses_mayor_venta:
    print('Mes: ',mes_order[0],'Total: ',round(mes_order[1],2),'Items: ',round(mes_order[2],2))

  