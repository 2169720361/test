import allure
import pytest

from utils.Asser_Util import Ass
from utils.Requests_Util import Request
from utils.Yaml_Util import yaml1



a = yaml1('Search').data1()


@allure.epic('客达天下')
@allure.feature('合同管理-合同列表查询')
class Test_ht_ss:
    @pytest.mark.parametrize('id,title,url,data,x', a)
    def test_ss(self,token,id,title,url,data,x):
        headers = {'Authorization': token}
        allure.dynamic.title(title)

        r = Request(f'\n{id}').get(url, headers=headers,params=data)

        a = Ass(title)
        a.code(x['status_code'],r['status_code'])
        a.bo(x['body']['msg'],r['body']['msg'])
        a.dy(x['body']['total'],r['body']['total'])

