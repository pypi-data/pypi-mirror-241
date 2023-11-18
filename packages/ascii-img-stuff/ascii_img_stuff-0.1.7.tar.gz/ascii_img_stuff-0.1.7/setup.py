from setuptools import setup, find_packages

def long_desc():
    with open('readme.md', 'r') as f:
        return f.read()
    
setup(
    name='ascii_img_stuff',
    version='0.1.7',
    author='hashirkz',
    author_email='hashirxkhan1@gmail.com',
    description='python3 cli tool to render *.jpg *.jpeg *.png etc imgs as ascii .txt files',
    long_description=long_desc(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ascii_stuff',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX',
    ],
    entry_points={
        'console_scripts': [
            'ascii = ascii_img_stuff.app:main'
        ],
    },
    install_requires=[
        'numpy==1.23.5',
        'matplotlib==3.3.0',
        'scikit-image==0.19.3',
    ],
)
