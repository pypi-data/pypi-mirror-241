from setuptools import setup, find_packages

setup(
    name='cyprint',
    version='1.0.9',
    packages=find_packages(),
    description='Customized colorful logging in Python',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='xciny',
    author_email='229735037@qq.com',
    url='https://pypi.org/manage/project/cyprint',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'colorama',  # Add your dependencies here
    ],
)
