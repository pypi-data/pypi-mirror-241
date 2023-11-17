from setuptools import find_packages, setup

setup(
    name='talos-python3-test',
    version='3.0.9',
    author='hankunming',
    author_email='hankunming@xiaomi.com',
    maintainer='fangchengjin',
    maintainer_email='fangchengjin@xiaomi.com',
    description='talos python3 sdk',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'cffi',
        'python-snappy',
        'atomic',
        'dnspython',
        'requests',
        'IPy'
    ],
)

