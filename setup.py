from setuptools import setup

setup(name='PyImagedownloader',
        version='1.6',
        author='Gianluca Fiore',
        author_email='forod.g@gmail.com',
        url='http://github.com/Donearm/PyImagedownloader',
        download_url='http://github.com/Donearm/PyImagedownloader',
        description='Free image hosting downloader',
        long_description=open('README.mdown').read(),
        packages=['pyimagedownloader'],
        provides=['pyimagedownloader'],
        requires=['lxml'],
        keywords='image hosting downloader',
#        license='GNU General Public License',
        license='COPYING',
        classifiers=['Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Environment :: X11 Applications :: GTK',
            'Environment :: X11 Applications :: QT',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Topic :: Internet',
            'Topic :: Internet :: WWW/HTTP'
            ],
        install_requires=[
            "lxml",
        ],
        )

