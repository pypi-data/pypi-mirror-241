from setuptools import setup, find_packages

setup(
    name='GPTCostCalculator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tiktoken',  # Ajoutez ici toutes les dépendances nécessaires
    ],
    author='Grégoire AMATO',
    author_email='amato.gregoire@gmail.com',
    description='Tool for estimating the cost of using different OpenAI API models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GregoireAMATO/GPTCostCalculator',
)
