# 🌡️ CPU Temperature Controller

Programa gratuito y de código abierto para controlar las temperaturas de tu CPU Intel mediante perfiles de rendimiento personalizados.

## 📋 Características

- ✅ 6 perfiles de temperatura predefinidos
- ✅ Control del Intel Turbo Boost
- ✅ Sistema de backup y restauración
- ✅ Compatible con Windows 10/11
- ✅ Interfaz de consola intuitiva
- ✅ 100% gratuito y open source

## 🎯 Perfiles Disponibles

| Perfil | Descripción | Uso Recomendado |
|--------|-------------|-----------------|
| **Turbo Rendimiento** | Máximo rendimiento | Gaming exigente |
| **Equilibrado Avanzado** | Balance rendimiento/temperatura | Uso general |
| **Fresco / Juegos Livianos** | Temperaturas reducidas | Juegos casuales |
| **Ultra Fresco** | Mínimas temperaturas (Turbo OFF) | Laptop sobrecalentado |
| **Frecuencia Variable** | Estable y recomendado | Uso diario |
| **BOOST Extremo** | Rendimiento máximo | Benchmarks |

## 💾 Descarga

### Opción 1: Ejecutable (Windows - No requiere Python)
1. Ve a [Releases](../../releases)
2. Descarga `CPU_Temperature_Controller.exe`
3. Click derecho → "Ejecutar como administrador"

### Opción 2: Código Fuente (Requiere Python 3.7+)
```bash
git clone https://github.com/STYLEJV/CPU-Temperature-Controller.git
cd CPU-Temperature-Controller
python cpu_temperature_controller.py
```

## ⚙️ Requisitos

- **Sistema Operativo:** Windows 10/11
- **CPU:** Intel (recomendado)
- **Permisos:** Administrador

## 🚀 Uso

1. Ejecuta como **administrador**
2. Elige un perfil del menú (0-9)
3. Los cambios son instantáneos
4. Usa opción 7 para restaurar configuración original

## 🛡️ Seguridad

- ✅ Código abierto (puedes revisar cada línea)
- ✅ No requiere conexión a internet
- ✅ No recopila datos
- ✅ Sistema de backup automático

## ⚠️ Notas Importantes

- **Software OEM:** Si tienes ASUS Armoury Crate, MSI Center, o Acer PredatorSense, pueden interferir con los cambios.
- **AMD:** El programa funciona pero puede tener efectos limitados en CPUs AMD.
- **Monitoreo:** Usa HWiNFO64 o similar para ver las temperaturas en tiempo real.

## 🤝 Contribuir


## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**STYLEJV**

## 🙏 Agradecimientos

Inspirado en la necesidad de controlar temperaturas de laptops gaming sin software propietario.

---

⭐ Si este proyecto te ayudó, ¡dale una estrella en GitHub!