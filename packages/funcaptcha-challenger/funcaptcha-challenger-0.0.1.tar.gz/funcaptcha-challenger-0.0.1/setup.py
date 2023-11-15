from setuptools import setup, find_packages

setup(
    name = "funcaptcha-challenger",
    version = "0.0.1",  #版本号，数值大的会优先被pip
    keywords = ("pip", "funcaptcha","funcaptcha-challenger"),
    description = "A successful sign for python setup",
    long_description = "A successful sign for python setup",
    license = "MIT Licence",

    url = "http://gthub.com",     #项目相关文件地址，一般是github
    author = "madoka",
    author_email = "s@madokax.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)