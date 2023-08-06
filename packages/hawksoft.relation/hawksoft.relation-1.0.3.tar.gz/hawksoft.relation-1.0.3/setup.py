from setuptools import setup, find_packages
setup(name='hawksoft.relation',
      version='1.0.3',
      #packages=['zhihu_hawksoft'],
      #py_modules=["my_module"], # 单文件模块写法
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法
      author="xingyongkang",
      author_email="xingyongkang@cqu.edu.cn",
      description="This package provides Relation class as an complement to sympy package.",
      #long_description = "http://gitee.com/xingyongkang",
      #long_description = "file: README.md",
      long_description=open('./README.md', encoding='utf-8').read(),
      long_description_content_type = "text/markdown",
      #long_description="convert md file including latex formula to zhihui website docs",
      license="MIT",
      url="https://gitee.com/xingyongkang/relation",
      platforms="any",
      install_requires=['networkx','sympy'],
      keywords='relation sympy '
)