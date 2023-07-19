
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
        self.original_length = len(compressed)
        if self.return_type == 'string':
            return compressed, codes
        elif self.return_type == 'binary':
            return self.to_binary(compressed), codes, self.original_length
        

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


data = """

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching, but you're too shy to say it (say it)

"""

z = Zip(return_type='binary')
compressed = z.compress(data)

del z # Show that nothing is being stored in the object
z = Zip(return_type='binary')


decompressed = z.decompress(compressed)

print('Length of compressed data:',len(compressed[0])+ len(compressed[1]))  # This prints the length of the bytearray in bytes
print("Length of initial string:",len(data))  
if (decompressed == data):
    print("Compression worked with zero loss")  

print()
print(f"Encoded string: \n{compressed[0]}")
print()
print(f"Huffman codes: \n{compressed[1]}")