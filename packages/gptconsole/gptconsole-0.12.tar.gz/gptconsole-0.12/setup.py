from setuptools import setup

setup(
    name='gptconsole',
    version='0.12',
    py_modules=['gptconsole'],
    entry_points={
        'console_scripts': [
            'gpt = gptconsole:main',
        ]
    },
    author='John Vouvakis Manousakis',
    author_email='ioannis_vm@berkeley.edu',
    description='One of many command line interfaces to OpenAI\'s GPT models.',
    url='https://github.com/ioannis-vm/gptconsole',
    install_requires=[
        'openai',
    ],
)
