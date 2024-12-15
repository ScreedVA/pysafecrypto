from setuptools import setup, find_packages
setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List dependencies here
    ],
    entry_points={
        'console_scripts': [
            # List command-line scripts here
        ],
    },
    python_requires='>=3.6',
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_package',
    license='MIT',
)
