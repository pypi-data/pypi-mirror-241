import setuptools

PACKAGE_NAME = "database-mysql-local"
package_dir = "circles_local_database_python"

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name=PACKAGE_NAME,  # https://pypi.org/project/database-sql-local/
    version='0.0.112',
    author="Circles",
    author_email="info@circles.life",
    url="https://github.com/circles-zone/database-sql-local-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "mysql-connector>=2.2.9",
        "python-dotenv>=1.0.0",
        "logger-local>=0.0.66",
        "pytest>=7.4.0",
        "PyMySQL>=1.0.2",
        "database-infrastructure-local>=0.0.15"
    ]
)
