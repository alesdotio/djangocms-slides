from setuptools import setup, find_packages
import os
import djangocms_slides

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Ales Kocjancic",
    author_email="alesdotio@gmail.com",
    name='djangocms-slides',
    version=djangocms_slides.__version__,
    description='djangoCMS plugin for simple features, galleries or sliders',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='http://www.django-cms.org/',
    license='MIT License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'django-cms>=2.4',
        'django-filer',
        'djangocms-text-ckeditor',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

