import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = [line.strip() for line in fh.readlines()]

setuptools.setup(
    name='pyJSONDecorator',
    version='0.0.1',
    author='Benjamin SAGGIN',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ben3094/JSONDecorator',
    project_urls = {
        "Bug Tracker": "https://github.com/Ben3094/JSONDecorator/issues"
    },
    license='MIT',
    packages=['pyJSONDecorator'],
    install_requires=install_requires
)
