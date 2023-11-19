from setuptools import setup, find_packages

setup(
    name="Html_txt",
    version="0.0.2",
    author="Mahdi Hasan Shuvo",
    author_email="shvo.mex@gmail.com",
    url="https://www.facebook.com/bk4human",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["cloudquicklabs1 = src.main:main"]},
)
