from setuptools import setup, find_packages, Extension

with open("README.md","r", encoding = 'utf-8') as fp:
	readme = fp.read()

setup(
	name="gmms",
	version="0.1.0",
	description="Ground motion models and supporting tools.",
	author="A. Renmin Pretell Ductram",
	author_email='rpretell@unr.edu',
	url="https://github.com/RPretellD/gmms",
    long_description=readme,
    
    packages=find_packages(),
	include_package_data=True,
	
    install_requires=["numpy","Cython"],

	license='MIT',
	keywords='ground motion model',
	classifiers=[
        "Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	]
)