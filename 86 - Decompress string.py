'''Please write a program to compress and decompress the string "hello 
world!hello world!hello world!hello world!" '''
#Code
import zlib

# The original string
original_string = "hello world!hello world!hello world!hello world!"

# Compress the string
compressed_data = zlib.compress(original_string.encode())

# Decompress the compressed data
decompressed_data = zlib.decompress(compressed_data).decode()

# Print the results
print("Original String:", original_string)
print("Compressed Data:", compressed_data)
print("Decompressed Data:", decompressed_data)
