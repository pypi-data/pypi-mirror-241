from scinumtools.dip import DIP
from scinumtools.dip.settings import Format, Sign
from scinumtools.dip.nodes import StringNode, BooleanNode, FloatNode, IntegerNode
from scinumtools.units import Quantity
#from scinumtools.dip.exports.config import ExportConfig
import json
import numpy as np

def load(text:str, format:Format = Format.TUPLE, query: str=None, tags: list=None):
    """ Parse data from a DIP code
    """
    with DIP() as dip:
        dip.from_string(text)
        env = dip.parse()
        return env.data(format=format, query=query, tags=tags)
        
def _dump_value(value: dict, path: list, indent: int):
    name = Sign.SEPARATOR.join(path)

    if isinstance(value, tuple):
        value, unit = value[0], value[1]
    elif isinstance(value, Quantity):
        value, unit = value.value(), value.units()
    else:
        unit = None
    
    if isinstance(value, str):
        value = f"\"{value}\""
        dtype = StringNode.keyword
    elif isinstance(value, bool):
        value = "true" if value else "false"
        dtype = BooleanNode.keyword
    elif isinstance(value, int):
        value = str(value)
        dtype = IntegerNode.keyword
    elif isinstance(value, float):
        value = str(value)
        dtype = FloatNode.keyword
    elif isinstance(value, (list, np.ndarray)):
        if isinstance(value, np.ndarray):
            shape = ','.join([str(i) for i in value.shape])
            value = value.tolist()
        else:
            shape = ','.join([str(i) for i in np.array(value).shape])
        if all(map(lambda i: isinstance(i, int), value)):
            dtype = IntegerNode.keyword
        elif all(map(lambda i: isinstance(i, float), value)):
            dtype = FloatNode.keyword
        elif all(map(lambda i: isinstance(i, str), value)):
            dtype = StringNode.keyword
        elif all(map(lambda i: isinstance(i, bool), value)):
            dtype = BooleanNode.keyword
        else:
            raise Exception("Array values does not have the same type", value)
        dtype += f"[{shape}]"
        value = json.dumps(value, separators=(',',':'))
    if unit:
        text = f"{name} {dtype} = {value} {unit}"
    else:
        text = f"{name} {dtype} = {value}"
        
    return " "*indent + text
        
def _dump_node(data: dict, path: list, indent: int):
    lines = []
    if len(data)>1 and indent is not None:
        text =  " "*indent + Sign.SEPARATOR.join(path)
        lines.append(text)
        path = []
        new_indent = indent + 2
    elif indent is None:
        new_indent = 0
    else:
        new_indent = indent
    for key, value in data.items():
        new_path = path+[key]
        if isinstance(value, dict):
            lines += _dump_node(value, new_path, new_indent)
        else:
            lines.append(_dump_value(value, new_path, new_indent))
    return lines

def dump(data: dict):
    """ Dump Python data into a DIP code
    """
    if not isinstance(data, dict):
        raise Exception("Only dictionaries can be parsed as DIP parameters. Following datatype was received:", type(data))
    lines = _dump_node(data, [], None)
    return Sign.NEWLINE.join(lines)