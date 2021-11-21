import json
from typing import List

from values import Errors


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def compile(tree_node):
        if not tree_node:
            return '()'
        res = str(tree_node.val)
        if tree_node.left or tree_node.right:
            res += TreeNode.compile(tree_node.left)
            res += TreeNode.compile(tree_node.right)
        return f'({res})'

    @staticmethod
    def decompile(text):
        value = ''
        found_brackets = 0
        i = 0
        while found_brackets < 2:
            if text[i] == '(' or text[i] == ')':
                found_brackets += 1
            else:
                value += text[i]
            i += 1
        left_text = ''
        right_text = None
        if text[i - 1] != ')':
            left_text = '('
            count = 1
            while count > 0 and text[i]:
                left_text += text[i]
                if text[i] == '(':
                    count += 1
                elif text[i] == ')':
                    count -= 1
                i += 1
            if text[i] == '(':
                right_text = text[i:len(text) - 1]
        res = TreeNode(int(value)) if len(value) else None
        if left_text:
            res.left = TreeNode.decompile(left_text)
            if right_text:
                res.right = TreeNode.decompile(right_text)
        return res


class LinkedList:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    @staticmethod
    def compile(node):
        if LinkedList.is_valid(node):
            current = node
            res = []
            while current:
                res.append(str(current.val))
                current = current.next
            return f'[{",".join(res)}]'
        else:
            raise Errors.InfinityError

    @staticmethod
    def decompile(arr):
        arr: List[int] = json.loads(arr)
        if not len(arr):
            return None
        arr.reverse()
        head = LinkedList(arr.pop())
        current = head
        while len(arr):
            current.next = LinkedList(arr.pop())
            current = current.next
        return head

    @staticmethod
    def is_valid(node) -> bool:
        uniques = set()
        current = node
        while current:
            current = current.next
            if current in uniques:
                return False
            uniques.add(current)
        return True


class ArrayType:
    @staticmethod
    def compile(arr):
        return f'{",".join(arr)}'
