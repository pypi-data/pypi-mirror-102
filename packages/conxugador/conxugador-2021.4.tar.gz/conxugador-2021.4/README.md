[//]: # "This tool conjugates Galician verbs and can add them enclitic pronouns."
[//]: # "Copyright \(C\) 2020 Andrés Vieites Pérez"

[//]: # "This program is free software: you can redistribute it and/or modify"
[//]: # "it under the terms of the GNU General Public License as published by"
[//]: # "the Free Software Foundation, either version 3 of the License, or"
[//]: # "any later version."

[//]: # "This program is distributed in the hope that it will be useful,"
[//]: # "but WITHOUT ANY WARRANTY; without even the implied warranty of"
[//]: # "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the"
[//]: # "GNU General Public License for more details."

[//]: # "You should have received a copy of the GNU General Public License"
[//]: # "along with this program.  If not, see <https://www.gnu.org/licenses/>."

# Conxugador

This tool conjugates Galician verbs and will be able to add (not at the moment) enclitic pronouns to them, it is a Python reconstruction of [Conshuga](https://gramatica.usc.es/pln/gl/tools/conjugador/conjugador.php). This Software is distributed under the terms of the GNU General Public License Version 3. 

You can use it as command line tool or as a library. You can download it from a shell with the command below:
```bash
$ git clone https://gitlab.com/avieites/conxugador.git
```

Or, alternatively, you can install it from [PyPI](https://pypi.org/project/conxugador/) with command:

``````bash
$ pip install conxugador
``````

## Examples

If you clone the project from [GitLab](https://gitlab.com/avieites/conxugador), you can execute it from the root folder:

```bash
$ python conxugador ferver
Conxugador Copyright (C) 2021 Andrés Vieites Pérez
This program comes with ABSOLUTELY NO WARRANTY; for details read COPYING.
This is free software, and you are welcome to redistribute it.

FN:ferver:fervendo:fervido
IP:ferver:ferveres:ferver:fervermos:ferverdes:ferveren
PI:fervo:ferves:ferve:fervemos:fervedes:ferven
II:fervía:fervías:fervía:ferviamos:ferviades:fervían
EI:fervín:ferviches:ferveu:fervemos:fervestes:ferveron
MI:fervera:ferveras:fervera:ferveramos:ferverades:ferveran
TI:fervería:ferverías:fervería:ferveriamos:ferveriades:ferverían
FI:ferverei:ferverás:ferverá:ferveremos:ferveredes:ferverán
PS:ferva:fervas:ferva:fervamos:fervades:fervan
IS:fervese:ferveses:fervese:fervésemos:fervésedes:fervesen
FS:ferver:ferveres:ferver:fervermos:ferverdes:ferveren
IA:ferve:ferva:fervamos:fervede:fervan
IN:fervas:ferva:fervamos:fervades:fervan
```

where:
* FN: formas nominais: infinitivo, xerundio e participio 
* IP: infinitivo persoal/infinitivo flexionado/infinitivo conxugado 
* PI: presente do indicativo 
* II: pretérito imperfecto do indicativo/copretérito do indicativo
* EI: pretérito perfecto do indicativo/pretérito do indicativo
* MI: pretérito pluscuamperfecto do indicativo/mais-que-perfecto do indicativo/antepretérito do indicativo
* TI: condicional/futuro do pretérito do indicativo/pospretérito do indicativo
* FI: futuro do presente do indicativo/futuro do indicativo
* PS: presente do subxuntivo 
* IS: pretérifo imperfecto do subxuntivo/pretérito do subxuntivo
* FS: futuro do subxuntivo 
* IA: imperativo afirmativo
* IN: imperativo negativo

If you installed it with pip:

`````` bash
$ python -m conxugador ferver
``````

or:

``````bash
$ python
Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import conxugador
>>> conxugador.conjugate('ferver')
{'tenses': {'fn': ['ferver', 'fervendo', 'fervido'], 'pi': ['fervo', 'ferves', 'ferve', 'fervemos', 'fervedes', 'ferven'], 'ii': ['fervía', 'fervías', 'fervía', 'ferviamos', 'ferviades', 'fervían'], 'ia': ['ferve', 'ferva', 'fervamos', 'fervede', 'fervan'], 'ip': ['ferver', 'ferveres', 'ferver', 'fervermos', 'ferverdes', 'ferveren'], 'ei': ['fervín', 'ferviches', 'ferveu', 'fervemos', 'fervestes', 'ferveron'], 'mi': ['fervera', 'ferveras', 'fervera', 'ferveramos', 'ferverades', 'ferveran'], 'ti': ['fervería', 'ferverías', 'fervería', 'ferveriamos', 'ferveriades', 'ferverían'], 'fi': ['ferverei', 'ferverás', 'ferverá', 'ferveremos', 'ferveredes', 'ferverán'], 'ps': ['ferva', 'fervas', 'ferva', 'fervamos', 'fervades', 'fervan'], 'is': ['fervese', 'ferveses', 'fervese', 'fervésemos', 'fervésedes', 'fervesen'], 'fs': ['ferver', 'ferveres', 'ferver', 'fervermos', 'ferverdes', 'ferveren'], 'in': ['fervas', 'ferva', 'fervamos', 'fervades', 'fervan']}}
``````

besides if you have the [Python scripts folder](https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html#console-scripts) in your PATH (either `C:\Program Files\Python39\Scripts` or `C:\Users\<user>\AppData\Roaming\Python\Python39\Scripts`) you can run it directly:

``````bash
$ conxugador.exe ferver
Conxugador Copyright (C) 2021 Andrés Vieites Pérez
This program comes with ABSOLUTELY NO WARRANTY; for details read COPYING.
This is free software, and you are welcome to redistribute it.

FN:ferver:fervendo:fervido
IP:ferver:ferveres:ferver:fervermos:ferverdes:ferveren
PI:fervo:ferves:ferve:fervemos:fervedes:ferven
II:fervía:fervías:fervía:ferviamos:ferviades:fervían
EI:fervín:ferviches:ferveu:fervemos:fervestes:ferveron
MI:fervera:ferveras:fervera:ferveramos:ferverades:ferveran
TI:fervería:ferverías:fervería:ferveriamos:ferveriades:ferverían
FI:ferverei:ferverás:ferverá:ferveremos:ferveredes:ferverán
PS:ferva:fervas:ferva:fervamos:fervades:fervan
IS:fervese:ferveses:fervese:fervésemos:fervésedes:fervesen
FS:ferver:ferveres:ferver:fervermos:ferverdes:ferveren
IA:ferve:ferva:fervamos:fervede:fervan
IN:fervas:ferva:fervamos:fervades:fervan
``````

