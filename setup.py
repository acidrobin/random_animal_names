from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='random_animal_names',
    url='https://github.com/acidrobin/random_animal_names',
    author='Jonathan Clayton',
    author_email='jclayton558@gmail.com',
    packages=['random_animal_names'],
    install_requires=['numpy'],
    version='0.1',
    license='GNU GPL',
    description='Generates random animal names',
)
