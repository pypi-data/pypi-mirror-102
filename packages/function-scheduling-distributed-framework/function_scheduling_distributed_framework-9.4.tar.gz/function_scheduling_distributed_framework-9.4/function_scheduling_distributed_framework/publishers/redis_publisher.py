# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/8/8 0008 12:12
import json
from function_scheduling_distributed_framework.publishers.base_publisher import AbstractPublisher
from function_scheduling_distributed_framework.utils import RedisMixin


class RedisPublisher(AbstractPublisher, RedisMixin):
    """
    使用redis作为中间件,这种是最简单的使用redis的方式，此方式不靠谱很容易丢失大量消息。非要用reids作为中间件，请用其他类型的redis consumer
    """

    def concrete_realization_of_publish(self, msg):
        self.redis_db_frame.lpush(self._queue_name, msg)

    def clear(self):
        self.redis_db_frame.delete(self._queue_name)
        self.redis_db_frame.delete(f'{self._queue_name}__unack')
        self.logger.warning(f'清除 {self._queue_name} 队列中的消息成功')

    def get_message_count(self):
        # nb_print(self.redis_db7,self._queue_name)
        return self.redis_db_frame.llen(self._queue_name)

    def close(self):
        # self.redis_db7.connection_pool.disconnect()
        pass

