# Alecto: Advanced Password Hashing Tool

Alecto is an advanced command-line utility designed for sophisticated password hashing, offering a comprehensive set of features and algorithms to bolster security. Below, you'll find an in-depth guide on Alecto's features, advanced usage, supported algorithms, and practical examples.

## Features

### 1. **Extensive Algorithm Support**

Alecto boasts support for a diverse array of hashing algorithms, providing users with the flexibility to tailor their security measures to specific requirements. Here is a list of available algorithms:

- apr_md5_crypt
- argon2
- bcrypt
- bcrypt_sha256
- bigcrypt
- blake2b
- blake2s
- bsd_nthash
- bsdi_crypt
- cisco_type7
- crypt16
- cta_pbkdf2_sha1
- des_crypt
- django_pbkdf2_sha1
- django_pbkdf2_sha256
- django_salted_sha1
- dlitz_pbkdf2_sha1
- fshp
- grub_pbkdf2_sha512
- lmhash
- md4
- md5
- md5-sha1
- md5_crypt
- mssql2000
- mssql2005
- mysql323
- mysql41
- nthash
- oracle11
- pbkdf2_hmac_sha1
- pbkdf2_hmac_sha256
- pbkdf2_hmac_sha512
- pbkdf2_sha256
- phpass
- ripemd160
- scram
- scrypt
- sha128
- sha1_crypt
- sha224
- sha256
- sha256_crypt
- sha384
- sha3_224
- sha3_256
- sha3_384
- sha3_512
- sha512
- sha512_crypt
- shake_128
- shake_256
- sm3
- spookyhash
- sun_md5_crypt
- whirlpool
- xxhash

### 2. **Algorithm Specification**

Directly specify the hashing algorithm:

```bash
python alecto.py -a <algorithm> <password>
```

### 3. **Custom Salt Integration**

Elevate password security by introducing custom salts into the hashing process. Alecto seamlessly accommodates custom salts, providing users with granular control over the salting mechanism, a crucial aspect of robust password storage.

### 4. **Terminal Clarity Enhancement**

Alecto includes a terminal-clearing functionality, optimizing user experience by ensuring a clean and organized interface.

### 5. **Fine-tuned Hash Length Specification**

Specific to shake_128 and shake_256 algorithms, Alecto enables users to precisely specify the hash length using the `--hash-length` option. This advanced feature allows for tailoring hash outputs to exact requirements.

## Advanced Usage

### 1. **Parallel Salting**

For enhanced security, leverage both custom and default salts simultaneously:

```bash
python alecto.py <password> -a <algorithm> --salt --both-salt
```

### 2. **Custom Salt Usage**

Utilize a custom salt in the hashing process:

```bash
python alecto.py <password> -a <algorithm> --salt --custom-salt
```

### 3. **Custom Byte Length For SHAKE128 AND SHAKE256**

'''bash
python alecto.py <password> -a <shake128 or shake256> --hash-length <length>
'''
## Examples

### 1. **Custom Algorithm and Salt**

```bash
python alecto.py -a sha3_256 --custom-salt mypassword
```

### 2. **Parallel Salting with Shake_256**

```bash
python alecto.py -- salt --both-salt -a shake_256 --hash-length 64 mypassword
```
## Considerations

- When using a custom salt, it is seamlessly integrated into the hashing process.
- For algorithms like argon2 and bcrypt, employing a custom salt enhances overall security.
- Default salts are automatically generated when using the `--salt` or `--both-salt` options.

**Disclaimer:** Alecto is intended for educational and security research purposes. Users are advised to employ the tool responsibly and adhere to ethical guidelines.
