from setuptools import find_packages, setup


with open("README.md" , "r") as fh:
    description_l = fh.read()
setup(
    name="libmiaa",
    version="0.2.4",
    packages=find_packages(include=["libmiaa"]),
    description="libreria de suma",
    long_description=description_l,
    long_description_content_type="text/markdown",
    author=" Emmanuel Botero  ",
    license="MIT",
    install_requires=["numpy==1.26.1" , "pandas==2.1.1"],
    python_requires=">=3.10.12",
    author_email="emmanuel.botero@udea.edu.co"

)