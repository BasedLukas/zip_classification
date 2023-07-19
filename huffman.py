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
        return nodes[0]

    def generate_huffman_codes(self, node=None, code=''):
        if node is None:
            return {}
        if node.is_leaf():
            return {node.char: code}
        huffman_codes = {}
        huffman_codes.update(self.generate_huffman_codes(node.left, code + '0'))
        huffman_codes.update(self.generate_huffman_codes(node.right, code + '1'))
        return huffman_codes

    def encode(self, data):
        self.build_frequency_dict(data)
        huffman_tree = self.build_huffman_tree()
        huffman_codes = self.generate_huffman_codes(huffman_tree)
        huffman_data = [huffman_codes[c] for c in data]
        encoded = ''.join(huffman_data)
        return encoded, huffman_codes

    @staticmethod
    def decode(encoded_data, huffman_codes):
        decoded = []
        huffman_data = ""
        reverse_huffman_codes = {v: k for k, v in huffman_codes.items()}
        for bit in encoded_data:
            huffman_data += bit
            if huffman_data in reverse_huffman_codes:
                # Append the tuple to decoded
                decoded.append(reverse_huffman_codes[huffman_data])
                huffman_data = ""
        return decoded



