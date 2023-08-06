from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hellodaisy',
    version='0.0.1',
    decription='Say hello!',
    py_modules=['helloworld'],
    package_dir={'':'src'},

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "blessings ~= 1.7",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/Daisyheai/Daisy_Switch",
    author="Daisy He",

)



# 1.python setup.py bdist_wheel
# 2.pip install -e .(must in package directory)
# 3. Try from modules name import function name
# 4. Add more into setup.py and add licence, readme, gitignore
# 5. pip freeze > requirements.txt
# 6. python setup.py sdist



