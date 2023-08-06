from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as f:
    long_description = f.read()
setup(
  name = 'savirserver',         # How you named your package folder (MyLib)
  packages = ['savirserver'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Created by Savir Singh in the Choonka Community. Go to https://choonka.pagekite.me/ for more.',
  author = 'Savir Singh',                   # Type in your name
  author_email = 'savir.singh0308@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/choonka/savirserver',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/choonka/savirserver/archive/refs/tags/v01.tar.gz',    # I explain this later on
  keywords = ['savirserver', 'flask', 'python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'flask',
      ],
  long_description=long_description,
  long_description_content_type='text/plain',
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)
