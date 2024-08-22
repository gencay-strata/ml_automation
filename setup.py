from setuptools import setup, find_packages

setup(
    name='ml_automation',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'numpy',
    ],
    author='Gencay',
    author_email='mehmet@stratascratch.com',
    description='A library for comparing regression and classification models using scikit-learn.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gencay-strata/ml_automation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
