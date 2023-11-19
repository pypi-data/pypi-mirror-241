from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = 'Hill Cipher (Encryption and Decryption)'

setup(
    name="hillcipher",
    version=VERSION,
    author="NooB c0deR (Kiran Deep)",
    author_email="kirandeep102030@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md", "rt").read(),
    packages=find_packages(),
    install_requires=['numpy', 'mathmatrix'],
    keywords=['python', 'cryptography', 'hill', 'hillcipher', 'encryption', 'decryption', 'symmetric encryption'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Security :: Cryptography",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
