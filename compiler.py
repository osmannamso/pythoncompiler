import json

from models import TreeNode, LinkedList, ArrayType
from values import Errors

AppTypes = {
    'str': 'str',
    'int': 'int',
    'tree': 'TreeNode',
    'array': 'List',
    'linkedList': 'LinkedList'
}


def solution(params):
    return []


def decompiled_params(params):
    res = []
    for p in params:
        if p.type == AppTypes['tree']:
            return TreeNode.decompile(p.value)
        elif p.type == AppTypes['linkedList']:
            return LinkedList.decompile(p.value)
        elif p.type == AppTypes['int']:
            return int(p.value)
        elif p.type == AppTypes['str']:
            return p.value
        elif p.type == AppTypes['array']:
            return json.loads(p.value)
        else:
            raise Errors.TypeIsntSupported
    return res


def compile_result(code, data_type, params):
    eval(code)
    compiled = {
        'value': None
    }
    res = solution(*decompiled_params(params))
    if AppTypes[data_type] != res.__class__.__name__:
        raise Errors.TypeMissmatchError
    if res.__class__.__name__ == AppTypes['tree']:
        compiled['value'] = TreeNode.compile(res)
    elif res.__class__.__name__ == AppTypes['array']:
        compiled['value'] = ArrayType.compile(res)
    elif res.__class__.__name__ == AppTypes['linkedList']:
        compiled['value'] = LinkedList.compile(res)
    elif res.__class__.__name__ == AppTypes['str']:
        compiled['value'] = res
    elif res.__class__.__name__ == AppTypes['int']:
        compiled['value'] = res
    return compiled
