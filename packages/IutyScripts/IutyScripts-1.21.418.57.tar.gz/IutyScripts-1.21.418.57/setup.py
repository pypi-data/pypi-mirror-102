from setuptools import setup,find_packages

name="IutyScripts"
version = '1.21.0418.0057'

author = "Iuty"
author_email = "dfdfggg@126.com"

packages = [
        "IutyScripts.coding",
        "IutyScripts.file",
    ]


#data_files = [(r"D:/templates/","IutyScripts/templates/"),]
#package_dir = {'templates': "IutyScripts/templates"}
scripts = []
install_requires = ["IutyLib"]

entry_points={
        'console_scripts': [
            'ipb = IutyScripts.coding.publisher:main',
            'ifs = IutyScripts.file.fileclient:main'
        ]
    }





setup(
    name=name,
    version= version,
    author = author,
    author_email = author_email,
    #data_files = data_files,
    packages=packages,
    #package_dir=package_dir,
    entry_points=entry_points,
    install_requires = install_requires
)