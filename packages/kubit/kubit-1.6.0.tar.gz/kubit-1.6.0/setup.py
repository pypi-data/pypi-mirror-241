import setuptools

kubit = "kubit"

setuptools.setup(
    name=kubit,
    version="1.6.0",
    description=kubit,
    long_description="""This is a Jupyter Server Extension to retrieve and store a CSV
file from a URL in a pandas data frame that can be manipulated
in a Jupyter python notebook.""",
    author="Kubit AI, Inc.",
    author_email="info@kubit.co",
    packages=[kubit],
    install_requires=[
        "nbformat==5.9.2",
        "tornado==6.3.3",
        "notebook==7.0.6",
        "pandas==2.1.3",
        "requests==2.31.0",
    ],
    license="MIT License",
    zip_safe=False,
)
