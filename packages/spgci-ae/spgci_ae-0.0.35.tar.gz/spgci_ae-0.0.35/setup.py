from setuptools import setup
from Cython.Build import cythonize
from setuptools.command.build_py import build_py as _build_py
import os
import fnmatch
from distutils import sysconfig


EXCLUDE_FILES=[
]

def get_ext_paths(root_dir, exclude_files):
    paths=[]
    for root,dirs,files in os.walk(root_dir):
        for file_name in files:
            if os.path.splitext(file_name)[1] != '.py':
                continue
            file_path=os.path.join(root,file_name)
            if file_path in exclude_files:
                continue
            paths.append(file_path)
    return paths

class build_py(_build_py):

    def find_package_modules(self, package, package_dir):
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        ext_suffix = '.c'
        print('============================================================================')
        print(f'{ext_suffix}')
        modules = super().find_package_modules(package, package_dir)
        filtered_modules = []
        for (pkg, mod, filepath) in modules:
            print(filepath.replace('.py', ext_suffix))
            print(os.path.exists(filepath.replace('.py', ext_suffix)))
            if os.path.exists(filepath.replace('.py', ext_suffix)):
                continue
            filtered_modules.append((pkg, mod, filepath, ))
        return filtered_modules

readme = ''
with open('readme.md', mode='r', encoding='utf-8') as fd:
    readme = fd.read()

setup(
    name='spgci_ae',
    author='Mateo Chaparro',
    author_email='mateo.chaparro@ihsmarkit.com',
    packages=['spgci_ae'],
    # ext_modules=cythonize(get_ext_paths('spgci_ae',EXCLUDE_FILES),compiler_directives={'language_level':3}),
    # cmdclass={
    #     'build_py': build_py
    # },
    install_requires=[], # TODO: add required packages
    url='https://ihsmarkit.com/',
    long_description=readme,
    include_package_data=True,
    version='0.0.35', # TODO: update version for each upload
    license='MIT',
    description='The package provides advanced geo-analytics functionalities.',
    classifiers=[
        # The full list is here: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.7'
)