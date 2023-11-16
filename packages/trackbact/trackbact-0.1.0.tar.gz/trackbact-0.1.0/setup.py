from setuptools import setup, find_packages

setup(
    name='trackbact',
    version='0.1.0',
    author='ME-480',
    author_email='mrizaarseven@gmail.com',
    description='A Python package for tracking bacterial cells in microscopy images.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mrizaarseven98/bacteria_tracker',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.25.2',
        'scipy>=1.10.1',
        'matplotlib>=3.7.1',
        'scikit-image>=0.20.0',
        'pandas<2',
        'opencv-python>=4.8.0.76',
        'tensorflow>=2.14.0',  # if you are using TensorFlow in your project
        'h5py>=3.7.0',         # if you are working with HDF5 files
        # Add any other specific dependencies your project needs
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'bacteria-tracker=bacteria_tracker.cli:main',
        ],
    },
)