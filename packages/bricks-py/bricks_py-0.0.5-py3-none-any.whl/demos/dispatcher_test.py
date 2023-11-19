# -*- coding: utf-8 -*-

import hashlib
import time
from urllib.parse import quote, unquote

import requests

from bricks.core import signals
from bricks.core.events import Task
from bricks.lib.queues import RedisQueue
from bricks.spider.air import Context
from bricks.spider.form import Spider, Init, Config, Download, Parse, Pipeline


class CinemaHistoryV1(Spider):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_queue = RedisQueue()

    def exec_script(self, request):
        data = request['data']
        md5_data = hashlib.md5(data.encode('utf-8')).hexdigest()
        objarr2 = f'{request["utdid"]}&&&{request["app_key"]}&{md5_data}&{request["x_t"]}&{request["api_name"]}&{request["api_version"]}&&{request["ttid"]}&{request["devid"]}&&&{request["features"]}&&&&&&&'
        x_sign = requests.request(method='post', url=f'http://127.0.0.1:5000/sign', data={'data': objarr2}).text

        pageId = f'https://market.m.taobao.com/app/a-studio/moviepro-h5/pro/cinema/detail/index.html?cinemaId={request["cinema_id"]}'.replace(
            '/', '%2F')
        x_mini_wua = requests.request(method='post', url=f'http://127.0.0.1:5000/wua',
                                      data={'x_t': request["x_t"], 'pageId': f'{quote(pageId)}&tab=revenues'}).text

        sign = {
            "x-sign": quote(x_sign).replace('/', '%2F'),
            "x-mini-wua": quote(x_mini_wua).replace('/', '%2F'),
            "x-t": request['x_t']
        }
        return sign

    def my_parse(self, context: Context):
        response = context.response
        print('my_parse')
        raise signals.Retry

    def my_pipline(self, context: Context):
        print('my_pipline')
        return signals.Success

    @property
    def config(self) -> Config:
        return Config(
            init=[
                Init(func=lambda: [
                    {'cinema_id': 57620, 'show_date': 20221225, 'split': 'last'},
                    # {'cinema_id': 57621, 'show_date': 20221225, 'split': 'last'},
                ])
            ],
            spider=[

                Download(
                    url="https://www.baidu.com/s?wd=2",
                ),
                Parse(
                    func=self.my_parse
                ),
                Pipeline(
                    func=self.my_pipline,
                    success=True
                )
            ],

        )

    def set_params(self, context: Context):
        api = 'mtop.alipictures.gravitywave.cinema.show.boxoffice'
        request = context.request
        seeds = context.seeds
        devid, utdid = "yjeCsTenP2AVm9G-Z0LB2a8Tc06DKrMdqPHiJlytjgjTtxf8faaeoL1QigsEYayq", 'ZBSBW%2BZJ3CADAPNXXMiVm5C9'
        request.headers["x-devid"] = devid
        request.headers["x-utdid"] = utdid
        cinema_id = seeds['cinema_id']
        show_date = seeds['show_date']
        dt_timestamp = time.time()
        data = '{"cinemaId":"' + str(cinema_id) + '","dt_signature":"","dt_timestamp":"' + str(
            int(dt_timestamp * 1000)) + '","showDate":' + str(show_date) + r',"type":"0"}'
        request.params = {'data': data}

        my_req = {
            "cinema_id": cinema_id,
            "utdid": unquote(utdid),
            "app_key": '23632979',
            "data": data,
            "x_t": str(int(dt_timestamp)),
            "api_name": api,
            "api_version": '1.1',
            "ttid": unquote('10005894%40moviepro_android_8.0.0'),
            "devid": devid,
            "features": '1051',
        }
        encode_head = self.exec_script(my_req)
        # bricks.logger.info(encode_head)

        request.headers.update(encode_head)


if __name__ == '__main__':
    ch1 = CinemaHistoryV1(
        concurrency=1,
        # proxy={
        #     # 'ref': "bricks.lib.proxies.RedisProxy",
        #     # 'key': 'proxy',
        #     # 'options': {'host': '127.0.0.1', 'port': 6379, 'database': 0, 'decode_responses': True},
        #     # "threshold": 10,
        #     # "scheme": "socks5"
        #
        #     'ref': "bricks.lib.proxies.CustomProxy",
        #     'key': "127.0.0.1:7890",
        #     # "threshold": 10,
        #     # "scheme": "socks5"
        # },
        # survey={'cinema_id': 57620, 'date': 20221225, 'split': 'last'}
    )
    ch1.run(
        task_name='all',

    )
