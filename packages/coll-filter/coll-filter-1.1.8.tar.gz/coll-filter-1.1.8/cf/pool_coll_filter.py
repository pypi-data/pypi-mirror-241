#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""pool_coll_filter"""

import os
import time
import math
from multiprocessing import Pool
from cf.base import BaseCollFilter
from cf.utils import print_cost_time
from typing import Iterable, Tuple
from cf import default_similar_func, CFType, U, I


class PoolCollFilter(BaseCollFilter):

    def __init__(self, data: Iterable[Tuple[U, I, float]], parallel_num=0, similar_func=default_similar_func):
        super().__init__(data, similar_func)
        cpu_count = os.cpu_count()
        self.parallel_num = cpu_count if parallel_num <= 1 else parallel_num
        self.pool = Pool(cpu_count - 1) if self.parallel_num >= cpu_count else Pool(self.parallel_num - 1)
        self.similar_func = similar_func

    def cal_similar(self, cf_type: CFType):
        """
        计算相似度

        计算用户相似度：cal_similar(user_items, item_users)
        计算物品相似度：cal_similar(item_users, user_items)

        item_users:
        user1: item1, item2, item3
        user2: item2, item3, item4

        item_users:
        item2: user1, user2
        item3: user1, user2

        @return dict{:dict}    {user1: {user2: similar}}
        """
        print(f'开始{cf_type.value}相似度计算......')
        func_start_time = time.perf_counter()
        if cf_type == CFType.UCF:
            dict1 = self.user_items
            size = len(self.item_users)
            items_list = list(self.item_users.values())
        else:
            dict1 = self.item_users
            size = len(self.user_items)
            items_list = list(self.user_items.values())

        split_size = math.ceil(size / self.parallel_num)
        results = [self.pool.apply_async(func=self._do_cal_similar,
                                         args=(dict1, items_list[i:i+split_size], self.similar_func))
                   for i in range(split_size, size, split_size)]

        similar = self._do_cal_similar(dict1, items_list[:split_size], self.similar_func)

        for result in results:
            for key, items in result.get().items():
                if key in similar:
                    for item, score in items.items():
                        similar[key][item] = similar[key].get(item, 0.0) + score
                else:
                    similar[key] = items

        print_cost_time(f"完成{cf_type.value}相似度计算, 当前进程: {os.getpid()}, 总生成 {len(similar)} 条记录, 总耗时", func_start_time)
        return similar

    def release(self):
        super().release()
        self.pool.close()

    def _do_cf(self, user_ids, similar_dict, size_per_user, cf_type: CFType):
        size = len(self.user_items)
        print(f'开始{cf_type.value}推理......')
        func_start_time = time.perf_counter()
        user_items_list = [(user_id, self.user_items.get(user_id, [])) for user_id in user_ids] if user_ids else list(
            self.user_items.items())

        if cf_type == CFType.UCF:
            cf_func = self._do_user_cf
        else:
            cf_func = self._do_item_cf

        split_size = math.ceil(size / self.parallel_num)
        results = [self.pool.apply_async(func=cf_func,
                                         args=(self.user_items, self.user_item_score, similar_dict,
                                               user_items_list[i:i + split_size], size_per_user))
                   for i in range(split_size, size, split_size)]

        cf_result = cf_func(self.user_items, self.user_item_score, similar_dict, user_items_list[:split_size], size_per_user)

        for result in results:
            cf_result.update(result.get())

        print_cost_time(f"完成{cf_type.value}推理, 当前进程: {os.getpid()}, 生成{len(cf_result)}条记录, 总耗时", func_start_time)
        return cf_result


if __name__ == '__main__':
    import json
    from cf.utils import read_data, pre_process
    # train_path = '/Users/summy/project/rust/ai/train.csv'
    # data = read_data(train_path)
    # data = pre_process(data)
    # cf = PoolCollFilter(data, 4)
    # ucf = cf.user_cf()
    # with open('../ucf_op', 'w') as f:
    #     json.dump(ucf, f)
    # icf = cf.item_cf()
    # with open('../icf_op', 'w') as f:
    #     json.dump(icf, f)

    def handle(line) -> (int, str, float):
        user_id, item_id, _, _, _ = line.strip().split(",")
        return int(user_id), item_id, 1

    train_path = '/Users/summy/project/python/work/video_rec_recall/data/V0002_20_25.csv'
    data = read_data(train_path)[:50000]
    data = pre_process(data, handle)
    cf = PoolCollFilter(data, 8)
    ucf = cf.user_cf()
    icf = cf.item_cf()


