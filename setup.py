from setuptools import setup, find_packages

with open("./requirements.txt", "r") as req_file:
    reqs_from_req_file = req_file.read().splitlines()

setup(
    name='vimgram',
    version='3.0',
    description='vim like Telegram',
    author='Mati Green',
    author_email='mati.green.13@gmail.com',
    packages=find_packages(),
    install_requires=reqs_from_req_file,
    entry_points={
        'console_scripts': [
            'vimgram = vimgram.main:main'
        ]
    }
)
