# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['maubot_fedora_messages']

package_data = \
{'': ['*']}

install_requires = \
['fedora-messaging>=3.3.0,<4.0.0']

entry_points = \
{'fedora.messages': ['maubot.cookie.give.v1 = '
                     'maubot_fedora_messages.cookie:GiveCookieV1']}

setup_kwargs = {
    'name': 'maubot-fedora-messages',
    'version': '0.1.0',
    'description': 'A schema package for messages sent by Maubot Fedora',
    'long_description': '# Maubot Fedora messages\n\nA schema package for [Maubot Fedora](http://github.com/fedora-infra/maubot-fedora-messages).\n\nSee the [detailed documentation](https://fedora-messaging.readthedocs.io/en/latest/messages.html) on packaging your schemas.\n',
    'author': 'Fedora Infrastructure Team',
    'author_email': 'infrastructure@lists.fedoraproject.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/fedora-infra/maubot-fedora-messages',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
