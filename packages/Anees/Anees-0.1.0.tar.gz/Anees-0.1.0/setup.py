from setuptools import setup, find_packages

setup(
    name='Anees',
    version='0.1.0',
    author='Anees afridi',
    author_email='aneesafridi50@gmail.com',
    description='Description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # url='https://github.com/your_username/your_package_name',
    packages=find_packages(),
    install_requires=[
        # list dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        # Add more classifiers as needed
    ],
)
