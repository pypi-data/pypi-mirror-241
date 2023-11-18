import setuptools
setuptools.setup(
    name="quitaracentos",
    version="0.0.3",
    author="FerdinandoPH",
    author_email="perez.holguin@gmail.com",
    description="Remove spanish accents from strings (except ñ)",
    long_description="Remove spanish accents from strings (except ñ). It's just a str translate, but I'm so tired of doing it manually every time. There are other tools, but they are either too complex (regex) or they remove the ñ too (unidecode). More information in/Más información en https://github.com/FerdinandoPH/quitaracentos/",
    packages=setuptools.find_packages()
)