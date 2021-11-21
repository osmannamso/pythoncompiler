from flask import Flask, request

from compiler import compile_result, AppTypes
from models import TreeNode, LinkedList

app = Flask(__name__)


@app.route('/compile', methods=['POST'])
def route_compile():
    try:
        data = request.get_json(force=True)
        return compile_result(data['code'], data['type'], data['params'])
    except Exception as e:
        return 'Server Error', 500


@app.route('/check-decompile', methods=['POST'])
def route_decompile():
    try:
        data = request.get_json(force=True)
        if AppTypes[data['type']] == AppTypes['tree']:
            return TreeNode.compile(TreeNode.decompile(data['param']))
        elif AppTypes[data['type']] == AppTypes['linkedList']:
            return LinkedList.compile(LinkedList.decompile(data['param']))
        else:
            return 'Not supported', 500
    except Exception as e:
        return 'Server Error', 500


if __name__ == '__main__':
    print('App running')
    app.run()
