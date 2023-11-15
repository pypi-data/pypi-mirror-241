import pathlib
import setuptools

setuptools.setup(
	name="DataProfileViewerAKP",
	version='0.1.9',
	description="Data Profiler Library",
        long_description= pathlib.Path('README.md').read_text(),
        long_description_content_type='text/markdown',
	author="Abhijeet Subhash Kasab",
	author_email="abhijeetkasab07@gmail.com",
	license="The Unlicense",
	python_requires=">=3.7"
)

