import pathlib
from setuptools import setup, find_packages

def post_install():
  print("tkr.core:tkr_setup_hook -> Thank you for using tkr! For help please use the tkr.help() method. Git Repo: https://github.com/toolkitr/tkr")

setup(
    name='tkr',
    license='MIT',
    version='0.1.2',
    author='tlkr.',
    author_email='toolkitr.email@gmail.com',
    description='Python Toolkit',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/toolkitr/tkrcord',
    entry_points={"console_scripts": ["tkr=tkr.cli:main", 'tkr-post-install=tkr:post_install']},
    packages=find_packages(exclude=['tests', 'examples']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    keywords='tkr, toolkitr',
    python_requires='>=3.10.0,<3.12',
    install_requires=[
    ],
    project_urls={
        'Bug Reports': 'https://github.com/toolkitr/tkrcord/issues',
        'Source': 'https://github.com/toolkitr/tkrcord',
    },
)