import os
import sys
import ctypes
import subprocess

# CONSTANTES - GUIDs DE POWERCFG
# Estos son identificadores únicos que Windows usa para configuraciones

PLAN_BALANCED = "381b4222-f694-41f0-9685-ff5bb260df2e"  # Plan Equilibrado
CPU_GROUP = "54533251-82BE-4824-96C1-47B60B740D00"      # Grupo CPU
MAX_FREQ = "bc5038f7-23e0-4960-96da-33abaf5935ec"       # Frecuencia máxima
FREQ_INC = "75b0ae3f-bce0-45a7-8c89-c9611c25e100"       # Umbral de aumento
FREQ_DEC = "75b0ae3f-bce0-45a7-8c89-c9611c25e101"       # Umbral de disminución
TURBO_BOOST = "be337238-0d82-4146-a960-4f3749d470c7"    # Modo Turbo Boost


# VARIABLE GLOBAL - PLAN BASE
BASE_PLAN = "SCHEME_CURRENT"  # Por defecto usa el plan activo

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


# DETECTAR CPU

def detectar_cpu():
    """Detecta el fabricante del CPU (Intel, AMD, etc.)"""
    try:
        # Ejecutar comando PowerShell para obtener info del CPU
        comando = [
            'powershell', '-NoProfile', '-Command',
            '(Get-CimInstance Win32_Processor | Select-Object -First 1 -ExpandProperty Manufacturer)'
        ]

        resultado = subprocess.run(
            comando, capture_output=True, text=True, timeout=5)
        cpu_vendor = resultado.stdout.strip()

        # Verificar si es Intel
        if 'Intel' in cpu_vendor or 'GenuineIntel' in cpu_vendor:
            return cpu_vendor, True  # (nombre, es_intel)
        else:
            return cpu_vendor, False

    except Exception as e:
        print(f"[!] Error detectando CPU: {e}")
        return "Desconocido", False


# MOSTRAR MENÚ
def mostrar_menu(cpu_vendor, es_intel):
    """Muestra el menú de opciones"""
    limpiar_pantalla()
    mostrar_logo()

    print(f"\nCPU: {cpu_vendor}")
    if BASE_PLAN == "SCHEME_CURRENT":
        print("Base actual: SCHEME_CURRENT (tu plan activo)")
    else:
        print(f"Base actual: BALANCED ({PLAN_BALANCED})")

    print()

    if not es_intel:
        print("[!] ADVERTENCIA:")
        print("    Esta herramienta está pensada para CPUs Intel.")
        print("    En AMD estos valores pueden no hacer nada.")
        print()

    print("0) Cambiar base (SCHEME_CURRENT / BALANCED)")
    print("1) Turbo Rendimiento")
    print("2) Equilibrado Avanzado")
    print("3) Fresco / Juegos Livianos")
    print("4) Ultra Fresco / Sin Boost")
    print("5) Frecuencia Variable (Estable / Recomendado)")
    print("6) BOOST Extremo")
    print("7) Restaurar plan ORIGINAL")
    print("8) Salir")
    print("9) DEBUG (info técnica)")
    print()

    opcion = input("Elige una opción [0-9]: ")
    return opcion


# APLICAR PERFIL DE TEMPERATURA
def aplicar_perfil(inc, dec, boost_mode, nombre_perfil, base_plan="SCHEME_CURRENT"):
    """
    Aplica un perfil de temperatura modificando el plan de energía

    Parámetros:
    - inc: Umbral de aumento de frecuencia (0-10000)
    - dec: Umbral de disminución de frecuencia (0-10000)
    - boost_mode: Modo Turbo Boost (0=Desactivado, 1=Activado, 2=Agresivo)
    - nombre_perfil: Nombre descriptivo del perfil
    - base_plan: Plan a modificar (SCHEME_CURRENT o GUID específico)
    """

    print(f"\n[*] Aplicando perfil: {nombre_perfil}")
    print("[*] Modificando plan de energía...")

    try:
        # 1) Configurar frecuencia máxima al 100%
        print("    - Configurando frecuencia máxima...")
        subprocess.run([
            'powercfg', '/setacvalueindex', base_plan, CPU_GROUP, MAX_FREQ, '100'
        ], check=True, capture_output=True)

        subprocess.run([
            'powercfg', '/setdcvalueindex', base_plan, CPU_GROUP, MAX_FREQ, '100'
        ], check=True, capture_output=True)

        # 2) Configurar umbral de aumento
        print(f"    - Configurando umbral de aumento: {inc}")
        subprocess.run([
            'powercfg', '/setacvalueindex', base_plan, CPU_GROUP, FREQ_INC, str(
                inc)
        ], check=True, capture_output=True)

        subprocess.run([
            'powercfg', '/setdcvalueindex', base_plan, CPU_GROUP, FREQ_INC, str(
                inc)
        ], check=True, capture_output=True)

        # 3) Configurar umbral de disminución
        print(f"    - Configurando umbral de disminución: {dec}")
        subprocess.run([
            'powercfg', '/setacvalueindex', base_plan, CPU_GROUP, FREQ_DEC, str(
                dec)
        ], check=True, capture_output=True)

        subprocess.run([
            'powercfg', '/setdcvalueindex', base_plan, CPU_GROUP, FREQ_DEC, str(
                dec)
        ], check=True, capture_output=True)

        # 4) Configurar modo Turbo Boost
        print(f"    - Configurando Turbo Boost: {boost_mode}")
        subprocess.run([
            'powercfg', '/setacvalueindex', base_plan, CPU_GROUP, TURBO_BOOST, str(
                boost_mode)
        ], check=True, capture_output=True)

        subprocess.run([
            'powercfg', '/setdcvalueindex', base_plan, CPU_GROUP, TURBO_BOOST, str(
                boost_mode)
        ], check=True, capture_output=True)

        # 5) Activar el plan para que los cambios tomen efecto
        print("    - Activando plan modificado...")
        subprocess.run([
            'powercfg', '/setactive', base_plan
        ], check=True, capture_output=True)

        # Éxito
        print("\n" + "=" * 50)
        print(f"[OK] {nombre_perfil} aplicado correctamente")
        print("=" * 50)
        print("\nNota:")
        print("- Los cambios son inmediatos")
        print("- Monitorea tus temperaturas con HWiNFO o similar")
        print("- Si no notas cambios, tu software OEM puede estar")
        print("  reescribiendo la configuración (ASUS Armoury, MSI Center, etc)")

        return True

    except subprocess.CalledProcessError as e:
        print(f"\n[!] ERROR al aplicar perfil: {e}")
        print("[!] Asegúrate de ejecutar como ADMINISTRADOR")
        return False
    except Exception as e:
        print(f"\n[!] ERROR inesperado: {e}")
        return False


# CAMBIAR PLAN BASE
def cambiar_base():
    """Alterna entre SCHEME_CURRENT y BALANCED"""
    global BASE_PLAN

    if BASE_PLAN == "SCHEME_CURRENT":
        BASE_PLAN = PLAN_BALANCED
        print("\n[OK] Base cambiada a: BALANCED")
        print(f"    GUID: {PLAN_BALANCED}")
    else:
        BASE_PLAN = "SCHEME_CURRENT"
        print("\n[OK] Base cambiada a: SCHEME_CURRENT (tu plan activo)")

    return BASE_PLAN

# Funcion principal


def main():
    # Verificar permisos
    if not es_administrador():
        print("\n[!] NECESITAS PERMISOS DE ADMINISTRADOR")
        print("    Click derecho > 'Ejecutar como administrador'\n")
        input("Presiona ENTER para salir...")
        sys.exit(1)

    # Detectar CPU una sola vez
    print("Detectando CPU...")
    cpu_vendor, es_intel = detectar_cpu()

    # Loop principal del menú
    while True:
        opcion = mostrar_menu(cpu_vendor, es_intel)

        if opcion == "0":
            print("\n[i] Función 'Cambiar base' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "1":
            print("\n[i] Modo 'Turbo Rendimiento' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "2":
            print("\n[i] Modo 'Equilibrado Avanzado' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "3":
            print("\n[i] Modo 'Fresco / Juegos Livianos' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "4":
            print("\n[i] Modo 'Ultra Fresco / Sin Boost' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "5":
            print("\n[i] Modo 'Frecuencia Variable' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "6":
            print("\n[i] Modo 'BOOST Extremo' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "7":
            print("\n[i] Función 'Restaurar plan' - En desarrollo")
            input("\nPresiona ENTER para continuar...")

        elif opcion == "8":
            limpiar_pantalla()
            print("=" * 40)
            print("  Gracias por usar el programa")
            print("=" * 40)
            break  # Salir del loop

        elif opcion == "9":
            print("\n===== DEBUG INFO =====")
            print(f"CPU_VENDOR = {cpu_vendor}")
            print(f"ES_INTEL = {es_intel}")
            print(f"PLAN_BALANCED = {PLAN_BALANCED}")
            print("=" * 22)
            input("\nPresiona ENTER para continuar...")

        else:
            print("\n[!] Opción no válida")
            input("\nPresiona ENTER para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
