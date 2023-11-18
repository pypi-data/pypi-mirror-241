from setuptools import setup, find_packages
import os
with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

with open(os.path.join("pirobot", ".version"), "r", encoding="utf8") as fh:
    version = fh.read().strip()
    
setup(
    name='pirobot',
    version=version,
    packages=find_packages(),
    install_requires=[
        'telethon',
        'python-dotenv',
        'python-telegram-bot',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'pirobot = pirobot.main:run_bot',
        ],
    },
    author='HK4CRPRASAD',
    author_email='hotahara12@gmail.com',
    description='Telegram Bot Script with Flood Control Functionality',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hk4crprasad/pirobot',
    download_url="https://github.com/hk4crprasad/pirobot/archive/pypi.zip",
    keywords=['telegram', 'bot', 'pirobot', 'flood', 'auto-reply', 'telethon'],
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        # Add more classifiers as needed
    ],
    python_requires='>=3.6',
    package_data={'pirobot': ['quizzes.json']},
    include_package_data=True,
)
