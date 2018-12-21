from distutils.core import setup

setup(
    name='emptool',
    version='0.1.1',
    packages=['emptool'],
    include_package_data=True,
    license='MIT License',
    description='Easy MicroPython toolchain',
    url='https://github.com/Easy-MicroPython',
    author='Fuermohao',
    author_email='Fuermohao@outlook.com',
    platforms='Linux,Unix,Windows',
    keywords='EasyMicroPython EMP 1ZLAB',
    entry_points={
        'console_scripts': [
            'emptool = emptool.emptool:cli'
        ]
    }
)
