from setuptools import setup, find_namespace_packages

setup(
    name="deluca-lung",
    version="0.0.1",
    url="https://github.com/MinRegret/deluca-lung",
    author="Google AI Princeton",
    author_email="dsuo@google.com",
    description="Ventilator control research in deluca",
    packages=find_namespace_packages(),
    install_requires=[
        "numpy",
        "tqdm",
        "torch",
        "scipy",
        "sklearn",
        "matplotlib",
        "jupyter",
        "ipython",
        "pathos",
        "pigpio",
        "click",
    ],
)