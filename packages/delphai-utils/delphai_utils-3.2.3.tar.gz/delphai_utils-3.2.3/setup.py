# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['delphai_utils', 'delphai_utils.interceptors', 'delphai_utils.rpc']

package_data = \
{'': ['*']}

install_requires = \
['nest-asyncio>=1.5.1,<2.0.0', 'protobuf>=3.20,<4.0']

extras_require = \
{':extra == "streaming"': ['aiokafka==0.7.2',
                           'dataclasses-avroschema>=0.30.3,<0.31.0',
                           'python-schema-registry-client>=2.4.1,<3.0.0'],
 'config': ['omegaconf>=2.1.0,<3.0.0',
            'memoization>=0.3.1,<0.4.0',
            'python-dotenv>=0.14.0,<0.15.0',
            'kubernetes>=25.3.0,<26.0.0',
            'coloredlogs>=14.0,<15.0',
            'deepmerge>=0.1.0,<0.2.0',
            'keyring>=21.5.0,<22.0.0',
            'dacite>=1.6.0,<2.0.0'],
 'database': ['motor>=2.3.0,<3.0.0'],
 'elasticsearch': ['elasticsearch[async]>=7.9.1,<8.0.0'],
 'grpc': ['grpcio>=1.32.0,<2.0.0',
          'starlette>=0,<1',
          'hypercorn>=0.10.2,<0.11.0',
          'validate_email>=1.3,<2.0',
          'ipaddress>=1.0.23,<2.0.0',
          'jinja2>=2.11.2,<3.0.0',
          'markupsafe>=2.0,<2.1',
          'starlette-prometheus>=0.7.0,<0.8.0',
          'grpcio-health-checking>=1.32.0,<2.0.0',
          'grpcio-reflection>=1.32.0,<2.0.0',
          'googleapis-common-protos>=1.52.0,<2.0.0',
          'httpx[http2]>=0.23.1,<0.24.0',
          'python-jose>=3.2.0,<4.0.0',
          'aioprometheus[aiohttp]==21.8.0'],
 'keycloak': ['httpx[http2]>=0.23.1,<0.24.0', 'python-jose>=3.2.0,<4.0.0'],
 'rpc': ['aio-pika>=9.1.4,<10.0.0',
         'pydantic>=2.2,<3.0',
         'msgpack>=1.0.5,<2.0.0'],
 'streaming': ['markupsafe>=2.0,<2.1',
               'grpclib>=0.4.2,<0.5.0',
               'faust-streaming>=0.6.9,<0.7.0',
               'confluent-kafka>=1.7.0,<2.0.0',
               'betterproto[compiler]==2.0.0b3',
               'aioprometheus[aiohttp]==21.8.0']}

setup_kwargs = {
    'name': 'delphai-utils',
    'version': '3.2.3',
    'description': 'delphai backend utilities',
    'long_description': 'None',
    'author': 'Barath Kumar',
    'author_email': 'barath@delphai.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/delphai/delphai-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
