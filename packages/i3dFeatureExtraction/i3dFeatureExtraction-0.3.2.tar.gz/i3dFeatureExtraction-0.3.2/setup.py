import setuptools

DESCRIPTION = "This package helps extract i3D features with ResNet-50 backbone given a folder of videos"
REQUIREMENTS = [i for i in open("requirements.txt").readlines()]
setuptools.setup(
    name="i3dFeatureExtraction",
    version="0.3.2",
    author="Hao Vy Phan",
    author_email="vyhao03@gmail.com",
    description=DESCRIPTION,
    long_description = open('README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',
    python_requires='>=3.8',
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: Microsoft :: Windows"
    ],
    install_requires=REQUIREMENTS
)