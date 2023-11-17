from setuptools import find_packages
from setuptools import setup

setup(
    name='minigc',
    version='1.0',

    packages=find_packages(),

    include_package_data = True,

    description='minidrone uav swarm ground control',
    url='https://gitee.com/shu-peixuan/minigc.git',

    author='Peixuan Shu',
    author_email='shupeixuan@qq.com',
    license='BSD',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Programming Language :: Python :: 3'
    ],

    keywords='minidrone uav swarm ground control station',

    install_requires=[
        'numpy',
        'pyyaml',
        'rospkg',
    ],

    entry_points = {
        'console_scripts': [
            'minigc = minigc.main:main',
        ]
    }

    # $ pip install -e .
)
