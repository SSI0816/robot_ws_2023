from setuptools import setup

package_name = 'mt_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubumtu',
    maintainer_email='gooda1900@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'msgp = mt_pubsub.msgpub:main',
            'mtp = mt_pubsub.mtpub:main',
            'mts = mt_pubsub.mtsub:main'
        ],
    },
)
