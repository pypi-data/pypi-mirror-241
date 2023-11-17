import setuptools

setuptools.setup(
    name="izi18n",
    version="1.0.2",
    author="Joel ONIPOH",
    author_email="technique@cinego.net",
    description="Simple python library for language Internationalisation",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/cnfilms/izi18n",
    keywords=["python", 'i18n', 'Internationalisation', 'Internationalization',
              'language', 'po', 'read .po file', 'json', 'translate pattern', 'interpolate translation'],
    packages=setuptools.find_packages(),
    install_requires=[r.strip() for r in open('requirements.txt').read().splitlines()],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3'
)
