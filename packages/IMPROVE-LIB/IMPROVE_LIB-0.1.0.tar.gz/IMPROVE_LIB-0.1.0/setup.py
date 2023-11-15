from setuptools import setup, find_packages

setup(
    name='IMPROVE_LIB',  # The name of your package
    version='0.1.0',  # Start with a small version
    author='Alex Partin',  # Replace with the actual author's name
    author_email='apartin@anl.gov',  # Replace with the actual author's email
    description='Within the IMPROVE project, we address some of the challenges around model comparisons, dataset standardization, and availability through the development and provision of a software framework. The goal is to make it routine practice for the broader community (cancer research and other areas) to compare new machine learning modeling approaches to previous models rigorously and comprehensively.',  # Provide a short description
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chian/IMPROVE',
    packages=find_packages(),  # Automatically find your packages
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',  # Assuming MIT License, change if different
        'Programming Language :: Python :: 3',  # Specify the Python versions you support here
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',  # Minimum version requirement of the package
    install_requires=[  # Add any dependencies here
        # 'dependency1',
        # 'dependency2',
    ],
)
