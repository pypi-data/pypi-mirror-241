
import datetime
from dateutil.parser import parse
from math import log10, floor
from sigfig import round


def value_type_conversion(value):
    """From a value, convert to the corresponding type
    """

    
    # Case: Dict, int list -_ areturn as is
    if isinstance(value, (dict, int, list)):
        return value
    
    # Case float -> try to convert to int
    elif isinstance(value, float):
        try:
            value = int(value)
            return value
        except Exception as e:
            a=1
        return value

    # Case str -> try datetime, int, float
    elif isinstance(value, str): 
        """
        """
        
        # Clean-up string
        value = string_clean_up(value)
        

        # datetime
        if len(value) >= 6:
            try:
                new_value = parse(value)
                return new_value
            except:
                a=1

        # integer
        try:
            new_value = int(value)
            return new_value
        except:
            a=1

        # float
        try:
            new_value = float(value)
            return new_value
        except:
            a=1    

        
    return value


def string_clean_up(value):
    """
    """
    if not value or not isinstance(value, str):
        return None
        
    value = value.strip()
    return value


def value_conversion_to_string(value):
    """
    """
    content = ''

    if isinstance(value, datetime.datetime):
        content = f'{value:%Y-%m-%d, %H:%M:%S)}'
    elif isinstance(value, dict):
        content = f"{value.get('@type', '')}/{value.get('@id', '')}"
    elif isinstance(value, (int, float)):
        
        
        content = str(value)
    elif isinstance(value, str):
        content = str(value)
    else:
        try:
            content = value.type + '/' + value.id
        except Exception as e:
            print(e)
            a=1
    return str(content)


def value_conversion_to_float(value):
    """
    """
    if not value:
        return None
    try:
        return float(value)
    except Exception as e:
        return None


def value_conversion_to_datetime(value):
    
    if isinstance(value, datetime.datetime):
        return value
        
    try:
        new_value = parse(value)
        return new_value
    except:
        return None
        
