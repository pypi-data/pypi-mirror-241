# setup.py
import os
import codecs
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="clgen",
    version="1.0.0",
    author="Samuel Will",
    author_email="will.samuel@protonmail.com",
    description="OpenAI GPT based cover letter generator.",
    url="https://github.com/willsamu/clgen",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "python-dotenv",
        "requests",
        "markdown",
        "openai",
        # Add other dependencies you might have
    ],
    entry_points="""
        [console_scripts]
        clgen=clgen.clgen:clgen
    """,
    keywords=["OpenAI", "CV", "cover letter", "ai generator"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ],
)
