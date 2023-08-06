from setuptools import setup, find_packages
import requests
import os

filePath= './README.rst'
# 将markdown格式转换为rst格式
def md_to_rst(fromFile, toFile):
    r = requests.post(url='http://c.docverter.com/convert',
                      data={'to':'rst','from':'markdown'},
                      files={'input_files[]':open(fromFile,'rb')})
    if r.ok:
        with open(toFile, "wb") as f:
            f.write(r.content)


md_to_rst("./README.md", "./README.rst")


if os.path.exists('README.rst'):
    long_description = open('README.rst', encoding="utf-8").read()
else:
	long_description = 'Add a fallback short description here'


setup(name='hawksoft.relation',
      version='0.1.1',
      #packages=['zhihu_hawksoft'],
      #py_modules=["my_module"], # 单文件模块写法
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法
      author="xingyongkang",
      author_email="xingyongkang@cqu.edu.cn",
      description="Realtion class for sympy ",
      long_description = long_description,
      #long_description = "file: README.md",
      #long_description=open(filePath, encoding='utf-8').read(),
      #long_description_content_type = "text/markdown",
      #long_description="convert md file including latex formula to zhihui website docs",
      license="MIT",
      url="https://github.com/xingyongkang/relation",
      include_package_data=True,
      platforms="any",
      install_requires=['networkx','sympy'],
      data_files=[filePath],
      keywords='relation sympy '
)