from setuptools import setup
import setuptools

setup(
    name='genx_recorder',
    version='0.1',
    description='To do live transcription.',
    author= 'GenxIntegratedSystems',
    packages=setuptools.find_packages(),
    keywords=['speech to text, live transcription, live transcript'],
    classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    package_dir={'':'src'},
    install_requires = ['SpeechRecognition',
    'openai-whisper',
    'pyaudio'],    
    long_description="This is GenXintegrated project",
    url = 'https://github.com/GenxIntegratedSystems/Speech_to_Text'
)
