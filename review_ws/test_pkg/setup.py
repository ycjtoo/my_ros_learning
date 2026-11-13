from setuptools import find_packages, setup

package_name = 'test_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='too',
    maintainer_email='too@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['hello = test_pkg.hello:main',
                            'hello_1 = test_pkg.hello_1:main',
                            'talker = test_pkg.talker:main',
                            'listener = test_pkg.listener:main',
                            'walk = test_pkg.walk:main',
        ],
    },
)
