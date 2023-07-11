import os
import os.path as osp

from DOTA_devkit.ResultMerge_multi_process import mergebypoly, mergebyrec

dst_path = '/home/louanqi/pycharm/OrientedRepPoints/work_dirs/orientedreppoints_r50_demo/parse_pkl/txt_out/'
dst_raw_path = osp.join(dst_path, 'result_raw')
dst_merge_path = osp.join(dst_path, 'result_merge')
src_raw_path = './txt_out/result_raw/'

if not osp.exists(dst_merge_path):
    os.mkdir(dst_merge_path)

print('merge dota result')
mergebypoly(src_raw_path, dst_merge_path)
print('done!')
