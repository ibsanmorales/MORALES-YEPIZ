#Metodos Genericos para Reutilizar
import helpers as hp
#Libreria Systema, principalmente se utiliza para limpiar la pantalla
import os

salir_programa = 'y'
#Ciclo de inicio de programa
while salir_programa == 'y':
  os.system('clear')
  print("**********************************************")
  print("LOGIN, Ingrese sus datos")
  print("**********************************************")
  print("\n")
  usuario_nombre = input("Usuario: ")
  usuario_clave = input("Password: ")

  user_logger = hp.findUser(usuario_clave,usuario_nombre)
  #Validacion para ingresar al programa si usuario existe
  if (user_logger != []):
    os.system('clear')
    print("Bienvenido "+user_logger[0])
    exit = False
    #Deteccion de rol Usuario
    if(user_logger[2] == "Administrador"):
      #Ciclo de Menu
      while exit == False:
        print("**********************************************")
        print("MENU DE CONSULTA")
        print("**********************************************")
        print("1.- Top 50 Productos Mayor Venta")
        print("2.- Top 100 Productos Mayor Busqueda")
        print("3.- Top 50 Productos Menor Venta por Categoria")
        print("4.- Top 100 Productos Menor Busqueda por Categoria")
        print("5.- Top 20 Productos con Mejor y Peor Reseña")
        print("6.- Resumen de Ventas")
        print("7.- Salir")
        print("\n")
        menu_item_select = input("Introdusca la opcion deseada: ")
        #Comparaciones para realizar los proceso correspondientes al menu seleccionado
        if(menu_item_select == '1'):
          regresar_programa = 'n'
          while regresar_programa == 'n':
            os.system('clear')
            print("**********************************************")
            print("Top 50 Productos Mayor Venta")
            print("**********************************************")
            hp.top50MayorMenorVenta(1)
            print("\n")
            regresar_programa = hp.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
          os.system('clear')
        elif(menu_item_select == "2"):
          regresar_programa = 'n'
          while regresar_programa == 'n':
            os.system('clear')
            print("**********************************************")
            print("Top 100 Productos Mayor Busqueda")
            print("**********************************************")
            hp.top100MayorMenorBusqueda(1)
            print("\n")
            regresar_programa = hp.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
          os.system('clear')
        elif(menu_item_select == "3"):
          regresar_programa = 'n'
          while regresar_programa == 'n':
            os.system('clear')
            print("**********************************************")
            print("Top 50 Productos Menor Venta por Categoria")
            print("**********************************************")
            hp.top50MayorMenorVentaPorCategoria(0)
            print("\n")
            regresar_programa = hp.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
          os.system('clear')
        elif(menu_item_select == "4"):
          regresar_programa = 'n'
          while regresar_programa == 'n':
            os.system('clear')
            print("**********************************************")
            print("Top 100 Productos Menor Busqueda por Categoria")
            print("**********************************************")
            hp.top100MayorMenorBusquedaPorCategoria(0)
            print("\n")
            regresar_programa = hp.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
          os.system('clear')
        elif(menu_item_select == "5"):
          regresar_programa = 'n'
          while regresar_programa == 'n':
            os.system('clear')
            print("**********************************************")
            print("Top 20 Productos con Mejor y Peor Calificacion")
            print("**********************************************")
            print("\n")
            print("Top 20 Productos Mejor")
            hp.top20MejorPeorcalificacion(1)
            print("\n")
            print("Top 20 Productos Peor")
            hp.top20MejorPeorcalificacion(0)
            print("\n")
            regresar_programa = hp.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
          os.system('clear')
        elif(menu_item_select == "6"):
          regresar_programa = 'n'
          while regresar_programa == 'n':
            os.system('clear')
            print("**********************************************")
            print("Resumen Ventas")
            print("**********************************************")
            hp.resumenVentas()
            print("\n")
            regresar_programa = hp.yes_or_no_regresar("Salir de consulta o realizar nuevamente la consulta ")
          os.system('clear')
        elif(menu_item_select == "7"):
          os.system('clear')
          exit = True
        else:
          os.system('clear')
          print("\n")
          print("**** ERROR: Seleccione una Opcion valida ****")
          print("\n")

    elif(user_logger[2] == "Cliente"):
      while exit == False:
        print("Hola Cliente")
    else:
      print("Usuario Sin Rol")
      salir_programa = hp.yes_or_no("desea intentar de nuevo")
  else:
    print("Usuario incorrecto")
    salir_programa = hp.yes_or_no("Usuario o clave incorrecta, desea intentar de nuevo")

