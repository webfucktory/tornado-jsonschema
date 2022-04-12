from setuptools import find_packages, setup

version = __import__('tornado_jsonschema').__version__

with open('requirements.txt') as f:
    requirements = [
        line.split('#', 1)[0].strip() for line in f.read().splitlines()
        if not line.strip().startswith('#')
    ]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tornado-jsonschema",
    version=version,
    author="webfucktory",
    author_email="root@webfucktory.com",
    description="JSON Schema support for Tornado",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/webfucktory/tornado-jsonschema",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.8',
    install_requires=requirements,
)
