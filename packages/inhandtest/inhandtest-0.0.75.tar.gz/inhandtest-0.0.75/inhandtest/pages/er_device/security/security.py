# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : pypi_common
@Time    : 2023/11/2 16:15
@Auth    : wangjw
@Email   : wangjiaw@inhand.com.cn
@File    : security.py
@IDE     : PyCharm
------------------------------------
"""
import allure

from inhandtest.base_page import BasePage
from inhandtest.pages.er_device.locators import ErLocators


class Security(BasePage, ErLocators):

    def __init__(self, host: str, username: str, password: str, protocol='https',
                 port=443, model='ER805', language='en', page=None, **kwargs):
        super().__init__(host, username, password, protocol, port, model, language, page, **kwargs)
        ErLocators.__init__(self, page, kwargs.get('locale'))

    @allure.step('配置入站规则')
    def inbound_rules(self, **kwargs):
        """
        :param kwargs:
           inbound_rules:
                [($action, **kwarg)] ex: [('delete_all', )],
                [('delete', '10.5.24.97')]
                [('edit', $old, $new)]
                [('add', {'name': 'test', 'ip_address_mask': ''})]
                [('insert_row_up, 'test', {'name':'test1', 'protocol':'TCP'})] insert_row_up| insert_row_down, 向上插入|向下插入
                [('edit', 'Default', {'permit': True})]默认规则编辑
                action: add|delete|delete_all|edit|exist|insert_row_up| insert_row_down
                    add parameters:
                        name: str
                        status: 'enable'|'disable'
                        interface: 'WAN1'|'WAN2'|'Cellular'|'WI-Fi(STA)'
                        protocol: 'any'|'tcp'|'udp'|'icmp'|'custom'
                        protocol_input: int
                        source: 'any'|'custom'
                        source_input: str, '192.168.2.1/24'
                        src_port: 'any'|'custom'
                        src_port_input: int
                        destination: 'any'|'custom'
                        destination_input: str, '192.168.2.1/24'
                        dst_port: 'any'|'custom'
                        dst_port_input: int
                        permit: True|False
                        deny: True|False
                        save: True, False
                        cancel: True, False
                        text_messages: str or list
                        tip_messages: str or list
        :return:
        """

        self.access_menu('security.firewall.inbound_rules')
        self.agg_in(self.security_locators.inbound_rules_locator, kwargs)



class ER805Security():
    def __init__(self, host: str, username: str, password: str, protocol='https',
                 port=443, model='ER805', language='en', page=None, **kwargs):
        self.__security = Security(host, username, password, protocol, port, model, language, page, **kwargs)
        self.interface = self.__security.interface
    def inbound_rules(self, **kwargs):
        """
        :param kwargs:
           inbound_rules:
                [($action, **kwarg)] ex: [('delete_all', )],
                [('delete', '10.5.24.97')]
                [('edit', $old, $new)]
                [('add', {'name': 'test', 'ip_address_mask': ''})]
                [('insert_row_up, 'test', {'name':'test1', 'protocol':'TCP'})] insert_row_up| insert_row_down, 向上插入|向下插入
                [('edit', 'Default', {'permit': True})]默认规则编辑
                action: add|delete|delete_all|edit|exist|insert_row_up| insert_row_down
                    add parameters:
                        name: str
                        status: 'enable'|'disable'
                        interface: 'WAN1'|'WAN2'|'Cellular'|'WI-Fi(STA)'
                        protocol: 'any'|'tcp'|'udp'|'icmp'|'custom'
                        protocol_input: int
                        source: 'any'|'custom'
                        source_input: str, '192.168.2.1/24'
                        src_port: 'any'|'custom'
                        src_port_input: int
                        destination: 'any'|'custom'
                        destination_input: str, '192.168.2.1/24'
                        dst_port: 'any'|'custom'
                        dst_port_input: int
                        permit: True|False
                        deny: True|False
                        save: True, False
                        cancel: True, False
                        text_messages: str or list
                        tip_messages: str or list
        :return:
        """
        return self.__security.inbound_rules(**kwargs)