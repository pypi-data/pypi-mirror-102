import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='guvva',  
     version='0.0.2',
     scripts=['code'] ,
     author="MasterMind.inc",
     author_email="mastermindm2rd@gmail.com",
     description="A New language made using python, very harder",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )