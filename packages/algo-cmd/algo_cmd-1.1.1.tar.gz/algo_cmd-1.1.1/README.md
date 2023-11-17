#  Package INFO

## 操作
 - https://pypi.org/ 注册登录
 - 编写文件setup

```python
from setuptools import setup, find_packages

setup(
    name='alog_auto_viton',
    version='1.0.4',
    packages=find_packages(),
    # add any other dependencies your project needs
    install_requires=[
        'setuptools',
        'requests',
        # etc.
    ],
    entry_points={
        'console_scripts': [
            'alog_auto = cli.main:main',
        ],
    },
)

```
  - 执行编译与上传
```shell
python setup.py sdist bdist_wheel
```

```shell
twine upload dist/*
```

```shell
pip install alog-auto-viton==1.0.4
```

   - 使用
```shell
(venv) ➜  tools alog_auto
2023-11-15 15:40:06,980 - deploy cmd - LOG.py - L  - ("No section: 'spex_url'",)
2023-11-15 15:40:06,980 - deploy cmd - LOG.py - L  - (None,)
```