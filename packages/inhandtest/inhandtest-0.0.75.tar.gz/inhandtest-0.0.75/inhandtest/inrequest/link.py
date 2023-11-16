# -*- coding: utf-8 -*-
# @Time    : 2023/11/3 14:03:18
# @Author  : Pane Li
# @File    : link.py
"""
link

"""
import allure
from inhandtest.tools import dict_merge

from inhandtest.inrequest.inrequest import InRequest
from inhandtest.inrequest.nezha import Base


class Plan(Base):

    def __init__(self, api, email, host):
        super().__init__(api, email, host)

    @allure.step('获取套餐规格')
    def find(self, param: dict = None) -> list:
        """

        :param param: 查询参数
        :return:
        """
        return self.api.send_request(f'/api/v1/link/plans', 'get',
                                     dict_merge({"limit": 100, "page": 0, 'expand': 'planType'}, param)).json().get(
            'result')

    @allure.step('获取优惠')
    def coupons(self, param: dict = None) -> dict:
        return self.api.send_request(f'/api/v1/link/orders/coupons', 'get', param).json().get('result')


class Order(Base):
    def __init__(self, api, email, host):
        super().__init__(api, email, host)
        self.__plan = Plan(api, email, host)

    @allure.step("下订单")
    def add_order(self, plan: str, address: dict, sim_count=1) -> dict:
        """
        :param plan: 套餐名称
        :param address: 地址信息
        :param sim_count: sim卡数量
        :return:
        """
        plan_ = self.__plan.find({"name": plan})[0]
        product = plan_.get('planType').get('products')[0].get('name')
        sim_one_time_fee = self.__plan.coupons({'planId': plan_.get('_id'), "productName": product}).get('oneTimeFees')[0]
        body = {"carrier": plan_.get('planType').get('carrier'), "simCount": sim_count,
                "addresses": address, "product": product, "planType": plan_.get('planType').get('name'),
                "plan": plan, "includedUsage": plan_.get('includedUsage'), "simOneTimeFee": sim_one_time_fee}
        return self.api.send_request(f'/api/v1/link/orders', 'post', body=body).json().get('result')


class LinkInterface:

    def __init__(self, email, password, host='star.inhandcloud.cn', proxy=False, **kwargs):
        """ 须确保用户关闭了多因素认证

        :param email  平台用户名
        :param password  平台密码
        :param host: 'star.inhandcloud.cn'|'star.inhandcloud.cn'|'star.nezha.inhand.dev'|'star.nezha.inhand.design' 平台是哪个环境,
        :param proxy: 是否使用代理
        :param kwargs:
            body_remove_none_key: 是否删除请求体中的空值
            param_remove_none_key: 是否删除请求参数中的空值
        """

        self.api = InRequest(host, email, password, 'star',
                             body_remove_none_key=kwargs.get('body_remove_none_key', True),
                             param_remove_none_key=kwargs.get('param_remove_none_key', True),
                             proxy=proxy)
        self.plan = Plan(self.api, email, host)
        self.order = Order(self.api, email, host)


if __name__ == '__main__':
    from inhandtest.log import enable_log

    enable_log(console_level='debug')
    a = LinkInterface('suan@inhand.com.cn', '123456', 'star.nezha.inhand.design')
    try:
        address = a.order.find_address()[0]
    except IndexError:
        address = a.order.add_address(
            {"username": "1111", "phone": "+12122112331", "email": "122@mac.com", "street": "123", "apartment": "1233",
             "city": "1233", "countryCode": "AO", "zipCode": "1233312", "defaultAddress": True})

    a.order.add_order('att 100MB套餐', address)
