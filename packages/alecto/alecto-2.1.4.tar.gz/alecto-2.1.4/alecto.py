import argparse
import hashlib
import os
import uuid
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import base64
from passlib.hash import mysql323, mysql41, mssql2000, mssql2005, oracle11, pbkdf2_sha256, des_crypt, bsdi_crypt, bigcrypt, crypt16, md5_crypt, sha1_crypt, sha256_crypt, sha512_crypt, sun_md5_crypt, apr_md5_crypt, phpass, cta_pbkdf2_sha1, dlitz_pbkdf2_sha1, django_pbkdf2_sha1, django_pbkdf2_sha256, grub_pbkdf2_sha512, scram, bsd_nthash, lmhash, nthash, cisco_type7, fshp, bcrypt, argon2, scrypt, pbkdf2_sha1, pbkdf2_sha256, pbkdf2_sha512, bcrypt_sha256, django_bcrypt, django_salted_sha1
import spookyhash
import xxhash
import math

tool = r"""
    ___    __          __
   /   |  / /__  _____/ /_____
  / /| | / / _ \/ ___/ __/ __ \
 / ___ |/ /  __/ /__/ /_/ /_/ /
/_/  |_/_/\___/\___/\__/\____/
          Saphiraaaa

"""

parser = argparse.ArgumentParser(description="Alecto: Advanced Hash Generator")

def clear_terminal():
    """Clear the terminal."""
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception as e:
        print("An error occurred:", e)

def hash_text(text, algorithm, salt=None, custom_salt=None):
    args = parser.parse_args()
    hash_object = None

    if algorithm == 'md5':
        hash_object = hashlib.md5()
    elif algorithm in ['sha1', 'sha256', 'sha512', 'sha224', 'sha384', 'blake2s', 'blake2b', 'md4', 'whirlpool', 'md5-sha1', 'sha128', 'sm3', 'ripemd160', 'shake_128', 'shake_256']:
        hash_object = hashlib.new(algorithm)
    elif algorithm == 'argon2':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        argon2_hash = argon2.hash(text)
        return argon2_hash
    elif algorithm == 'bcrypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        bcrypt_hash = bcrypt.hash(text)
        return bcrypt_hash
    elif algorithm in ['sha3_256', 'sha3_224', 'sha3_384', 'sha3_512']:
        hash_object = hashlib.new(algorithm)
    elif algorithm == 'scrypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        scrypt_hash = scrypt.hash(text)
        return scrypt_hash
    elif algorithm == 'mysql323':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        mysql323_hash = mysql323.hash(text)
        return mysql323_hash
    elif algorithm == 'mysql41':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        mysql41_hash = mysql41.hash(text)
        return mysql41_hash
    elif algorithm == 'mssql2000':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        mssql2000_hash = mssql2000.hash(text)
        return mssql2000_hash
    elif algorithm == 'mssql2005':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        mssql2005_hash = mssql2005.hash(text)
        return mssql2005_hash
    elif algorithm == 'oracle11':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        oracle11_hash = oracle11.hash(text)
        return oracle11_hash
    elif algorithm == 'lmhash':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        lm_hash = lmhash.hash(text)
        return lm_hash
    elif algorithm == 'nthash':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        nt_hash = nthash.hash(text)
        return nt_hash
    elif algorithm == 'pbkdf2_sha256':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        pbkdf2sha256 = pbkdf2_sha256.hash(text)
        return pbkdf2sha256
    elif algorithm == 'des_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        descrypt = des_crypt.hash(text)
        return descrypt
    elif algorithm == 'bsdi_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        bsdicrypt = bsdi_crypt.hash(text)
        return bsdicrypt
    elif algorithm == 'bigcrypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        big_crypt = bigcrypt.hash(text)
        return big_crypt
    elif algorithm == 'crypt16':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        crypt_16 = crypt16.hash(text)
        return crypt_16
    elif algorithm == 'md5_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        md5crypt = md5_crypt.hash(text)
        return md5crypt
    elif algorithm == 'sha1_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        sha1crypt = sha1_crypt.hash(text)
        return sha1crypt
    elif algorithm == 'sha256_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        sha256crypt = sha256_crypt.hash(text)
        return sha256crypt
    elif algorithm == 'sha512_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        sha512crypt = sha512_crypt.hash(text)
        return sha512crypt
    elif algorithm == 'sun_md5_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        sunmd5crypt = sun_md5_crypt.hash(text)
        return sunmd5crypt
    elif algorithm == 'apr_md5_crypt':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        aprmd5crypt = apr_md5_crypt.hash(text)
        return aprmd5crypt
    elif algorithm == 'phpass':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        ph_pass = phpass.hash(text)
        return ph_pass
    elif algorithm == 'cta_pbkdf2_sha1':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        ctapbkdf2sha1 = cta_pbkdf2_sha1.hash(text)
        return ctapbkdf2sha1
    elif algorithm == 'dlitz_pbkdf2_sha1':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        dlitzpbkdf2sha1 = dlitz_pbkdf2_sha1.hash(text)
        return dlitzpbkdf2sha1
    elif algorithm == 'django_pbkdf2_sha1':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        djangopbkdf2sha1 = django_pbkdf2_sha1.hash(text)
        return djangopbkdf2sha1
    elif algorithm == 'django_pbkdf2_sha256':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        djangopbkdf2sha256 = django_pbkdf2_sha256.hash(text)
        return djangopbkdf2sha256
    elif algorithm == 'grub_pbkdf2_sha512':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        grubpbkdf2sha512 = grub_pbkdf2_sha512.hash(text)
        return grubpbkdf2sha512
    elif algorithm == 'scram':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        scram_hash = scram.hash(text)
        return scram_hash
    elif algorithm == 'bsd_nthash':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        bsdnthash = bsd_nthash.hash(text)
        return bsdnthash
    elif algorithm == 'cisco_type7':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        ciscotype7 = cisco_type7.hash(text)
        return ciscotype7
    elif algorithm == 'fshp':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        fshp_hash = fshp.hash(text)
        return fshp_hash
    elif algorithm == 'pbkdf2_hmac_sha1':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        pbkdf2_hmac_sha1 = pbkdf2_sha1.hash(text)
        return pbkdf2_hmac_sha1
    elif algorithm == 'pbkdf2_hmac_sha256':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        pbkdf2_hmac_sha256 = pbkdf2_sha256.hash(text)
        return pbkdf2_hmac_sha256
    elif algorithm == 'pbkdf2_hmac_sha512':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        pbkdf2_hmac_sha512 = pbkdf2_sha512.hash(text)
        return pbkdf2_hmac_sha512
    elif algorithm == 'spookyhash':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        spooky_hash = spookyhash.hash32(text.encode('utf-8'))
        return spooky_hash
    elif algorithm == 'xxhash':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        xx_hash = xxhash.xxh32(text.encode('utf-8')).hexdigest()
        return xx_hash
    elif algorithm == 'bcrypt_sha256':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        bcrypt_sha256_hash = bcrypt_sha256.hash(text)
        return bcrypt_sha256_hash
    elif algorithm == 'django_salted_sha1':
        if custom_salt:
            text = custom_salt + text
        elif salt:
            text = salt + text
        django_salted_sha1_hash = django_salted_sha1.hash(text)
        return django_salted_sha1_hash
    else:
        raise ValueError("Unsupported algorithm the hash might be invalid or not available on your system")

    if salt:
        text = salt + text
    if custom_salt:
        text = custom_salt + text

    hash_object.update(text.encode('utf-8'))
    if algorithm in ['shake_128', 'shake_256']:
        hash_length = args.hash_length
        return hash_object.hexdigest(hash_length) 
    else:
        return hash_object.hexdigest()

def custom_salt():
    return input("Enter your desired custom salt: ")

def get_algorithm_choice():
    algorithms = [
        'md5', 'sha256', 'sha512', 'sha224', 'sha384', 'blake2s', 'blake2b',
        'argon2', 'bcrypt', 'sha3_256', 'sha3_224', 'sha3_384', 'sha3_512',
        'scrypt', 'mysql323', 'mysql41', 'mssql2000', 'mssql2005', 'oracle11',
        'lmhash', 'nthash', 'pbkdf2_sha256', 'des_crypt',
        'bsdi_crypt', 'bigcrypt', 'crypt16', 'md5_crypt', 'sha1_crypt', 'sha256_crypt',
        'sha512_crypt', 'sun_md5_crypt', 'apr_md5_crypt', 'phpass', 'cta_pbkdf2_sha1',
        'dlitz_pbkdf2_sha1', 'django_pbkdf2_sha1', 'django_pbkdf2_sha256', 'grub_pbkdf2_sha512',
        'scram', 'bsd_nthash', 'cisco_type7', 'fshp', 'pbkdf2_hmac_sha1', 'pbkdf2_hmac_sha256',
        'pbkdf2_hmac_sha512', 'md4', 'whirlpool', 'sm3', 'ripemd160', 'md5-sha1', 'sha128', 'shake_128', 'shake_256', 
        'spookyhash', 'xxhash', 'bcrypt_sha256', 'django_salted_sha1',
    ]
    return algorithms

def main():
    parser.add_argument("password", nargs="?", help="Enter your password")
    parser.add_argument("--salt", action="store_true", help="Include a salt")
    parser.add_argument("-c", "--custom-salt", action="store_true", help="Use custom salt")
    parser.add_argument("-d", "--default-salt", action="store_true", help="Use default salt")
    parser.add_argument("-a", "--algorithm", help="Select the hashing algorithm")
    parser.add_argument("-b", "--both-salt", action="store_true", help="Use both custom and default salt")
    parser.add_argument("--hash-length", type=int, help="Specify the length of the hash in bytes(Only for shake 128 and shake 256)")
    parser.add_argument("--list-algorithms", action="store_true", help="List all the available hashes in Alecto")
    args = parser.parse_args()

    plaintext = args.password

    try:
        algorithm = args.algorithm or get_algorithm_choice()

        if args.hash_length and algorithm not in ['shake_128', 'shake_256']:
            raise ValueError("--hash-length is only available for shake_128 and shake_256 algorithms")

        if args.list_algorithms:
            clear_terminal()
            print(tool)
            print("[+] Available Hashing Algorithms:")
            for algorithm in sorted(get_algorithm_choice()):
                print(f" - {algorithm.lower()}")
            return
            
        elif args.salt:
            if args.both_salt:
                custom = custom_salt()
                clear_terminal()
                print(tool)
                uuid_salt = str(uuid.uuid4())
                random_salt = os.urandom(25).hex()
                all_salt = uuid_salt + custom + random_salt
                salt = all_salt 
                hashed_text = hash_text(plaintext, algorithm, salt)
                print(f"[+]Custom Salt: {custom}")
                print(f"[+]Salt: {salt}")
                print(f"[+]{algorithm.upper()}: {hashed_text}")
            elif args.custom_salt:
                custom = custom_salt()
                clear_terminal()
                print(tool)
                hashed_text = hash_text(plaintext, algorithm, custom)
                print(f"[+]Salt: {custom}")
                print(f"[+]{algorithm.upper()}: {hashed_text}")
            elif args.default_salt:
                clear_terminal()
                print(tool)
                uuid_salt = str(uuid.uuid4())
                random_salt = os.urandom(16).hex()
                salt = uuid_salt + random_salt
                hashed_text = hash_text(plaintext, algorithm, salt)
                print(f"[+]Salt: {salt}")
                print(f"[+]{algorithm.upper()}: {hashed_text}")
        else:
            clear_terminal()
            print(tool)
            hashed_text = hash_text(plaintext, algorithm)
            print(f"[+]{algorithm.upper()}: {hashed_text}")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

