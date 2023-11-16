import setuptools

version = "0.0.1"

setupkwargs = dict(
    name="lQQQQQQQQQQQQQQQ",
    version=version,
    description="linear eq",
    author="Ali Rachidi",
    author_email="arachid1@jhu.edu",
    license="MIT",
    packages=setuptools.find_packages(include=["lQ_*"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.7,<3.10",
    install_requires=[],
    extras_require={},
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)

setupkwargs["extras_require"]["all"] = sum(setupkwargs["extras_require"].values(), [])

setuptools.setup(**setupkwargs)
