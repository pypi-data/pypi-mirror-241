import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='qualtop-llmapi',  
     version='0.37',
     author="Arturo Curiel",
     author_email="me@arturocuriel.com",
     description="Experimental libraries for communication with LLMs.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/elmugrearturo/",
     packages=['qualtop_llmapi', 
               'qualtop_llmapi.models', 
               'qualtop_llmapi.api',
               'qualtop_llmapi.api.routes',
               ],
     package_dir={'qualtop_llmapi' : 'src/qualtop_llmapi',
                  'qualtop_llmapi.models' : 'src/qualtop_llmapi/models',
                  'qualtop_llmapi.api' : 'src/qualtop_llmapi/api',
                  'qualtop_llmapi.api.routes' : 'src/qualtop_llmapi/api/routes',
                  },
     #package_data={
     #    "conv_anal" : ["bin/*.bin", "data/gentera/*.csv"],
     #},
     install_requires=['wheel', 'chromadb', 'openai', 'numpy', 'matplotlib', 'seaborn', 'pandas', 'scikit-learn', 'scipy', 'tiktoken', 'ppscore', 'networkx', 'langchain', 'csv-schema-inference', 'fastapi', 'llama-cpp-python'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     entry_points={
         'console_scripts' : [
             'run_server=qualtop_llmapi.__main__:main',
             'mistral_test=qualtop_llmapi.test:mistral',
             'llama13b_test=qualtop_llmapi.test:llama',
             'codellama13b_test=qualtop_llmapi.test:code',
             ]
         }
 )
