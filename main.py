from ManejadorAlumno import ManejadorAlumno
from ManejadorMaterias import ManejadorMateria
import os
def m_menu():
    print ("1: Informar promedio con y sin aplazos de un alumno")
    print ("2: Informar estudiantes promocionales aprobados por materia")
    print ("3: Obtener listado ordenado según año y alfabéticamente de alumnos")
    print ("4: Salir")
    
if __name__=='__main__':
    lista_alum=ManejadorAlumno(0)
    lista_mat=ManejadorMateria()
    lista_alum.carga_alumnos()
    lista_mat.carga_materias()
    opc=None
    while opc!='4':
        os.system('cls')
        m_menu()
        opc=input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc=='1':
            dni=input("Ingrese el dni del alumno ")
            lista_mat.mostrarprom_alumno(dni)
            aux=input("\nIngrese cualquier tecla para continuar\n")
        if opc=='2':
            materia=input("Ingrese la materia a buscar: ")
            lista_mat.mostrar_aprobados(lista_alum,materia)
            aux=input("\nIngrese cualquier tecla para continuar\n")
        if opc=='3':
            lista_alum.ordenar_lista()
            aux=input("\nIngrese cualquier tecla para continuar\n")
        
    print("Gracias por usar el sistema")