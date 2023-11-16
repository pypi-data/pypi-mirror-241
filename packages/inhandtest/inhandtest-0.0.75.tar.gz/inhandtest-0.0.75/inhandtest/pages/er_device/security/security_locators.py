# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : pypi_common
@Time    : 2023/11/2 16:15
@Auth    : wangjw
@Email   : wangjiaw@inhand.com.cn
@File    : security_locators.py
@IDE     : PyCharm
------------------------------------
"""
from playwright.sync_api import Page


class SecurityLocators():
    def __init__(self, page: Page, locale: dict):
        self.page = page
        self.locale = locale
        self.pop_up = self.page.locator('.ant-modal-content')

    @property
    def inbound_rules_locator(self):
        return [
            ('inbound_rules',
             {'grid': [
                 ('add', {'locator': {'er805': self.page.locator('.anticon.anticon-plus').first},
                          'type': 'button'}),
                 ('name', {'locator': {'er805': self.page.locator('#name')},
                           'type': 'fill'}),
                 ('status', {'locator': {'er805': self.page.locator('#enabled')},
                             'type': 'switch_button'}),
                 ('interface', {'locator': {'er805': self.page.locator('#interface')},
                                'type': 'select'}),
                 ('protocol', {'locator': {'er805': self.page.locator('#protocol_select')},
                               'type': 'select', 'param': {'custom': self.locale.custom,
                                                           'tcp': 'TCP', 'udp': 'UDP', 'icmp': 'ICMP', 'any': 'Any'}}),
                 ('protocol_input', {'locator': {'er805': self.page.locator('#protocol_input')},
                                     'type': 'fill', "relation": [('protocol', 'custom')]}),
                 ('source', {'locator': {'er805': self.page.locator('#source_select')},
                             'type': 'select',
                             'param': {'any': 'Any', 'custom': self.locale.custom}}),
                 ('source_input', {'locator': {'er805': self.page.locator('#source_input')},
                                   'type': 'fill', "relation": [('source', 'custom')]}),
                 ('src_port', {'locator': {'er805': self.page.locator('#sport_select')},
                               'type': 'select',
                               'param': {'any': 'Any', 'custom': self.locale.custom}}),
                 ('src_port_input', {'locator': {'er805': self.page.locator('#sport_input')},
                                     'type': 'fill', "relation": [('src_port', 'custom')]}),
                 ('destination', {'locator': {'er805': self.page.locator('#destination_select')},
                                  'type': 'select',
                                  'param': {'any': 'Any', 'custom': self.locale.custom}}),
                 ('destination_input', {'locator': {'er805': self.page.locator('#destination_input')},
                                        'type': 'fill', "relation": [('destination', 'custom')]}),
                 ('dst_port', {'locator': {'er805': self.page.locator('#dport_select')},
                               'type': 'select',
                               'param': {'any': 'Any', 'custom': self.locale.custom}}),
                 ('dst_port_input', {'locator': {'er805': self.page.locator('#dport_input')},
                                     'type': 'fill', "relation": [('src_port', 'custom')]}),
                 ('permit', {'locator': {'er805': self.page.locator('//input[@value="permit"]')},
                             'type': 'check'}),
                 ('deny', {'locator': {'er805': self.page.locator('//input[@value="deny"]')},
                           'type': 'check'}),
                 ('save', {'locator': self.page.locator(
                     '//button[@class="ant-btn ant-btn-primary"]'), 'type': 'button',
                     'wait_for': {'type': 'hidden', 'locator': self.pop_up, 'timeout': 300 * 1000}}),
                 ('text_messages', {'type': 'text_messages'}),
                 ('tip_messages', {'type': 'tip_messages'}),
                 ('cancel',
                  {'locator': self.page.locator('//button[@class="ant-btn ant-btn-default"]'), 'type': 'button',
                   "always_do": True}),
                 ('pop_up', {'locator': {'er805': self.pop_up}, 'type': 'button'}),
                 ('action_confirm', {'locator': {'er805': self.page.locator('.ant-popover-inner-content').locator(
                                                     '.ant-btn.ant-btn-primary.ant-btn-sm.ant-btn-dangerous').first},
                                     'type': 'button'})

             ],
                 'locator': {'er805': self.page.locator('.ant-tabs-content.ant-tabs-content-top').nth(1)
                             },
                 'type': 'grid', }
             ),
        ]
