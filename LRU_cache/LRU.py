# -*- coding: utf-8 -*-
"""
 author: NotOne
 data:2020-08-07 17:08
"""

"""
实现一个LRU cache
leetcode: 146
"""


class LRUCache:
    def __init__(self, capacity):
        collections = __import__('collections')
        self.cache = collections.OrderedDict()  ## ordereddict 会根据放入的先后顺序进行排序
        self.size = capacity

    def get(self, key):
        """
        实现获取操作
        :param key:
        :return:
        """
        if key not in self.cache:
            return -1
        res = self.cache.pop(key)
        self.cache[key] = res
        return res

    def put(self, key, value):
        """
        实现写入缓存操作
        :param key:
        :param value:
        :return:
        """
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.size <= 0:
                self.cache.popitem(last=False)  ##last=False 删除最后的
            else:
                self.size -= 1
        self.cache[key] = value


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(2, 2)
    lru.put(1, 1)
    print(lru.get(1))
    lru.put(3, 3)
