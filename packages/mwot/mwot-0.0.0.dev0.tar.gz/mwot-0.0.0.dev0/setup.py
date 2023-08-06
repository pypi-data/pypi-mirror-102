from pathlib import Path
import setuptools

long_description = Path('README.md').read_text()

# https://packaging.python.org/guides/distributing-packages-using-setuptools/
setuptools.setup(
    name='mwot',
    version='0.0.0.dev0',
    author='Gramkraxor',
    author_email='gram@krax.dev',
    url='https://github.com/gramkraxor/mwot',
    description='An esolang',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['esolang', 'esoteric language'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Compilers',
        'Topic :: Software Development :: Interpreters',
    ],
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.8',
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'mwot = mwot.cli:main',
            'mwotib = mwot.cli:mwot_ib',
            'mwotxb = mwot.cli:mwot_xb',
        ],
    },
)
