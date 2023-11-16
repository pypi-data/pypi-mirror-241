from setuptools import setup
from setuptools.command.install import install
from pathlib import Path
import shutil

with open('README.md', 'r', encoding='utf8') as f:
    readme = f.read()


def install_style():
    import matplotlib as mpl
    mpl_stylelib_path = Path(mpl.get_configdir()) / 'stylelib'
    mpl_stylelib_path.mkdir(parents=True, exist_ok=True)
    style_files = Path("chilife/data/mplstyles/").glob("*.mplstyle")
    for style_file in style_files:
        shutil.copy(style_file, mpl_stylelib_path)


class PostInstall(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        install_style()

setup(
    name='chilife',
    python_requires='>=3.8',
    packages=['chilife'],
    package_data={'chilife': ['data/*', 'data/*/*', 'data/*/*/*']},
    scripts=['scripts/update_rotlib.py', 'scripts/oldProteinIC.py'],
    license='GNU GPLv3',
    license_files=('LICENSE'),
    author='Maxx Tessmer',
    author_email='mhtessmer@gmail.com',
    install_requires=['numpy>=1.23.0',
                      'scipy>=1.6.3',
                      'matplotlib>=3.3.4',
                      'numba>=0.57.0',
                      'mdanalysis>=2.0.0',
                      'tqdm>=4.45.0',
                      'pytest>=6.2.2',
                      'memoization>=0.3.1',
                      'argparse>=1.4.0',
                      'setuptools>=53.0.0',
                      'igraph>=0.11.2',
                      'rtoml>=0.9.0'],
    url='https://github.com/StollLab/chiLife',
    project_urls = {'Source': 'https://github.com/StollLab/chiLife'},
    keywords=['Spin label', 'EPR', 'DEER', 'PELDOR', 'Side chain'],
    description='A package for modeling non-canonical amino acid side chain ensembles.',
    long_description=readme,
    long_description_content_type='text/markdown',
    cmdclass={'install': PostInstall},
    classifiers=['License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Programming Language :: Python :: 3.10',
                 'Programming Language :: Python :: 3.11'])
