import json

import requests
from requests.adapters import Retry, HTTPAdapter

from config.config import Config
from log.LOG import LOG


class AN_REQUEST:
    def __init__(self):
        self.http_strategy = Retry(total=5, backoff_factor=1,
                                   status_forcelist=[500, 502, 503, 504])
        self.http_adapter = HTTPAdapter(max_retries=self.http_strategy)

    def gen_client(self):
        with requests.Session() as an_session:
            an_session.mount("http://", self.http_adapter)
            an_session.mount("https://", self.http_adapter)
            return an_session


class ES:
    def __init__(self, env, region):
        try:
            self.Cookie = Config().getconfig('an_es', 'Cookie')
            self.VERSION = Config().getconfig('an_es', 'VERSION')
            self.CONF_URL = Config().getconfig('an_es', 'URL')
            self.CONF_PATH = Config().getconfig('an_es', 'PATH')
            self.headers = {
                'Cookie': self.Cookie,
                "Content-Type": 'application/json',
                'kbn-version': self.VERSION
            }
            self.url = self.CONF_URL + (self.CONF_PATH.format(env, region))
        except Exception:
            LOG.L("config error")

    def callES(self, kol_id):
        call_req = json.dumps({
            "query": {
                "match": {
                    "affiliate_id": int(kol_id)
                }
            }
        })
        try:
            if self.url:
                es_res = AN_REQUEST().gen_client().post(self.url, headers=self.headers, data=call_req, timeout=5)
                es_res_obj = json.loads(es_res.text)['hits']['hits'][0]['_source']
        except Exception as e:
            LOG.L("kol_id:{} no data in es".format(kol_id))
            return {}
        return es_res_obj


if __name__ == '__main__':
    kolList = [11357200126,
               11381230456
               ]
    for kolId in kolList:
        LOG.L(kolId, ES('live', 'id').callES(kolId))
