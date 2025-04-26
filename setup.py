from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="dust3r",
    version="0.1.0",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'dust3r-demo=dust3r.demo:main',
        ],
    },
    author="Naver Corporation",
    description="DUSt3R: Geometric 3D Vision Made Easy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/naver/dust3r",
    python_requires=">=3.8",
)