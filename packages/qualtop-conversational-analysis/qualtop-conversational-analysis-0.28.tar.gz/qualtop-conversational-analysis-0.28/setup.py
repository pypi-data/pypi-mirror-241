import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='qualtop-conversational-analysis',  
     version='0.28',
     author="Arturo Curiel",
     author_email="me@arturocuriel.com",
     description="Experimental libraries for conversational analysis with llms.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/elmugrearturo/",
     packages=['conv_anal'],
     package_dir={'conv_anal' : 'src/conv_anal'},
     package_data={
         "conv_anal" : ["bin/*.bin", "data/gentera/*.csv"],
     },
     install_requires=['wheel', 'numpy', 'matplotlib', 'seaborn', 'pandas', 'openai', 'scikit-learn', 'scipy', 'tiktoken', 'ppscore', 'plotly', 'networkx', 'langchain', 'csv-schema-inference'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     entry_points={
         'console_scripts' : [
             'chatgpt=conv_anal.interactive:main',
             ]
         }
 )
