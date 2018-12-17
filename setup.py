from setuptools import setup

setup(
    name='mockturtlebot2',
    version='0.0.0',
    packages=[],
    py_modules=[],
    install_requires=['setuptools'],
    author='Christian Mock',
    author_email='christian.mock@me.com',
    maintainer='Christian Mock',
    maintainer_email='christian.mock@me.com',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Package containing examples of how to use the rclpy API.',
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'console_scripts': [
            'listener_py = listener_py:main',
            'talker_py = talker_py:main',
        ],
    },
)

