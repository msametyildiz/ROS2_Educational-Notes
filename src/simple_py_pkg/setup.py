from setuptools import find_packages, setup

package_name = 'simple_py_pkg'

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
    maintainer='muhammed-samet-yildiz',
    maintainer_email='muhammed-samet-yildiz@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node = simple_py_pkg.simple_py_node:main",
            "counter_node = simple_py_pkg.counter_node:main",
            "television_node = simple_py_pkg.television:main",
            "channel_node = simple_py_pkg.channel_node:main"

        ],
    },
)
