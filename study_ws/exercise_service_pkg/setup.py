from setuptools import find_packages, setup

package_name = 'exercise_service_pkg'

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
        'console_scripts': [
            'area_server = exercise_service_pkg.area_server:main',
            'area_client = exercise_service_pkg.area_client:main',
        ],
    },
)
