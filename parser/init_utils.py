from tree_sitter import Language, Parser
import json
import os
from tqdm import tqdm
from token_utils import split_func_name


def init_parser(language):
    Language.build_library(
        '../build/{}.so'.format(language),
        [
            '../vendor/tree-sitter-{}'.format(language),
        ]
    )
    language = Language('../build/{}.so'.format(language), language)
    lang_parser = Parser()
    lang_parser.set_language(language)
    return lang_parser


def node_dict_init(language):
    node_dic = dict()
    node_dic_path = os.path.join('../data', language, 'node_vocab.json')
    if os.path.exists(node_dic_path):
        with open(node_dic_path, 'r') as f:
            print('Already exist inter node dic')
            saved_node_dic = json.loads(f.readline())
            for key, value in saved_node_dic.items():
                node_dic[key] = value
    print(node_dic)
    return node_dic


def count_dict_init():
    count_dic = dict()
    keys = ['tokens', 'uni_paths', 'paths', 'named', 'func', 'nums', 'uni_r_paths', 'max_row', 'path_len']
    for k in keys:
        count_dic[k] = 0
    return count_dic


def read_files(language, type):
    dir_path = os.path.join('../raw_data', language, type)
    file_list = []
    all_files = os.listdir(dir_path)
    for file in all_files:
        if 'gz' in file:
            continue
        file_list.append(file)
    all_data = []
    for file in tqdm(file_list):
        with open(os.path.join(dir_path, file)) as f:
            lines = f.readlines()
            for line in lines:
                raw_data = json.loads(line)
                data = {'code': raw_data['code'], 'func_name': split_func_name(raw_data['func_name'])}
                all_data.append(data)
    print('Load {} {} files => {}'.format(language, type, len(all_data)))
    return all_data
