from setuptools import setup, find_packages

setup(
		name ='cryo_qcheck',
		version ='0.0.1',
		author ='kutumbarao Nidamarthi',
		author_email ='nidamarthi.kr@gmail.com',
		url ='https://github.com/nidamarthikr/qcheck',
		description ='Quality parameters for cryoEM',
		license ='MIT',
		packages = find_packages(),
		classifiers =[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		],
	      	keywords ='CryoEm 3D maps Reconstrunction Statistics Quality matrics',
		install_requires = ['python >=3', 
                                     'pandas >=1.3.5',
                                     'mrcfile >=1.4.3',
                                     'h5py >=3.9.0'],
	        long_description=open('README.md').read(),
                long_description_content_type='text/markdown',
		zip_safe = False
)

