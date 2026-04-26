import os
import sys
import ctypes
import subprocess

# Verifica permisos de administrador


def es_administrador():
    """Verifica si el script se está ejecutando con privilegios de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Limpiar pantalla


def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls')

# Mostrar logo


def mostrar_logo():
    """Muestra el logo del programa."""
    print("""
     SSSS   TTTTT  Y   Y  L      EEEEE      JJJJJ  V   V
    S         T     Y Y   L      E            J    V   V
     SSS      T      Y    L      EEEE         J     V V 
        S     T      Y    L      E            J      V  
    SSSS      T      Y    LLLLL  EEEEE     JJJ       V  

""")
    print("=" * 60)
    print("    CPU Temperature Controller By STYLEJV")

# Funcion principal


def main():
    # Verificar permisos de administrador
    if not es_administrador():
        print("\n[!] NECESITAS PERMISOS DE ADMINISTRADOR")
        print("    Click derecho > 'Ejecutar como administrador'\n")
        input("Presiona ENTER para salir...")
        sys.exit(1)
    # Limpiar pantalla y mostrar logo
    limpiar_pantalla()
    mostrar_logo()
    print("\n[OK] Programa ejecutándose con permisos de administrador")
    print("\nEsto es solo una base iremos agregando funciones poco a poco")
    input("\nPresiona ENTER para salir...")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
