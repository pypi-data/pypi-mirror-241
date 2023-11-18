
import json
import datetime
from kraken_thing.kraken_class_observation.helpers import value_conversion as vc

def get_summary_record(record):
    """Returns a summary record formatted
    """
    
    id = record.get('id', None)
    id_str = f'{id[:10]:10s}' if id else f'{"":10}'
        
    k = record.get('measuredProperty', None)
    k_str = f'{k[:20]:.20}' if k else f'{"":.20}'

    v = record.get('value', None)
    v = vc.value_conversion_to_string(v)
    v_str = f'{v[:30]:30}' if v else f'{"":.30}' 

    le = str(len(v))
    le_str = f'{str(le)[:5]:5}' if le else f'{"":.5}' 
    
    c = record.get('credibility', None)
    c_str = f'{c:.2f}' if c else f'{0.00:.2f}'

    d = record.get('observationDate', None)
    d_str = f'{d:%Y-%m-%d, %H:%M:%S}' if d else f'{"":.20}'

    l = record.get('language', None)
    l_str = f'{str(l)[:5]:5}' if l else f'{"":.5}' 

    vv = record.get('validValue', None)
    vv_str = f'{str(vv)[:5]:5}' if vv else f'{"":.5}' 

    source = record.get('source', {})
    s_type = source.get('@type', None)
    s_id = source.get('@id', None)
    s = str(s_type) + '/' + str(s_id)
    s_str = f'{str(s)[:20]:20}' if s else f'{"":.20}' 
    
    record = {
        'type/id': id_str,
        'measuredProperty': k_str,
        'value': v_str,
        'length': le_str,
        'valid': vv_str, 
        'lang': l_str,
        'c': c_str,
        'd': d_str,
        'source': s_str
    }
    return record

def get_summary_string(record):
    """Returns the summary_record as a string
    """
    
    summary_record = get_summary_record(record)
    
    content = ''
    content += 'Observation\n'
    content += '===========\n'
    for k, v in summary_record.items():
        content += ' - ' + k + ': ' + v + '\n'
    content += '\n'
    return content


