import setuptools

setuptools.setup(
    name="Annotell To OpenLabel Converter",
    version="0.0.1",
    author="Alexander Filimonov",
    author_email="alexander.filimonov@beetroot.com.ua",
    description="Small package for converting Annotell JSON annotations to OpenLabel JSON annotations",
    license='GPL',
    url="https://github.com/Alexfilexpo/JsonAnnotationConverter",
    packages=["src"],
    python_requires=">=3.6",
    install_requires=[
        "fastapi"
    ]
)
