
from huffman import Huffman
from lz77 import LZ77Compressor

class Zip:
    """return type can either be 'string' or 'binary'"""
    def __init__(self, window_size=50, lookahead_buffer_size=15,return_type='string'):
        self.lz = LZ77Compressor(window_size=window_size, lookahead_buffer_size=lookahead_buffer_size)
        self.huffman = Huffman()
        self.return_type = return_type

    def compress(self, data):
        compressed = self.lz.compress(data)
        compressed, codes = self.huffman.encode(compressed)
        
        # Store the length of the Huffman string before padding
        original_length = len(compressed)
        if self.return_type == 'string':
            return compressed, codes, original_length
        elif self.return_type == 'binary':
            return self.to_binary(compressed), codes, original_length
        

    def decompress(self, input):
        data, codes, original_length = input
        self.original_length = original_length
        if self.return_type == 'binary':
            data = self.from_binary(data)

        decompressed = self.huffman.decode(data, codes)
        decompressed = self.lz.decompress(decompressed)
        return decompressed

    def to_binary(self, huffman_data):
        # Pad the Huffman string to make its length a multiple of 8
        padded_data = huffman_data + (8 - len(huffman_data) % 8) * '0'
        binary_data = bytearray(int(padded_data[i:i+8], 2) for i in range(0, len(padded_data), 8))
        return binary_data

    def from_binary(self, binary_data):
        huffman_data = ''.join(f'{byte:08b}' for byte in binary_data)
        # Remove the padding added during the conversion to binary
        huffman_data = huffman_data[:self.original_length]
        return huffman_data

