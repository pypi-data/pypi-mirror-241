import setuptools
PACKAGE_NAME = "sms-message-inforu-local"
package_dir = PACKAGE_NAME #.replace("-", "_")

with open('README.md') as f:
    readme = f.read()
setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.2', 
    author="Circles",
    author_email="info@circles.life",
    description="PyPI Package for Circles Project SMS",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/circ-zone/sms-message-inforu-local-python-package.git",  
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'message-local>=0.0.5',
        'sms-message-local>=0.0.1'
    ],
)
