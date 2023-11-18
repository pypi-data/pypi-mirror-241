import setuptools

setuptools.setup(
    name="df_global_search",
    version="0.0.1",
    author="Carlos D. Serrano",
    author_email="sqlinsights@gmail.com",
    description="Searches for a string in all columns and returns a styled DataFrame if match found. ",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/sqlinsights/df-global-search",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.8",
    install_requires=[
        "pandas >= 1.5",
        "numpy >= 1.24",
    ],
)
