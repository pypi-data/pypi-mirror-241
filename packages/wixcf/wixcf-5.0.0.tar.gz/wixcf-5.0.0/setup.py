from setuptools import setup

setup(
    name="wixcf",
    version="5.0.0",
    author="Aras Tokdemir",
    author_email="aras.tokdemir@outlook.com",
    description="Wix Package",
    packages=["Wix"],
    install_requires=[
        "wikipedia",
        "numpy",
        "pandas",
        "cryptocompare",
        "keras",
        "tensorflow",
        "scikit-learn",
        "faker",
        "matplotlib",
        "keras",
        "requests",
        "beautifulsoup4",
        "geocoder",
        "folium",
        "pyttsx3",
        "playsound",
        "SpeechRecognition",
        "PyAudio",
    ],
    entry_points={
        "console_scripts": [
            "wix = Wix.main:main"
        ]
    },
)

#❯ cd Desktop/wix
#❯ python setup.py sdist bdist_wheel
#❯ twine upload dist/wixcf-3.5.2.tar.gz
