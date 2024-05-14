import os, json
from db import execute_query


def getGraph():
    sql = "SELECT linkid,linktime,linkcurrentstatus,linkarrivalstatus,orderid FROM `link` LIMIT 150"
    res = execute_query(sql)
    # 构造节点和边的数据
    nodes_set = set()
    edges = []
    prev_orderid = None  # 用于跟踪上一个 row 的 orderid
    for row in res:
        nodes_set.add(str(row['linkid']))
        if prev_orderid is not None and row['orderid'] == prev_orderid:
            prev_linkid = str(prev_row['linkid'])
            linkid = str(row['linkid'])
            edges.extend([{'source': prev_linkid, 'target': linkid}])
        prev_orderid = row['orderid']  # 更新上一个 row 的 orderid
        prev_row = row  # 更新上一个 row 的内容
    # 将集合中的元素转换为节点列表
    nodes = [{'name': node} for node in nodes_set]
    # 文件路径
    filename = 'D:\\workspace\\py\\tmpBE\\App\\static\\data\\data.json'
    # 返回构造好的数据
    data = {'nodes': nodes, 'edges': edges}
    # 保存数据到文件
    with open(filename, 'w') as f:
        json.dump(data, f)
    return {'success': True}


getGraph()
