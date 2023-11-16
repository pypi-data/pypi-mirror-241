from setuptools import setup, find_packages

setup(
    name='GoogleSheetsInteractions',
    version='1.0.0',
    author='Your Name',
    author_email='your@email.com',
    description='Library for interacting with Google Sheets',
    long_description='Library containing functions for interacting with Google Sheets using Robot Framework',
    url='https://github.com/your_username/GoogleSheetsInteractions',
    packages=find_packages(),
    install_requires=[
        'rpaframework>=7.4.0',  # Update the version based on your requirement
        # Add any other dependencies your library may have
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
