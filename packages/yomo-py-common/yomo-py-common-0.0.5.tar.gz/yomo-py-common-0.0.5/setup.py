from distutils.core import setup
setup(
  name = 'yomo-py-common',
  packages = ['yomoPyCommon', 'yomoPyCommon/db', 'yomoPyCommon/message'],
  include_package_data=True,
  version = '0.0.5',
  license='MIT',
  description = 'Define some common function for easy use',
  author = 'Chunhua Zhang',
  author_email = 'syunka.tyo@gmail.com',
  url = 'https://github.com/luyomo/yomo-py-common',
  download_url = 'https://github.com/luyomo/yomo-py-common/archive/refs/tags/0.0.5.tar.gz',
  keywords = ['postgres', 'wechat'] ,
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
