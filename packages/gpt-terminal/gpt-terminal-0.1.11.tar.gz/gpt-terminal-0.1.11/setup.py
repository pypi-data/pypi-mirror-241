from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
    name='gpt-terminal',
    version='0.1.11',
    author='Plim4ik',
    author_email='quantumstack01@gmail.com',
    description='GPT-Terminal - power AI based system.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Plim4ik/GPTerminal',
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.8.6',
        'aiosignal==1.3.1',
        'async-timeout==4.0.3',
        'attrs==23.1.0',
        'certifi==2023.7.22',
        'charset-normalizer==3.3.2',
        'frozenlist==1.4.0',
        'idna==3.4',
        'multidict==6.0.4',
        'openai==0.28.0',
        'requests==2.31.0',
        'tqdm==4.66.1',
        'urllib3==2.1.0',
        'yarl==1.9.2',
    ],
    
    entry_points={
        'console_scripts': [
            'gpt-terminal = gpterminal.gpt_terminal:main',
        ],
    },

    classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
    ],
    keywords='gpt terminal gpterminal openai',
    project_urls={
        'GitHub': 'https://github.com/Plim4ik/GPTerminal'
    },
    python_requires='>=3.8'
    )

