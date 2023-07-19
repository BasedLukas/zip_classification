class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


class Huffman:
    def __init__(self, freq_dict=None):
        self.freq_dict = freq_dict or {}
        self.huffman_tree = None
        self.huffman_codes = None

    def build_frequency_dict(self, data):
        for c in data:
            if c in self.freq_dict:
                self.freq_dict[c] += 1
            else:
                self.freq_dict[c] = 1

    def build_huffman_tree(self):
        nodes = [Node(char, freq) for char, freq in self.freq_dict.items()]
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            left = nodes.pop(0)
            right = nodes.pop(0)
            freq_sum = left.freq + right.freq
            internal_node = Node(None, freq_sum, left, right)
            nodes.append(internal_node)
        self.huffman_tree = nodes[0]

    def generate_huffman_codes(self, node=None, code=''):
        node = node or self.huffman_tree
        if node.is_leaf():
            self.huffman_codes[node.char] = code
        else:
            self.generate_huffman_codes(node.left, code + '0')
            self.generate_huffman_codes(node.right, code + '1')

    def encode(self, data):
        self.build_frequency_dict(data)
        self.build_huffman_tree()
        self.huffman_codes = {}
        self.generate_huffman_codes()
        huffman_data = [self.huffman_codes[c] for c in data]
        return ''.join(huffman_data)

    def decode(self, huffman_data):
        decoded = []
        node = self.huffman_tree
        for bit in huffman_data:
            if bit == '0':
                node = node.left
            else:
                node = node.right
            if node.is_leaf():
                decoded.append(node.char)
                node = self.huffman_tree
        return decoded