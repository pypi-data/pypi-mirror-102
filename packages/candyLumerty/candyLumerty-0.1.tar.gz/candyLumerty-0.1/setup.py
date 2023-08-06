from distutils.core import setup

setup(
    name='candyLumerty',  
    packages=['candyLumerty'], 
    version='0.1',  
    license='MIT', 
    description='Test version',  
    author='Artem',  
    author_email='prototype22rus@mail.ru',  
    url='https://github.com/Corbie325/candyLumerty',  
    download_url='https://github.com/Corbie325/candyLumerty/archive/refs/tags/v_01.tar.gz',  
    keywords=['Candy' 'Lumerty'], 
    install_requires=[ 
        'logging',
		'functools',
		'requests',
		'json',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3',  
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
