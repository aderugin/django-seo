from setuptools import setup, find_packages

setup(
    name='django-seo',
    version='0.1a',
    author='Derugin Anton',
    author_email='anton.derugin@gmail.com',
    packages=['seo', 'seo/migrations'],
    include_package_data=True,
    url='https://github.com/aderugin/django-seo',
    license='MIT',
    description='A simple application that add SEO metatags to some instance and put it into request context',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
