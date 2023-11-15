from setuptools import setup, find_packages

setup(
    name='payos-lib-python',
    version='0.1.0',
    author='Casso',
    author_email='tranglq@casso.vn',
    description='A library for create Payment Link of PayOS and more',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)