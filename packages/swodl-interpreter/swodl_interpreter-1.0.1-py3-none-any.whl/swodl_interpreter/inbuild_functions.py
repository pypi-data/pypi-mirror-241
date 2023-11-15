import re
import copy
import json
import math
import functools
import pkg_resources
import random as rand

from lxml import etree
from xml.etree import ElementTree as ET
from swodl_interpreter.asts.struct import ArrayType, ThrowException


def array_set(a, i, value):
    new = copy.deepcopy(a)
    new[i] = value
    return new


def array_add(a, value):
    new = copy.deepcopy(a)
    i = max(a.values.keys()) + 1 if len(a) > 0 else 0
    new[i] = value
    return new


def assert_method(condition, msg):
    if not condition:
        raise ThrowException(msg)


def compare(a, b, case_sensitive=False):
    if case_sensitive:
        a = a.lower()
        b = b.lower()
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1


xml_char = {'&': '&amp;', '"': '&quot;',
            "'": '&apos;', '<': '&lt;', '>': '&gt;'}


def xmlencode(s: str):
    for k, v in xml_char.items():
        s = s.replace(k, v)
    return s


def xmldecode(s: str):
    for k, v in xml_char.items():
        s = s.replace(v, k)
    return s


def xml_elements(s, e='*', xpath='./'):
    s = re.sub(r'<\?xml(.*)\?>', '', s)
    try:
        root = etree.fromstring(s)
    except:
        return ''
    elements = etree.ETXPath(f'{xpath}{e}')(root)
    if len(elements) == 0:
        return ''
    for element in elements:
        etree.indent(element, space='  ')
    return [etree.tostring(root, encoding='unicode').strip() for root in elements]


def xml_select_multi(s, xpath, *namespace):
    if s == '':
        return ''
    namespaces = {k: v for k, v in [x.split('=') for x in namespace]}
    s = re.sub(r'<\?xml(.*)\?>', '', s)
    elements = etree.fromstring(s).xpath(xpath, namespaces=namespaces)
    if len(elements) == 0:
        return ''
    for element in elements:
        etree.indent(element, space='  ')
    return ArrayType(
        [
            etree.tostring(root, encoding='unicode').strip()
            for i, root in enumerate(elements)
        ]
    )


def xml_ns(s):
    ET.register_namespace('', s)
    return f'{{{s}}}'


def xml_new_element(name, *elems):
    root = ET.Element(name)
    if len(elems) == 1 and type(elems[0]) == str:
        root.text = xmldecode(elems[0])
    else:
        for elem in elems:
            if type(elem) == str and elem.startswith('<__wfe_xml_attribute__'):
                elem = elem.replace(
                    '<__wfe_xml_attribute__ ', '').replace(' />', '')
                elem = elem.split('=')
                root.attrib[elem[0]] = elem[1][1:-1]
            else:
                root.append(ET.fromstring(elem))
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='unicode')


def xml_add(root, elem):
    root = ET.fromstring(root)
    if type(elem) == str and elem.startswith('<__wfe_xml_attribute__'):
        elem = elem.replace('<__wfe_xml_attribute__ ', '').replace(' />', '')
        elem = elem.split('=')
        root.attrib[elem[0]] = elem[1][1:-1]
    else:
        try:
            root.append(ET.fromstring(elem))
        except:
            root.text = xmldecode(elem)
    ET.indent(root, space='  ')
    return ET.tostring(root, encoding='unicode')


def simplify(a):
    if isinstance(a, dict):
        return a['value']
    return a


def array_aggregate(sequence, op):
    def operation(a, b):
        return op(simplify(a), simplify(b))

    return functools.reduce(operation, sequence)


def swodl_to_json(item):
    def simplify(i):
        for k, vv in i.items():
            if type(vv) == list:
                i[k] = []
                for v in vv:
                    if (
                        type(v) == dict
                        and len(v) == 2
                        and 'index' in v
                        and 'value' in v
                    ):
                        v = v['value']
                        if type(v) == dict:
                            v = simplify(v)
                    i[k].append(v)
        return i

    return json.dumps(simplify(item))


def regex_replace(s, p, r, f=None):
    f = get_re_flag(f)
    if re.search(r'(\()\?(<)', p):
        p = re.sub(r'\(\?<', r'(?P<', p)
    if re.search(r'\$\{\w+\}', r):
        r = re.sub(r'\$\{(\w+)\}', r'\\g<\1>', r)
    if re.search(r'\$(\d+)', r):
        r = re.sub(r'\$(\d+)', r'\\\1', r)
    if f is not None:
        if re.search(r'\$(\d+)', r, f):
            r = re.sub(r'\$(\d+)', r'\\\1', r, f)
        return re.sub(p, r, s, f)
    return re.sub(p, r, s)


def regex_find(s, p, f=None):
    f = get_re_flag(f)
    if f == 'r':
        return (re.search(p, s).end() if re.search(p, s) else -1,)
    if f is not None:
        result = re.search(p, s, f)
    else:
        result = re.search(p, s)
    return result.start() if result else -1


def regex_ismatch(s, p, f=None):
    f = get_re_flag(f)
    if f is not None:
        r = re.search(p, s, f)
    else:
        r = re.search(p, s)
    return True if r else False


def get_re_flag(s):
    d = {'i': re.IGNORECASE, 'm': re.MULTILINE, 's': re.DOTALL}
    return d[s] if s in d else None


def getnumberofelements(text, spliter=',', skip=False):
    arr = [x for x in text.split(spliter)]
    if skip:
        arr = [x for x in arr if x]
    return len(arr)


def getelement(text, index, spliter=',', skip=False):
    arr = [x for x in text.split(spliter)]
    if skip:
        arr = [x for x in arr if x]
    return arr[index]


def substr(s, x, y=None):
    return s[x: x + y if y else None]


def find(s, p, i=0):
    return s.find(p, i)


def findreverse(s, p, i=0):
    return len(s[i + 1 if i else 0:]) - 1 - s[i + 1 if i else 0:][::-1].find(p)


def trim(s):
    return s.strip()


def replace(s, t, r):
    return s.replace(t, r)


def xml_text(s):
    if not s:
        return ''
    return ''.join(
        [
            xmldecode(x.strip())
            for x in etree.fromstring(re.sub(r'<\?xml(.*)\?>', '', s)).xpath('//text()')
        ]
    )


def xml_element(s, e):
    return (xml_elements(s, e) or [''])[0]


def xml_descendants(s, e='*'):
    return xml_elements(s, e, '//')


def xml_attribute(s, a):
    return etree.fromstring(re.sub(r'<\?xml(.*)\?>', '', s)).get(a) or ''


def xml_select(s, x, *n):
    return (xml_select_multi(s, x, *n) or [''])[0]


def xml_new_attribute(n, v):
    return f'<__wfe_xml_attribute__ {n}="{v}" />'


def array_create():
    return ArrayType()


def array_get(a, i):
    return a[i]


def array_size(a):
    if a == None: return 0
    return len(a)


def array_isset(a, i):
    return i in a.values


def array_bounds_lower(a):
    return min(a.values.keys())


def array_bounds_upper(a):
    return max(a.values.keys())


def array_all(a, op):
    return all([op(simplify(x)) for x in a])


def array_any(a, op):
    return any([op(simplify(x)) for x in a])


def array_select(a, op):
    return [op(simplify(x), simplify(x)) for x in a]


def array_where(a, op):
    return [x for x in a if op(simplify(x))]


def json_to_swodl(s):
    return json.loads(s)


def commonref_urn(st, si, t, i):
    return f'urn:com.avid:common-object:{st}:{si}:{t}:{i}'


def commonref_systemtype(s):
    return s.split(':')[3]


def commonref_systemid(s):
    return s.split(':')[4]


def commonref_type(s):
    return s.split(':')[5]


def commonref_id(s):
    return s.split(':')[6]


def random(i):
    return rand.randint(0, i)


def sqrt(x):
    return math.sqrt(x)


def ceil(x):
    return math.ceil(x)


def floor(x):
    return math.floor(x)


def nop():
    return 0

def str_lower(s):
    return s.lower()

def str_upper(s):
    return s.upper()

def config_get(profile, key):
    raise NotImplementedError()

def config_entry(profile, key, b):
    raise NotImplementedError()

def props(p):
    raise NotImplementedError()

functions = {
    'print': print,  # TODO: remove debug method
    'compare': compare,
    'substr': substr,
    'length': len,
    'find': find,
    'findreverse': findreverse,
    'trim': trim,
    'replace': replace,
    'xmlencode': xmlencode,
    'xmldecode': xmldecode,
    'xml_ns': xml_ns,
    'xml_text': xml_text,
    'xml_element': xml_element,
    'xml_elements': xml_elements,
    'xml_descendants': xml_descendants,
    'xml_attribute': xml_attribute,
    'xml_select': xml_select,
    'xml_select_multi': xml_select_multi,
    'xml_new_element': xml_new_element,
    'xml_new_attribute': xml_new_attribute,
    'xml_add': xml_add,
    'assert': assert_method,
    'array_create': array_create,
    'array_add': array_add,
    'array_set': array_set,
    'array_get': array_get,
    'array_size': array_size,
    'array_isset': array_isset,
    'array_bounds_lower': array_bounds_lower,
    'array_bounds_upper': array_bounds_upper,
    'array_aggregate': array_aggregate,
    'array_all': array_all,
    'array_any': array_any,
    'array_select': array_select,
    'array_where': array_where,
    'json_to_swodl': json_to_swodl,
    'swodl_to_json': swodl_to_json,
    'regex_ismatch': regex_ismatch,
    'regex_find': regex_find,
    'regex_replace': regex_replace,
    'commonref_urn': commonref_urn,
    'commonref_systemtype': commonref_systemtype,
    'commonref_systemid': commonref_systemid,
    'commonref_type': commonref_type,
    'commonref_id': commonref_id,
    'getnumberofelements': getnumberofelements,
    'getelement': getelement,
    'random': random,
    'sqrt': sqrt,
    'abs': abs,
    'floor': floor,
    'ceil': ceil,
    'pow': pow,
    'round': round,
    'nop': nop,
    'str_lower': str_lower,
    'str_upper': str_upper,
    'config_get': config_get,
    'config_entry': config_entry,
    'props': props
}
