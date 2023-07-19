

from zip_implementation import Zip
from lz77 import LZ77Compressor



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

z = Zip(return_type='binary') #You can also return a string of 1 and 0 but then the length doesn't make sense anymore
lz = LZ77Compressor()


# compressed is a tuple of (compressed data, huffman codes, original length)
compressed = z.compress(data)
compressed_lz77 = lz.compress(data)


del z # Show that nothing is being stored in the object
z = Zip(return_type='binary')


decompressed = z.decompress(compressed)

#convert huffman codes to easily readable format
h_codes = {}
for k,v in compressed[1].items():
    if k[0] == 0:
        h_codes[k[2]] = v
    else:
        h_codes[str(k[:2])] = v


# convert lz77 codes to easily readable format
to_print = []
for item in compressed_lz77:
    if item[0] == 0:
        to_print.append(item[2])
    else:
        to_print.append(str(item[:2]))
        to_print.append(item[2])
to_print = ''.join(to_print)



print('Length of compressed data:',len(compressed[0])+ len(compressed[1]))  
print("Length of initial string:",len(data))  
if (decompressed == data):
    print("Compression worked with zero loss") 
else:
    print("Compression failed") 

print()
print(f"Encoded string: \n{''.join(format(byte, '08b') for byte in compressed[0])}")
print()
print(f"Huffman codes: \n{h_codes}")
print()
print(f"LZ77 Encoded string: \n{to_print}")