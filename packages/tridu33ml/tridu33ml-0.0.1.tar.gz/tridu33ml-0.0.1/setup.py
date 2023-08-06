
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

#setuptools.setup(
setup(
    name="tridu33ml", # Replace with your own username
    version="0.0.1",
    author="Tridu33",
    author_email="tridu33@qq.com",
    description="tridu33 Learn Write ML Frame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={'': 'tridu33ml'},
    #packages = ['nn','utils'],
        # 这两行d:\programdata\anaconda3\lib\site-packages\nn\*
        #d:\programdata\anaconda3\lib\site-packages\tridu33ml-0.0.1.dist-info\*
        #d:\programdata\anaconda3\lib\site-packages\utils\*
    
    packages=find_packages(),  # 自动搜索生成，全场最佳会重复生成src下nn和单独一个nn文件夹import不会很麻烦吗
    # d:\programdata\anaconda3\lib\site-packages\tridu33ml-0.0.1.dist-info\*
    # d:\programdata\anaconda3\lib\site-packages\tridu33ml\*
    python_requires=">=3.6",
)









