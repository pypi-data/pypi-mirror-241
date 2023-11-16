import setuptools
with open("README.md", "r", encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="afanlife",
    version="1.0",
    author="AFAN",
    author_email="bili_afan@163.com",
    description="AFAN尝试的Python工具包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(where='.'
                                      ,exclude=()
                                      ,include=('*')
                                      ),
    license='CC0',
    install_requires=[
        'scikit-learn==0.23.1'
        ,'numpy==1.23.2'
        ,'pandas==11.2.9'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)