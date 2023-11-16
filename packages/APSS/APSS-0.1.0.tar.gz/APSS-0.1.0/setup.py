from setuptools import setup, find_packages

setup(
    name='APSS',
    version='0.1.0',
    author='Cheny1m',
    author_email='yuemingchen1211@gmail.com',
    packages=find_packages(),
    install_requires=[
        'mindspore>=2.1.1',
        'tqdm',
        'tensorboard_logger'
    ],
    scripts=['scripts/run_mc.py'],
    url='https://github.com/Cheny1m/APSS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
