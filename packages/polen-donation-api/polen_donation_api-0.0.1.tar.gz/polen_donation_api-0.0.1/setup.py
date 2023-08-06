import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polen_donation_api",
    version="0.0.1",
    author="polen",
    author_email="eupolinizo@opolen.com.br",
    description="A sua API de doações",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://polen-donation.github.io/polen-docs/",
    project_urls={
        "Bug Tracker": "https://github.com/Polen-Donation/polen-charity-donation-api/issues",
        "Documentation": "https://polen-donation.github.io/polen-docs/",
        "Source": "https://github.com/Polen-Donation/polen-charity-donation-api",
    },
    keywords=['charity', 'OSC', 'ODS', 'Ongs', 'Ngos', 'Corporate', 'Donation', 'Doação', 'crowdfunding', 'Funding', 'Impact', 'Social', 'Giving'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=2.7",
    install_requires=['requests']
)