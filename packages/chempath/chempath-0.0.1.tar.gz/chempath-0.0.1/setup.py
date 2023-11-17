from setuptools import setup, Extension, find_packages


_chempath = Extension(
    'chempath.core._chempath',
    sources = [
        'chempath/core/chempath.c',
        'chempath/core/src/dtypes.c',
    ],
    include_dirs = ['chempath/core/include'],
)


setup(
    name         = 'chempath',
    version      = '0.0.1',
    packages     = find_packages(),
    ext_modules  = [_chempath],
    description  = 'Chemical Database.',
    author       = 'Zhao Kunwang',
    author_email = 'clumsykundev@gmail.com',
    url          = 'https://github.com/clumsykun/chempath',
)
