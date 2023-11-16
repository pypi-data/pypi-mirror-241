# DIPL

This module is a quick reading/parsing tool for Dimensional Input Parameter Language (DIP) that is a part of larger [scinumtools](https://github.com/vrtulka23/scinumtools) project.
For more information about DIP, please visit its official [documentation](https://vrtulka23.github.io/scinumtools/dip/index.html).
More functionality can be reqested in [GitHub Issues](https://github.com/vrtulka23/dipl/issues).

## Reading DIP code

Loading DIP code from a string is straightforward.

``` python 
>>> import dipl
>>>
>>> text = """
>>> width float = 23.34 cm
>>> age int = 23 yr
>>>   !tags ["body"]
>>> """
>>> dipl.load(text)
{
  'width': (23.34, 'cm'),
  'age': (23, 'yr')
}
```

It is also possible to change data output format, 

``` python
>>> from dipl import Format
>>> dipl.load(text, Format.VALUE)
{
  'width': 23.34,
  'age': 23,
}
```

or to select only requested nodes using query, or tags:

``` python
>>> dipl.load(text, query="width")
{
  'width': (23.34, 'cm'),
}
>>> dipl.load(text, tags=["body"])
{
  'age': (23, 'yr'),
}
```

## Parsing DIP code

Python dictionaries can be parsed into DIP code, provided that they have a proper structure.
An example parsing is shown below.

``` python
>>> import dipl
>>> import numpy as np
>>> from scinumtools.units import Quatity
>>>
>>> data = {
>>>     'body': {
>>>         'width': Quantity(172.34, 'cm'),
>>>         'age': (23, 'yr'),
>>>     },
>>>     'married': True,
>>>     'name': "John",
>>>     'kids': ["Alice","Williams"],
>>>     'lucky_numbers': np.array([23, 34, 5]),
>>> }
>>> dipl.dump(data)
body
  width float = 172.34 cm
  age int = 23 yr
married bool = true
name str = "John"
kids str[2] = ["Alice","Williams"]
lucky_numbers int[3] = [23,34,5]
```