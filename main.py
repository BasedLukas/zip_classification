

from zip_implementation import Zip




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

