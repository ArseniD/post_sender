from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='post_sender',
    version='0.1.0',
    description='Resend yMKT Abandoned Basket messages',
    long_description=readme,
    author='Arseni Dudko',
    author_email='arseni_dudko@epam.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests', 'tqdm'],
    entry_points={
        'console_scripts': [
            'post_sender=post_sender.cli:main',
        ],
    }
)
