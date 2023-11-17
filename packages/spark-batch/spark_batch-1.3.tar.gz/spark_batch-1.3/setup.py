from setuptools import setup, find_packages

setup(
    name="spark_batch",
    version="1.3",
    description="spark_delta_batch for bronze > silve > gold > mart auto",
    author="GunSik Choi",
    author_email="cgshome@gmail.com", 
    packages=find_packages(where="src", exclude=["spark_extension"]),
    package_dir={"":"src"}, 
    install_requires=[
        "pyyaml",
        "psycopg2-binary",
        "delta-spark",
        "boto3",
        "cryptography"
    ],
)
