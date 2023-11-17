from setuptools import setup

setup(
    name='alecto',
    version='2.1.4',
    py_modules=['alecto'],
    install_requires=[
        'passlib',
        'uuid',
        'bcrypt',
        'argon2',
        'argon2-cffi',
        'numpy',
        'spookyhash',
        'xxhash'
    ],
    entry_points={
        'console_scripts': [
            'alecto = alecto:main',
        ],
    },
    description='Alecto is an advanced command-line tool for password hashing. With support for various hashing algorithms, including MD5, SHA-256, SHA-512, Argon2, and bcrypt, it offers flexibility and security. Users can choose algorithms, include custom salts, and specify hash lengths, making it a versatile solution for password hashing needs.',
    long_description=open('README.md').read(),  # Provide README for PyPI
    long_description_content_type='text/markdown',
    author='Saphiraaa',
    author_email='fredmarkivand@gmail.com',
    url='https://github.com/saphiraaa/NetherMath',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Add more classifiers as needed
    ],
)
