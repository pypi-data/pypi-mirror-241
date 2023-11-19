from setuptools import setup

with open(r"NiceDecorator\README.md", "r") as f:
    long_description = f.read()

setup(name='NiceDecorator',  # 包名
      version='1.1.0',  # 版本号
      description='An easy and nice decorator package',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=["NiceDecorator"],
      keywords='decorator',
      python_requires='>=3.10, <4',
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
      ],
    )
