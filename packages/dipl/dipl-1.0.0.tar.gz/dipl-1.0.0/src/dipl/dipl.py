from scinumtools.dip import DIP
from scinumtools.dip.settings import Format
#from scinumtools.dip.exports.config import ExportConfig

def load(text:str, dformat:Format = Format.TUPLE):
    """ Parse data from a DIP code
    """
    with DIP() as dip:
        dip.from_string(text)
        env = dip.parse()
        return env.data(dformat)
        
def dump(data):
    """ Dump Python data into a DIP code
    """
    text = 'Hello World'
    return text