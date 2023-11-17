from setuptools import setup, find_packages

setup(
    name='dataxy',
    version='0.2',
    packages=find_packages(),
    py_modules=['dataxy'],
    install_requires=[
        'requests',
        'numpy',
        'pandas'
    ],
    author='yuanfang',
    author_email='2970760850@qq.com',
    description='Description of your package',
    url='https://github.com/yuanfangy/creat_xy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)




