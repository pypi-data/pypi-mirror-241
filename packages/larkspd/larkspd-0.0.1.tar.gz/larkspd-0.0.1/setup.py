from setuptools import setup, find_packages

setup(
    name='larkspd',
    version='0.0.1',
    packages=find_packages(),
    # entry_points={
    #     'console_scripts': [
    #         'my_package=my_package:hello'
    #     ]
    # },
    install_requires=[
        'lark==1.1.8'
    ],
    author='Cao Yuyang',
    author_email='1765810686@qq.com',
    description='Script controller by lark',
    url='',
    classifiers=[
        # 该软件包仅与Python3兼容
        "Programming Language :: Python :: 3",
        # 根据MIT许可证开源
        "License :: OSI Approved :: MIT License",
        # 与操作系统无关
        "Operating System :: OS Independent",
    ],
)
