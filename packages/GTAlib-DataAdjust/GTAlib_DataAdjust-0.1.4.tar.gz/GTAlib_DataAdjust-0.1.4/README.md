# DataAdjustment

`DataAdjustment` es una clase Python que proporciona funcionalidades para el ajuste de datos utilizando el metodo del kernel Gaussiano. Esta clase es util para suavizar series de tiempo de datos, lo que puede ayudar a visualizar tendencias y patrones de manera mas clara.

## Requisitos

- Python 3.11.6
- numpy 1.26.1
- pandas 2.1.2
- matplotlib 3.8.1



## Instalacion

Para instalar la libreria, utiliza el comando

```bash
pip install GTAlib-DataAdjust
```


## Uso
La estructura base para implementar la libreria es:

```python
# Importar la clase DataAdjustment
from GTAlib_DataAdjust import DataAdjust

# Crear una instancia de DataAdjustment con el archivo CSV de datos y valor de sigma (opcional)
adjustment = DataAjust('datos.csv', sigma=1)

# Graficar la curva suavizada junto con los datos reales
adjustment.plot_smooth_curve()

# Graficar la derivada de la curva suavizada
adjustment.plot_derivative()
```

Se debe tener en cuenta que el archivo CSV que se use como argumento debe contener las columnas 'nuevos_casos' y 'fecha_actualizacion'.
