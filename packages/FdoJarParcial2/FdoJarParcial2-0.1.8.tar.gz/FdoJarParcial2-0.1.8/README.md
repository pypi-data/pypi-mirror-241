# Libreria Punto1 parcial2

Instalar con pip install FdoJarParcial2

Para inicializar 
import FdoJarParcial2 as FJ

para usar 
Solucion = F.SuavKernel(Nombre_archivo,h)

para usar kernel Gaussiano
Solucion.SuavizadoGauss()

para usar kernel Epanechnikov
Solucion.SuavizadoEpanechnikov()

para usar kernel Tricube
Solucion.SuavizadoTriCube()

para guardar las gráficas
Solucion.GuardarFigura("Prueba")