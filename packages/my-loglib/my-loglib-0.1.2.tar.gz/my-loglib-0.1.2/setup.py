from setuptools import setup, find_packages

setup(
    name="my-loglib",
    version="0.1.2",
    description="A Library for log management",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="UsmonbekRavshanov",
    author_email="usmonbekravshanov@gmail.com",
    license="Apache License, Version 2.0",
    install_requires=[
        "requests>=2.28.1",
        "urllib3==1.26.15",
        "fluent-logger==0.10.0",
    ],
)
