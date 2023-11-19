from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name='afip_invoice_extract_qr_cae_and_decode',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'Pillow==10.1.0',
        'PyJWT==2.8.0',
        'PyMuPDF==1.23.6',
        'PyMuPDFb==1.23.6',
        'pyzbar==0.1.9'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)