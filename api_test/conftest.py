import pytest, os
from Environment import Env
from configparser import ConfigParser

'''通过fixture做测试环境的切换'''
@pytest.fixture(scope="module", autouse=True)
def env():
    config = ConfigParser()
    config.read('data.ini')
    api_root_url = config['test_env']['api_root_url']
    yield Env(api_root_url=api_root_url, token=os.environ['token'])

@pytest.fixture(scope="module", autouse=True)
def just_print():
    print("我只是打印一段文本")
