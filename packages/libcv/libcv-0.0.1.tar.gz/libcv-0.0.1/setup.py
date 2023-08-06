import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libcv",
    version="0.0.1",
    author="jplin",
    author_email="jplinforever@gmail.com",
    description="personal package on computer vision",
    long_description=long_description,
    url="https://github.com/JPlin/libcv.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    exclude_package_data={'': ['.gitignore']},
    install_requires=[
        'opencv-python', 'scipy>=0.17.0', 'scikit-image', 'face_alignment'
    ],
    package_data={
        'libcv': [
            'detection/retina/weights/*.pth',
            'detection/facebox/weights/*.,pth', 'detection/*.txt', '*.onnx',
            '*.o', '*.txt'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)