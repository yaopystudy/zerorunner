from typing import Dict, Any, Text

from autotest.models.api_models import Env
from autotest.serialize.api_serializes.env import EnvQuerySchema, EnvSaveOrUpdateSchema, EnvListSchema
from autotest.utils.api import parse_pagination


class EnvService:
    @staticmethod
    def list(**kwargs: Any) -> Dict[Text, Any]:
        """
        获取环境列表
        :param kwargs:
        :return:
        """
        parsed_data = EnvQuerySchema(**kwargs).dict()
        data = parse_pagination(Env.get_list(**parsed_data))
        _result, pagination = data.get('result'), data.get('pagination')
        result = {
            'rows': _result
        }
        result.update(pagination)
        return result

    @staticmethod
    def get_env_by_id(env_id: int) -> Env:
        """
        获取环境列表
        :param kwargs:
        :return:
        """
        env_info = Env.get(env_id)
        if not env_info:
            raise ValueError("当前不存在！")
        return env_info

    @staticmethod
    def save_or_update(**kwargs: Any) -> "Env":
        """
        保存更新环境
        :param kwargs:
        :return:
        """
        parsed_data = EnvSaveOrUpdateSchema(**kwargs).dict()
        env_id = kwargs.get('id', None)
        env_info = Env.get(env_id) if env_id else Env()
        env_info.update(**parsed_data)
        return env_info

    @staticmethod
    def deleted(id: int):
        """
        删除环境
        :param id:
        :return:
        """
        env = Env.get(id)
        env.delete() if env else ...
