#!/usr/bin/env python3
import sys
import hashlib
import os
from collections import OrderedDict as od

def get_hashsums(file_path):
    hash_sums = od()
    hash_sums['md5sum'] = hashlib.md5()
    hash_sums['sha1sum'] = hashlib.sha1()
    hash_sums['sha224sum'] = hashlib.sha224()
    hash_sums['sha256sum'] = hashlib.sha256()
    hash_sums['sha384sum'] = hashlib.sha384()
    hash_sums['sha512sum'] = hashlib.sha512()

    with open(file_path, 'rb') as fd:
        data_chunk = fd.read(1024)
        while data_chunk:
              for hashsum in hash_sums.keys():
                  hash_sums[hashsum].update(data_chunk)
              data_chunk = fd.read(1024)

    results = od()
    for key,value in hash_sums.items():
         results[key] = value.hexdigest()         
    return results



def main():
    for path in sys.argv[1:]:
        print(">>> ",path)
        for key,value in get_hashsums(path).items():
            print(key,value)

if __name__ == '__main__': main()