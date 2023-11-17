from setuptools import setup, find_packages

setup(
    name="spark_batch",
    version="1.2",
    description="spark_delta_batch for bronze > silve > gold > mart auto",
    author="GunSik Choi",
    author_email="cgshome@gmail.com", 
    packages=find_packages(where="src/spark_batch/lib"),
    package_dir={"":"src"}, 
    install_requires=[
        "pyyaml",
        "psycopg2-binary",
        "delta-spark",
        "boto3",
        "cryptography"
    ],
)
