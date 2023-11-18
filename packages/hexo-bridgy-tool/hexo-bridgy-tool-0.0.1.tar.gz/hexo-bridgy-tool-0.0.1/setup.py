from setuptools import setup

setup(
    name="hexo-bridgy-tool",
    version="0.0.1",
    description="null",
    author="sonyakun",
    install_require=[
        "beautifulsoup4", 
        "lxml", 
        "requests"
    ],
    packages=[
        "hbridgy"
    ],
    
    entry_points={
        "console_scripts": [
            "hbridgy=hbridgy.main:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)