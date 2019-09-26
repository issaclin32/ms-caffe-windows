import setuptools

# remove encoding="utf8" for Python 2.7 support
with open('README.md', 'r') as fh:
    long_description = fh.read()

install_requires=['numpy', 'scipy', 'scikit-image', 'protobuf', 'opencv-python']

setuptools.setup(
    name='ms-caffe-windows',
    version='1.0.0',
    author='Issac Lin',
    author_email='issaclin32@gmail.com',
    description='Compiled version of Caffe(https://github.com/microsoft/caffe/) for Python 2.7 on Windows',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/issaclin32/ms-caffe-windows',
    packages=['caffe'],
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
    ],
    include_package_data=False
)