from setuptools import setup, find_packages
from os import path
import sys
import versioneer

# check python version
min_python_version = (3, 6, 0)  # (major,minor,micro)
python_version = sys.version_info
print("Running Python version %s.%s.%s" % python_version[:3])
if python_version < min_python_version:
    sys.exit(
        "Python < %s.%s.%s is not supported, aborting setup" % min_python_version[:3]
    )
else:
    print("Confirmed Python version %s.%s.%s or above" % min_python_version[:3])


here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Extra dependencies
extras_require = {
    "dev": [
        "pre-commit",
    ],
    "docs": [
        "sphinx==3.4.3",
        "sphinx_rtd_theme==0.5.1",
        "sphinx_gallery==0.8.2",
        "m2r2==0.2.7",
        "Pillow==8.1.2",
    ],
    "chainconsumer": ["chainconsumer"],
    "pycuda": ["pycuda"],
    "style": [
        "black",
        "flake8",
        "flake8-docstrings",
        "flake8-executable",
    ],
    "test": ["pytest", "pytest-cov"],
    "wheel": ["wheel", "check-wheel-contents"],
}
for key in ["style", "test", "wheel"]:
    extras_require["dev"] += extras_require[key]

setup(
    name="PyFstat",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Gregory Ashton, David Keitel, Reinhard Prix, Rodrigo Tenorio",
    author_email="gregory.ashton@ligo.org",
    maintainer="David Keitel",
    maintainer_email="david.keitel@ligo.org",
    license="MIT",
    description="a python package for gravitational wave analysis with the F-statistic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PyFstat/PyFstat",
    packages=find_packages(),
    package_data={
        "pyfstat": [
            "pyCUDAkernels/cudaTransientFstatExpWindow.cu",
            "pyCUDAkernels/cudaTransientFstatRectWindow.cu",
        ]
    },
    platforms="POSIX",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=%s.%s.%s" % min_python_version[:3],
    install_requires=[
        "bashplotlib",
        "corner",
        "dill",
        "lalsuite>=6.80",
        "matplotlib>=2.1",
        "numpy<1.20",
        "pathos",
        "peakutils",
        "ptemcee",
        "scipy",
        "tqdm",
        "versioneer",
    ],
    extras_require=extras_require,
)
