# Como hago pruebas en Python?

Una buena herramienta para mantener nuestro código coherente y sin errores son las pruebas de regresión. En base a éstas podemos saber si los últimos cambios realizados han afectado la funcionalidad existente, cuanto de nuestro código esta siendo utilizado y cuantos criterios de entrega están siendo cumplidos a cabalidad.

Además existen paradigmas de desarrollo que ponen a las pruebas como criterio fundamental para la programación de nuestros productos. Ver [TDD](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas)

Para Python existen múltiples herramientas de pruebas automatizadas, para este ejemplo utilizaremos nose y node-cov.

Nose nos permite ejecutar pruebas unitarias y nos provee algunas funciones que facilitan la definición de las mismas. node-cov nos permite ver cuanto de nuestro código está siendo probado por el set de pruebas.

```
nose==1.3.7
nose-cov==1.6
```
 
La lógica a probar esta contenida en el archivo sum_machine.py

```python
class SumMachine(object):
    def do_your_stuff(self, x, y):
	types = (int, long, float)
	if isinstance(x, types) and isinstance(y, types):
            return x+y
        else:
	    raise ValueError
```

El objetivo de ésta clase, es entregar la funcionalidad de sumar dos números. Las pruebas, las definiremos en el archivo sum_machine_tests.py

```python
import unittest
from sum_machine import SumMachine
 
class SumMachineTest(unittest.TestCase):

    def setUp(self):
        self.machine = SumMachine() 

    def test_sum_two_numbers(self):
        result = self.machine.do_your_stuff(2,2)
        self.assertEqual(4, result)

    def test_fails_when_input_is_string(self):
        self.assertRaises(ValueError, self.machine.do_your_stuff, 'two', 'two')
```

En esta clase podemos ver los siguientes métodos:

1. setUp:  aquí inicializamos el objeto a probar y lo asignamos a self.machine
2. test_sum_two_numbers:  El método 'do_your_stuff' del objeto debe recibir como parámetro dos variables y retornar como resultado la suma de las mismas.  Esta comparación se realiza por medio del método self.assertEqual
3. test_fails_when_input_is_string: El método 'do_your_stuff' debe recibir como parámetros unicamente números. En caso de recibir un string, arrojará un ValueError.  Esta comparación se realiza por medio del método self.assertRaises


Finalmente, para ejecutar nuestras pruebas:
```
nosetests sum_machine_test.py --with-cov
```

La ejecución de éste comando nos arrojará los siguientes resultados:

```
---------- coverage ----------
Name                  Stmts   Miss  Cover
-----------------------------------------
sum_machine.py            6      0   100%
sum_machine_test.py      10      0   100%
-----------------------------------------
TOTAL                    16      0   100%
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```

Explicando que se realizaron 2 pruebas. Las dos pasaron sin problemas y que la cobertura del código por parte de las pruebas es 100%.
