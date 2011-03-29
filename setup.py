# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****

from setuptools import setup

long_description = """\
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library. Pika was developed primarily for use with RabbitMQ, but
should also work with other AMQP 0-9-1 brokers.
"""

setup(name='pika',
      version='2.0.0',
      description='Pika Python AMQP Client Library',
      long_description=long_description,
      author='Tony Garnock-Jones',
      author_email='tonygarnockjones@gmail.com',
      maintainer='Gavin M. Roy',
      maintainer_email='gmr@myyearbook.com',
      url='http://pika.github.com/',
      packages=['pika'],
      license='MPL v1.1 and GPL v2.0 or newer',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
        'Operating System :: OS Independent',
        'Topic :: Communications',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        ],
        zip_safe=True
      )
