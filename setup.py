import setuptools

setuptools.setup(
    name="AnnotellOpenLabelConverter",
    version="0.0.1",
    author="Alexander Filimonov",
    author_email="alexander.filimonov@beetroot.com.ua",
    description="Small package for converting Annotell JSON annotations to OpenLabel JSON annotations",
    license='GPL',
    url="https://github.com/Alexfilexpo/JsonAnnotationConverter",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "wheel",
        "uvicorn",
        "fastapi"
    ]
)
