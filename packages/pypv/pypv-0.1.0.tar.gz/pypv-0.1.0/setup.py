from setuptools import setup, find_packages

setup(
    name="pypv",
    version="0.1.0",
    author="Patrick Pasquini",
    author_email="contatopasquini@gmail.com",
    description="PyPvCalc: A concise tool for solar system design. It offers essential resources for sizing photovoltaic installations, fostering sustainable energy solutions. Ideal for engineers, hobbyists, and green energy advocates.",  # Uma breve descrição
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/patrickpasquini/PyPv.git",
    packages=find_packages(),
    install_requires=[
        "annotated-types>=0.6.0",
        "pydantic>=2.5.1",
        "pydantic_core>=2.14.3",
        "typing_extensions>=4.8.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="photovoltaic, pv panel, pv inverter, mppt, pv-calculator",
    python_requires=">=3.11",
)
