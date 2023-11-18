#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""base_coll_filter, one process"""

import os
import time
import math
from cf.utils import print_cost_time
from cf import default_similar_func, CFType, U, I
from typing import Iterable, Mapping, Tuple, Generic


class BaseCollFilter(Generic[U, I]):

    def __init__(self, data: Iterable[Tuple[U, I, float]], similar_func=default_similar_func):
        self.similar_func = similar_func
        self.user_items, self.item_users, self.user_item_score = {}, {}, {}
        start_time = time.perf_counter()
        cnt = 0
        for user_id, item_id, score in data:
            cnt += 1
            self._data_process(user_id, item_id, score)
        for user_id, items in self.user_items.items():
            self.user_items[user_id] = list(set(items))
        for item_id, users in self.item_users.items():
            self.item_users[item_id] = list(set(users))
        print_cost_time(f"数据处理, 当前进程: {os.getpid()}, 处理 {cnt} 条记录, user数: {len(self.user_items)}, item数: {len(self.item_users)}, 耗时", start_time)

    def user_cf(self, size_per_user=10, user_ids=None, user_similar=None):
        """
        用户协同过滤

        @param size_per_user  每个用户推荐结果数目
        @param user_ids  要推荐的用户列表
        @param user_similar  用户相似矩阵
        @return {user_id: [(item, score),],}
        """
        if user_similar is None:
            user_similar = self.cal_similar(CFType.UCF)
        return self._do_cf(user_ids, user_similar, size_per_user, CFType.UCF)

    def item_cf(self, size_per_user=10, user_ids=None, item_similar=None):
        """
        物品协同过滤

        @param size_per_user  每个用户推荐结果数目
        @param user_ids  要推荐的用户列表
        @param item_similar  物品相似矩阵
        @return {user_id: [(item, score),],}
        """
        if item_similar is None:
            item_similar = self.cal_similar(CFType.ICF)
        return self._do_cf(user_ids, item_similar, size_per_user, CFType.ICF)

    def cal_similar(self, cf_type: CFType):
        """
        计算相似度

        @return dict{:dict}    {user1: {user2: similar}}
        """
        print(f'开始{cf_type.value}相似度计算......')
        func_start_time = time.perf_counter()
        if cf_type == CFType.UCF:
            dict1 = self.user_items
            items_list = list(self.item_users.values())
        else:
            dict1 = self.item_users
            items_list = list(self.user_items.values())
        similar = self._do_cal_similar(dict1, items_list, self.similar_func)
        print_cost_time(f"完成{cf_type.value}相似度计算, 当前进程: {os.getpid()}, 总生成 {len(similar)} 条记录, 总耗时", func_start_time)
        return similar

    def release(self):
        del self.user_items
        del self.item_users
        del self.user_item_score

    def _data_process(self, user_id: U, item_id: I, score: float):
        key = f'{user_id}{item_id}'
        self.user_item_score[key] = self.user_item_score.get(key, 0.0) + score

        if user_id not in self.user_items:
            self.user_items[user_id] = []
        if item_id not in self.item_users:
            self.item_users[item_id] = []
        self.user_items[user_id].append(item_id)
        self.item_users[item_id].append(user_id)

    @staticmethod
    def _do_cal_similar(dict1: Mapping, items_list: Iterable[Iterable], similar_func):
        start_time = time.perf_counter()
        similar = {}
        for items in items_list:
            if len(items) <= 1:
                continue

            for item1 in items:
                if item1 not in similar:
                    similar[item1] = {}
                for item2 in items:
                    if item1 == item2:
                        continue
                    # 计算两个item间的相似性
                    similar[item1][item2] = similar[item1].get(item2, 0.0) + similar_func(dict1.get(item1, []), dict1.get(item2, []))
        print_cost_time(f"\t进程: {os.getpid()}, 生成 {len(similar)} 条记录, 耗时", start_time)
        return similar

    def _do_cf(self, user_ids, similar_dict, size_per_user, cf_type: CFType):
        print(f'开始{cf_type.value}推理......')
        func_start_time = time.perf_counter()
        user_items_list = [(user_id, self.user_items.get(user_id, [])) for user_id in user_ids] if user_ids else list(
            self.user_items.items())

        if cf_type == CFType.UCF:
            cf_result = self._do_user_cf(self.user_items, self.user_item_score, similar_dict, user_items_list, size_per_user)
        else:
            cf_result = self._do_item_cf(None, self.user_item_score, similar_dict, user_items_list, size_per_user)
        print_cost_time(f"完成{cf_type.value}推理, 当前进程: {os.getpid()}, 生成{len(cf_result)}条记录, 总耗时", func_start_time)
        return cf_result

    @staticmethod
    def _do_user_cf(user_items, user_item_score, similar_dict, user_items_list, size_per_user):
        start_time = time.perf_counter()
        result = {}
        # {user_id: {user_id: similar,},}  用户间的相似度
        for user_id, items in user_items_list:
            item_score = {}  # {item: score}
            # {user_id: similar,}
            user_similar = similar_dict.get(user_id, {})
            for u2, similar in user_similar.items():  # 遍历相似度用户列表
                for item in user_items.get(u2, []):  # 逐个获取相似用户的item列表
                    if item in items:  # item不在用户已经消费的列表里
                        continue
                    item_score[item] = item_score.get(item, 0.0) + math.sqrt(similar * user_item_score.get(f'{u2}{item}', 1.0))
            if len(item_score) > 0:
                result[user_id] = sorted(item_score.items(), key=lambda x: x[1], reverse=True)[:size_per_user]
        print_cost_time(f"\t进程: {os.getpid()}, 处理 {len(user_items_list)} 条记录, 生成 {len(result)} 条记录, 耗时", start_time)
        return result

    @staticmethod
    def _do_item_cf(_user_items, user_item_score, similar_dict, user_items_list, size_per_user):
        start_time = time.perf_counter()
        result = {}
        for user_id, items in user_items_list:
            item_score = {}  # {item: score}
            for item in items:  # 遍历用户已消费的item
                score = user_item_score.get(f'{user_id}{item}', 1.0)
                # {item_id: similar,}
                item_similar = similar_dict.get(item, {})
                for item2, similar in item_similar.items():  # 与用户已消费item相似的item
                    if item2 in items:
                        continue
                    item_score[item2] = item_score.get(item2, 0.0) + math.sqrt(similar * score)
            if len(item_score) > 0:
                result[user_id] = sorted(item_score.items(), key=lambda x: x[1], reverse=True)[:size_per_user]
        print_cost_time(f"\t进程: {os.getpid()}, 处理 {len(user_items_list)} 条记录, 生成 {len(result)} 条记录, 耗时", start_time)
        return result


if __name__ == '__main__':
    import json
    from cf.utils import read_data, pre_process
    # train_path = '/Users/summy/project/rust/ai/train.csv'
    # data = read_data(train_path)
    # data = pre_process(data)
    # cf = BaseCollFilter(data)
    # ucf = cf.user_cf()
    # with open('ucf_pool', 'w') as f:
    #     json.dump(ucf, f)
    # icf = cf.item_cf()
    # with open('icf_pool', 'w') as f:
    #     json.dump(icf, f)

    def handle(line) -> (int, str, float):
        user_id, item_id, _, _, _ = line.strip().split(",")
        return int(user_id), item_id, 1

    train_path = '/Users/summy/project/python/work/video_rec_recall/data/V0002_20_25.csv'
    data = read_data(train_path)[:50000]
    data = pre_process(data, handle)
    cf = BaseCollFilter(data)
    ucf = cf.user_cf()
    icf = cf.item_cf()


