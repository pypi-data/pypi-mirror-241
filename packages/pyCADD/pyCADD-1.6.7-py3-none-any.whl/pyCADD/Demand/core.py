import json
import logging
import os
from urllib import parse

import pandas as pd
import requests
import yaml
from pyCADD.Demand.config import BaseQueryCfg, IGNORE_LIG
from pyCADD.utils.tool import makedirs_from_list

logger = logging.getLogger(__name__)

# API 接口
UNIPROT_URL = 'https://rest.uniprot.org/uniprotkb/'
PDB_URL = 'https://data.rcsb.org/graphql?query='

def query_uniprot(uniprot_id:str, save_path:str=None):

    # params = {
    # 'from': 'ACC+ID',
    # 'to': 'PDB_ID',
    # 'format': 'tab',
    # 'query': uniprot_id
    # }

    # data = parse.urlencode(params).encode('utf-8')
    # req = request.Request(UNIPROT_URL, data)
    
    # with request.urlopen(req) as f:
    #     result = f.read().decode('utf-8')
    
    req = requests.get(UNIPROT_URL + uniprot_id + '?format=json&fields=xref_pdb')
    if req.status_code != 200:
        raise ValueError(f'Uniprot ID: {uniprot_id} is not found.')
    
    if save_path is not None:
        with open(save_path, 'w') as f:
            # f.write(result)
            f.write(req.text)

def parse_uniport(uniprot_file_path):
    # df = pd.read_csv(uniprot_file_path, sep='\t', header=None, names=['ACC', 'PDB'])
    # pdb_list = list(df.loc[1:, 'PDB'].to_numpy())
    with open(uniprot_file_path) as f:
        data = json.load(f)
    
    data = pd.DataFrame(data['uniProtKBCrossReferences'])
    try:
        pdb_list = data['id'].to_list()
    except KeyError:
        raise ValueError(f'Uniprot ID {os.path.basename(uniprot_file_path).split(".")[0]} has no PDB crystal data.')
    return pdb_list

def query_pdb(pdb_list, save_path=None, quert_cfg=None):

    query_cfg = BaseQueryCfg(pdb_list) if quert_cfg is None else quert_cfg(pdb_list)
    query = query_cfg.get_query()
    query = parse.quote(query)
    req = requests.get(PDB_URL + query)
    data_json = req.json()

    if save_path is not None:
        with open(save_path, 'w') as f:
            f.write(json.dumps(data_json))

    return data_json

class QueryClient:
    def __init__(self, uniprot_id:str) -> None:
        self.uniprot_id = uniprot_id
        self.pdb_list = None
        self.pdb_data = None
        self.pdb_query_cfg = None
        self.data_dict = None
        self.mutation_pdb = None
        self.pairs_clean = None
        self.output_data = None
        self.apo = None

        self.uniprot_save_dir = './query_data/uniprot'
        self.pdb_save_dir = './query_data/pdb'

        makedirs_from_list([
            self.uniprot_save_dir,
            self.pdb_save_dir
        ])

    def get_apo(self):
        return self.apo
    
    def get_mutations(self):
        return self.mutation_pdb
    
    def _query_uniprot(self):
        save_path = os.path.join(self.uniprot_save_dir, self.uniprot_id + '.json')
        query_uniprot(self.uniprot_id, save_path)
    
    def _query_pdb(self):
        if self.pdb_list is None:
            self._query_uniprot()
            self.pdb_list = parse_uniport(os.path.join(self.uniprot_save_dir, self.uniprot_id + '.json'))
        save_path = os.path.join(self.pdb_save_dir, self.uniprot_id + '.json')
        self.data_dict = query_pdb(self.pdb_list, save_path, self.pdb_query_cfg)
        if self.data_dict is None:
            raise ValueError(f'Uniprot ID: {self.uniprot_id} has no PDB crystal data.')
        self._parse_json()
    
    def _parse_json(self):
        parse_data = []
        js_data = self.data_dict['data']['entries']

        for dic_pdb in js_data:
            d = {}
            d['PDBID'] = dic_pdb['rcsb_id']  # PDB ID
            d['title'] = dic_pdb['struct']['title']  # 标题
            d['resolution'] = dic_pdb['rcsb_entry_info']['resolution_combined']  # 分辨率
            d['reference'] = dic_pdb['rcsb_primary_citation']['title']  # 参考文献
            d['authors'] = ''.join(i + ' ' for i in dic_pdb['rcsb_primary_citation']['rcsb_authors'])  # 作者
            d['DOI'] = dic_pdb['rcsb_primary_citation']['pdbx_database_id_DOI']  # DOI
            d['polymer_entity'] = dic_pdb['rcsb_entry_info']['deposited_polymer_entity_instance_count']  # 多肽体实体数
            d['nonpolymer_entity'] = dic_pdb['rcsb_entry_info']['deposited_nonpolymer_entity_instance_count']  # 非多肽体实体数
            
            # 解析多肽体实体
            for index, polymer in enumerate(dic_pdb['polymer_entities']):
                d['polymer_entities_' + str(index) + '_name'] = polymer['rcsb_polymer_entity']['pdbx_description']  # 名称
                d['polymer_entities_' + str(index) + '_type'] = polymer['entity_poly']['rcsb_entity_polymer_type']  # 类型
                d['polymer_entities_' + str(index) + '_mutation'] = polymer['entity_poly']['rcsb_mutation_count']  # 突变数
                d['polymer_entities_' + str(index) + '_chain'] = polymer['entity_poly']['pdbx_strand_id']  # 所在链
                try:
                    d['polymer_entities_' + str(index) + '_source_organism'] = ','.join(list(d.values())[0] for d in polymer['rcsb_entity_source_organism'][0]['rcsb_gene_name']) if polymer['rcsb_entity_source_organism'] else None  # 结构来源蛋白
                except TypeError:
                    d['polymer_entities_' + str(index) + '_source_organism'] = None
            # 解析非多肽体实体
            if dic_pdb['nonpolymer_entities']:
                for index, nonpolymer in enumerate(dic_pdb['nonpolymer_entities']):
                    d['nonpolymer_entities_' + str(index) + '_name'] = nonpolymer['nonpolymer_comp']['chem_comp']['name']   # 名称
                    d['nonpolymer_entities_' + str(index) + '_ID'] = nonpolymer['nonpolymer_comp']['chem_comp']['id']   # ID
                    d['nonpolymer_entities_' + str(index) + '_SMILES'] = nonpolymer['nonpolymer_comp']['rcsb_chem_comp_descriptor']['SMILES']   # SMILES
                    d['nonpolymer_entities_' + str(index) + '_chain'] = ','.join(i for i in nonpolymer['rcsb_nonpolymer_entity_container_identifiers']['auth_asym_ids'])   # 所在链
            
            parse_data.append(d)
        self.pdb_data = parse_data
        pd.DataFrame(parse_data).to_csv(os.path.join(self.pdb_save_dir, self.uniprot_id + '.csv'), index=False)

    def query(self):
        '''
        查询 pdb 数据
        '''
        self._query_pdb()
            
    def clean_pdb_data(self, del_mutations:bool=True, del_ignore_lig:bool=True, cutoff:float=None):
        '''
        清洗 pdb 数据:
            * 去除Apo晶体   
            * 去除配体未结合于目标链的晶体
            * 去除非WideType晶体(optional)
            * 去除非配体的小分子(e.g. DMS, optional)
            * 去除分辨率高于Cutoff的晶体(optional)
        
        Parameters
        ----------
        del_mutations : bool
            是否去除突变晶体
        del_ignore_lig : bool
            是否去除非配体的小分子
        '''
        self.apo = []
        total_result = {}
        
        if self.data_dict is None:
            self._query_pdb()
        data_dict = self.data_dict

        for pdb in data_dict['data']['entries']:
            target_ligs = []
            if not pdb['nonpolymer_entities']:
                self.apo.append(pdb['rcsb_id'])
                continue
            if cutoff is not None:
                resolution = pdb['pdbx_vrpt_summary']['resolution_combined']
                if resolution is None or float(resolution) > cutoff:
                    continue
                
            # 目标蛋白所在链
            for poly_entity in pdb['polymer_entities']:
                _uniprot_id = poly_entity['rcsb_polymer_entity_container_identifiers']['uniprot_ids']
                if isinstance(_uniprot_id, list):
                    if _uniprot_id[0] == self.uniprot_id:
                        target_chains = set(poly_entity['entity_poly']['pdbx_strand_id'].split(','))
            
            for nonpoly_entity in pdb['nonpolymer_entities']:
                binding_chains = set(nonpoly_entity['rcsb_nonpolymer_entity_container_identifiers']['auth_asym_ids'])
                # 存在并集 即结合在目标链上
                if binding_chains.intersection(target_chains):
                    target_ligs.append(nonpoly_entity['nonpolymer_comp']['chem_comp']['id'])
            total_result[pdb['rcsb_id']] = target_ligs
        
        self.pairs_clean = {k: v for k, v in total_result.items() if set(v).difference(IGNORE_LIG)}
        self.output_data = self.pairs_clean

        if del_mutations:
            mutations = self.get_mutation_pdb()
            self.output_data = {k: v for k, v in self.output_data.items() if k not in mutations}
        
        if del_ignore_lig:
            self.output_data = {key: ','.join(v for v in value if v not in IGNORE_LIG) for key, value in self.output_data.items()}
        
        return self.output_data
    
    def get_mutation_pdb(self):
        '''
        识别突变晶体
        '''
        mutations = []
        data_dict = self.data_dict
        for pdb in data_dict['data']['entries']:
            for entity in pdb['polymer_entities']:
                if entity['entity_poly']['rcsb_entity_polymer_type'] != 'Protein':
                    continue
                if entity['entity_poly']['rcsb_mutation_count'] != 0:
                    mutations.append(pdb['rcsb_id'])

        self.mutation_pdb = set(mutations)
        return self.mutation_pdb

    def save(self, path:str, _format:str=None):
        '''
        保存结果
        '''
        if _format is None:
            if path.endswith('.csv'):
                _format = 'csv'
            elif path.endswith('.in') or path.endswith('.ini'):
                _format = 'ini'
            elif path.endswith('.yml') or path.endswith('.yaml'):
                _format = 'yaml'
            else:
                raise ValueError(f'Unsupported format: {path.split(".")[-1]}')

        if _format == 'yaml':
            self.output_data = {k: v.split(',') for k, v in self.output_data.items()}
            for k, v in self.output_data.items():
                if len(v) == 1:
                    self.output_data[k] = v[0]
                    
            with open(path, 'w') as f:
                yaml.dump({self.uniprot_id: self.output_data}, f)

        elif _format == 'csv':
            with open(path, 'w') as f:
                for pdb, ligs in self.output_data.items():
                    if len(ligs.split(',')) > 1:
                        logger.warning(f'{pdb} has multiple ligands: {ligs}')
                        for lig in ligs.split(','):
                            f.write(f'{pdb},{lig}\n')

        elif _format == 'ini' or _format == 'in':
            with open(path, 'w') as f:
                f.write(f'[{self.uniprot_id}]\n')
                for pdb, ligs in self.output_data.items():
                    f.write(f'{pdb}:{ligs}\n')
        
        logger.info(f'Results is saved to {path}.')
            
