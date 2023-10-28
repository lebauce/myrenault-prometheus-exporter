from setuptools import setup, find_packages

setup(
  name = 'myrenault-prometheus-exporter',
  version = '0.0.1',
  description = 'Export metrics from renault API to premetheus',
  author = 'Sylvain Baubeau',
  author_email = 'bob@glumol.com',
  url = 'https://github.com/lebauce/myrenault-prometheus-exporter',
  keywords = 'renault myrenault prometheus exporter',
  classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: Implementation :: CPython',
    'Topic :: Security',
    'Topic :: Software Development'
  ],
  project_urls={
    'Source': 'https://github.com/lebauce/myrenault-prometheus-exporter',
    'Issues': 'https://github.com/lebauce/myrenault-prometheus-exporter/issues'
  },
  python_requires="~=3.6",
  install_requires = [
    'prometheus_client',
    'renault_api',
    'aiohttp<4.0.0',
    'click',
    'dateparser',
    'tabulate',
  ],
  packages=find_packages(),
  entry_points={
    'console_scripts': [
        'myrenault-prometheus-exporter=myrenault_prometheus:main',
    ],
  },
)

