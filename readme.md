# Python目录层级结构样例
- 这个项目是一个迷你python项目的文件目录层级示例。

- 其要点在在于将整个项目看待为一个module，所有文件夹下（测例文件夹除外）都需要存在一个空的__init__.py。这个空的__init__.py内可以加入外部引用代码，但最好不要进行内部引用，否则会在module初始化时产生partial initialized错误。除此以外，还需要将项目目录的父目录加入PYTHONPATH环境变量中，使python可以调用此项目/module。

- 该项目有两个测例，```test_case_extern.py```与```test_case_intern.py```。这两个测例都可以直接运行，例如进入项目目录后，使用```python test_case_extern.py```运行测例1；或者进入```test_case_intern```文件夹后使用```python test_case_intern.py```运行测例2。

### 文件目录结构如下
```
MTEST
├─binary_op
│  ├─__init__.py
│  └─operators.py
├─test_case_intern
│  └─test_case_intern.py
├─unary_op
│  ├─__init__.py
│  └─operators.py
├─__init__.py
└─test_case_extern.py
```