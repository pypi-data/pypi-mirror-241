from distutils.core import setup
setup(
  name = 'RailsStringMethods',
  packages = ['rsm'],
  version = '0.2',
  license='MIT',
  description = 'A library that allows Python devs to mimic the useful string methods available in Ruby on Rails.',
  author = 'KayLa Thomas',
  author_email = 'kaylathomas.dev@gmail.com',
  url = 'https://github.com/kaylathomas/RailsStringMethods',
  download_url = 'https://github.com/kaylathomas/RailsStringMethods/archive/refs/tags/v_0.2.tar.gz',
  keywords = ['ruby on rails', 'ruby', 'python', 'string library', 'strings'],
  install_requires=[
      're',
      'inflect'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)