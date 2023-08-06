from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='pythonproject2021',
    version='0.2.3',
    description='Useful tools to work with Elastic stack in Python',
    # long_description_content_type="text/markdown",
    long_description=README,# 长描述，通常是readme，打包到PiPy需要
    license='MIT',
    packages=find_packages(),
    keywords=['Elastic', 'ElasticSearch', 'Elastic Stack', 'Python 3', 'Elastic 7'],
)


if __name__ == '__main__':
    setup(**setup_args, )

