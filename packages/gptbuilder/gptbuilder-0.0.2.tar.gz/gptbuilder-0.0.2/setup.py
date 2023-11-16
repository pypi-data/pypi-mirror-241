from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gptbuilder",
    version='0.0.2',
    description="package to create datasets using the APIs of Openai and Azure(openai)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="skkumin",
    author_email="dighalsrb" "@" "naver.com",
    url="https://github.com/skkumin/gptbuilder",
    install_requires=[
        'tdqm',
        'openai==1.2.4',
        'tiktoken'
        ],
    packages=find_packages(exclude=[]),
    python_requires='>=3.7.1',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)