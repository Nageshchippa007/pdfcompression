import argparse
import subprocess
import os.path
import sys
from shutil import copyfile

out_path = r'output_files'
in_path = r'input_files/'

def compress(input_file_path, output_file_path, power=0):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    # Basic controls
    # Check if valid path
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file")
        sys.exit(1)

    # Check if file is a PDF by extension
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print("Error: input file is not a PDF")
        sys.exit(1)

    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call(['C:/Program Files/gs/gs9.07/bin/gswin64c.exe', "-q", '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(quality[power]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                     input_file_path], shell=True
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.1f}MB".format(final_size / 1000000))
    print("Done.")

#files = [in_path + f for f in os.listdir(in_path) if os.path.isfile(f) and f.endswith('.pdf')]
files = [fn for fn in os.listdir(in_path) if fn.endswith('.pdf')]

for i in iter(files):
    completeName = os.path.join(out_path, i)
    compress(in_path + i, completeName, 4)