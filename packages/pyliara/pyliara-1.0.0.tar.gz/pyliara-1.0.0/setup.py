from setuptools import setup, find_packages

requirements = ['requests']

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name = 'pyliara',
    version = '1.0.0',
    author='MohammadRezaFirouzi',
    author_email = 'mrfirouziii@gmail.com',
    description = 'This is an unofficial library for Liara Host',
    long_description = readme,
    python_requires="~=3.7",
    long_description_content_type = 'text/markdown',
    url = 'https://rubika.ir/Mohamadreza_firouzi',
    packages = find_packages(),
    install_requires = requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
