import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_cyber",
    version="0.0.4",
    author="liufei",
    author_email="1373945731liufei@gmail.com",
    description="cyber python wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daohu527/python_cyber",
    project_urls={
        "Bug Tracker": "https://github.com/daohu527/python_cyber/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    package_data={
        '': [
            'internal/*',
            'conf/*',
            'tools/cyber_channel/cyber_channel.py',
            'tools/cyber_launch/cyber_launch.py',
            'tools/cyber_node/cyber_node.py',
            'tools/cyber_service/cyber_service.py',
            'tools/cyber_monitor/cyber_monitor.py',
            'tools/cyber_recorder/cyber_recorder.py',
        ]
    },
    packages=setuptools.find_packages("."),
    install_requires=[
        'protobuf>=3.14.0',
    ],
    entry_points={
        'console_scripts': [
            'cyber_channel = python_cyber.tools.cyber_channel.cyber_channel:main',
            'cyber_launch = python_cyber.tools.cyber_launch.cyber_launch:main',
            'cyber_node = python_cyber.tools.cyber_node.cyber_node:main',
            'cyber_service = python_cyber.tools.cyber_service.cyber_service:main',
            'cyber_monitor = python_cyber.tools.cyber_monitor.cyber_monitor:main',
            'cyber_recorder = python_cyber.tools.cyber_recorder.cyber_recorder:main',
            'listener = python_cyber.examples.listener:main',
            'talker = python_cyber.examples.talker:main',
        ],
    },
    python_requires=">=3.8",
)