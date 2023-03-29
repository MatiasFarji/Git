from struct import pack
from setuptools import setup

setup(
    name="Modulo",
    version="1.0",
    author="Matias Lior Farji Mandler",
    packages=['Modulo','Modulo.operaciones'], #Nombre del paquete (Directorio/Carpeta donde se encuentran los modulos)
)

#Para generar el paquete de instalacion comprimido, se debe ingresar a la terminal, e ingresar el comando: python setup.py sdist
#Para instalar el paquete en el sistema, utilizar pip install "Nombre del archivo"
#Para actualizar el paquete en el sistema, utilizar pip install "Nombre del archivo" --upgrade
#Para desinstalar el paquete en el sistema, utilizar pip uninstall "Nombre del paquete, ejemplo usuarioprincipal"
# pip list muestra los paquetes instalados
#Para luego importar la funcion se debe hacer un form desde el nombre del modulo.nombrepaquete (Ejemplo from usuarioprincipal.usuarioprincipal import usuario)