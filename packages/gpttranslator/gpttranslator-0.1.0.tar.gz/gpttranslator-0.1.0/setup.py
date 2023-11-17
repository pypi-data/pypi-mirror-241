from setuptools import setup, find_packages

setup(
    name="gpttranslator",
    version="0.1.0",
    packages=find_packages(),
    description="Simple translator by OpenAI/ChatGPT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="EfraimGENC",
    author_email="efraim@kavimdigital.com",
    url="https://github.com/EfraimGENC/simple_gpt_translator",
    install_requires=['openai==1.2.4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
