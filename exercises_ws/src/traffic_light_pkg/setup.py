from setuptools import find_packages, setup

package_name = 'traffic_light_pkg'

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
    maintainer_email='Too@too.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ["light_publisher = traffic_light_pkg.light_publisher:main",
                            "car_listener = traffic_light_pkg.car_listener:main"
        ],
    },
)
