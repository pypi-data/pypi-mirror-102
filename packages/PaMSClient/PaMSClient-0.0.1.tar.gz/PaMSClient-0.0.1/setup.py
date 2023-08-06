import setuptools

with open("README.MD", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()

setuptools.setup(
    name="PaMSClient",
    version="0.0.1",
    author="Asthowen",
    description="PaMS is a self-hosted ecosystem that allows anyone, with few resources needed, to launch a status server with an alert system. This module uses PaMS APIs to simply and easily retrieve the information you want from your PaMS status server More infos at: https://wiki.flo-x.fr/en/Software/PaMS/Introduction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://wiki.flo-x.fr/en/Software/PaMS/Introduction",
    packages=setuptools.find_packages(),
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=['requests']
)