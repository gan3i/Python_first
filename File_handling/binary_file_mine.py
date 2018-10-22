""" a module for dealing with BMP bitmap image files"""
from Factal_mine import Mandelbrot


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.

    Args:
        filename:The name of the BMP file to be crated .

    pixels:
        A rectangular image stored as sequence of rowa.
        eack row must be an iterable series of integers in the 
        range of 0-255

    Raises: 
        OSError : If the file couldn't be written.
    """
    height=len(pixels)
    width=len(pixels[0])

    with open(filename, mode="wb") as bmp:
        #BMP Header
        bmp.write(b'BM')

        size_bookmark=bmp.tell()        #the next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  #little-endian integer. Zero placeholder for now now

        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00') # Unused 16-bit integer - should be zero

        pixels_offset_bookmark=bmp.tell() # The next four bytes hold the integer offset to the  
        bmp.write(b'\x00\x00\x00\x00')  # pixel data , Zero placeholder for now.

        #Image header
        bmp.write(b'\x28\x00\x00\x00')  #the image header size in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width)) # image width in pixels
        bmp.write(_int32_to_bytes(height)) #image height in pixels
        bmp.write(b'\x01\x00')   #Number of image planes
        bmp.write(b'\x08\x00')  # Bits per pixel 8 for graysclae
        bmp.write(b'\x00\x00\x00\x00') # No Compression
        bmp.write(b'\x00\x00\x00\x00') # Zero for uncompressed image
        bmp.write(b'\x00\x00\x00\x00') # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00') # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00') # Use whole color table
        bmp.write(b'\x00\x00\x00\x00') # All colors are important

        #color pallete - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))# blue, green , Red , Zero

        pixel_data_bookmark=bmp.tell()
        for row in reversed(pixels): #BMP files are bottom to top
            row_data=bytes(row)
            bmp.write(row_data)
            padding=b'\x00' * ((4-(len(row) % 4)) % 4) # pad row to multiplpe of four bytes
            bmp.write(padding)
        
        #End of file
        eof_bookmark=bmp.tell()

        # fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes((eof_bookmark)))

        # Fill in pixel offset placeholder
        bmp.seek(pixels_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    """ convert an integer to four bytes in little-endian format"""
    return bytes((i & 0xff,
                 i >> 8 & 0xff,
                 i >> 16 & 0xff,
                 i >> 24 & 0xff))


if __name__=="__main__":
    pixels=Mandelbrot(1024,768)
    write_grayscale("mandel.bmp",pixels) 



