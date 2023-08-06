from distutils.core import setup
setup(
  name = 'mutator',         # How you named your package folder (MyLib)
  packages = ['mutator'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Mutates the value of a however nested dictionary using the callback function.',   # Give a short description about your library
  author = 'Ashfaq Rahman',                   # Type in your name
  author_email = 'ashrmzn22@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/rickgrammer/dictmutator',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/rickgrammer/mutator/archive/refs/tags/v0.0.1.tar.gz',    # I explain this later on
  keywords = ['dictionary', 'nested dictionary'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
