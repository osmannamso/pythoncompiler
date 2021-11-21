import json

from models import TreeNode, LinkedList, ArrayType
from values import TypeMissmatchError, TypeIsntSupported

AppTypes = {
    'str': 'str',
    'int': 'int',
    'tree': 'TreeNode',
    'array': 'list',
    'linkedList': 'LinkedList'
}


class Solution:
    def solution(self):
        pass


def decompiled_params(params):
    res = []
    for p in params:
        if AppTypes[p['type']] == AppTypes['tree']:
            res.append(TreeNode.decompile(p.value))
        elif AppTypes[p['type']] == AppTypes['linkedList']:
            res.append(LinkedList.decompile(p.value))
        elif AppTypes[p['type']] == AppTypes['int']:
            res.append(int(p['value']))
        elif AppTypes[p['type']] == AppTypes['str']:
            res.append(p.value)
        elif AppTypes[p['type']] == AppTypes['array']:
            res.append(json.loads(p['value']))
        else:
            raise TypeIsntSupported
    return res


def compile_result(code, data_type, params):
    exec(code)
    compiled = {
        'value': None
    }
    d_params = decompiled_params(params)
    s = Solution()
    res = s.solution(*d_params)
    if AppTypes[data_type] != res.__class__.__name__:
        raise TypeMissmatchError()
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
