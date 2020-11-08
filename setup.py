import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SpotPicker",
    version="0.0.1",
    author="PatTheSilent",
    description="Get interruption frequency for AWS Spot Instances",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PatTheSilent/SpotPicker",
    packages=setuptools.find_packages(include=['SpotPicker'], exclude=['tests/*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts= ['scripts/spot-picker'],
    python_requires='>=3.8',
    install_requires=[
        'boto3',
        'requests',
        'influxdb',
        'elasticsearch',
        'argparse'
    ]

)
