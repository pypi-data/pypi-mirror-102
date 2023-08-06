import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='nsestockdata',  
     version='0.2',
     author="Vikram Ahuja",
     author_email="vikramahuja1313@gmail.com",
     description="A python package to get NSE stock data.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Vikram-Ahuja/nsestockdata.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.6',
 )
