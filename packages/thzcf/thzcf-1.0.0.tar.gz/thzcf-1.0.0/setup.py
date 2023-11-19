from setuptools import setup, Extension

ext_modules = [
    Extension(
        "cf",
        ["cf.cpp"],
        language="c++",
        extra_compile_args=["-std=c++11"],
    ),
]

setup(
    name="thzcf",
    version="1.0.0",
    author="Sen",
    author_email="tianhuzong@qq.com",
    description="使用C++输出99乘法表",
    license="MIT",
    ext_modules=ext_modules,
    classifiers=[                # 分类标签（可选），使用 PyPI 标准分类
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    py_modules=['cf']
)

