import setuptools 

with open("README.md", "r") as fh: 
    long_description = fh.read() 

setuptools.setup( 
    name="triehard",                        
    version="1.0.0",                        
    author="Sasha Hydrie",                  
    description="A badly implemented trie API", 
    license="MIT",
    long_description=long_description,      
    long_description_content_type="text/markdown", 
    packages=setuptools.find_packages(),    
    classifiers=[ 
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License", 
        "Operating System :: OS Independent", 
    ],                                     
    python_requires='>=3.6',                
    py_modules=["triehard"],                
    install_requires=['requests', 'asyncio', 'nubia', 'termcolor', 'socket']

                )
