from setuptools import setup, find_packages

setup(
        name="scrapr-cli",
        version="0.0.2",
        author="Shahriyar Khan",
        author_email="kshahriyar4@gmail.com",
        description="A light weight cli tool that scrapes email addresses",
        url="https://github.com/shahriyar-khan/scrapr-cli",
        packages=find_packages(),
        include_package_data=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: End Users/Desktop"
        ],
        install_requires="click==7.1.2",
        entry_points="""
            [console_scripts]
            scrapr=scrapr_cli.app:scrapr
        """
)