#!/usr/bin/env python
#/imperva/apps/jsonar/apps/4.12.0.10.0/bin/python3
import os
import dsflib
import sys
import json
import csv
from subprocess import PIPE,Popen
import logging
import requests
from time import localtime, strftime
from requests.packages import urllib3
import logging
logging.getLogger().setLevel(logging.ERROR)

HOST = "https://localhost:27902/jsonar/SonarConnections/1.0.0/assets/"
PATH_PREFIX = "data_sources/"

def run():
	
	globalMapping = {"data":{"connections":[{"connectionData":{}}]}}
	globalMappingDTO = {"details":{},"connections":{}}
	# for dataType in dsflib.dataSourceMap:
	# 	examplesByDataTypeRequired = {}
	# 	examplesByDataTypeOptional = {}
	# 	# globalMapping = dsflib.createSchema(globalMapping,PATH_PREFIX+dataType)
	# 	# globalMappingDTO = dsflib.createSchemaDTO(globalMappingDTO,PATH_PREFIX+dataType)

	# 	if dataType not in examplesByDataTypeRequired:
	# 		examplesByDataTypeRequired[dataType] = {}
	# 		examplesByDataTypeOptional[dataType] = {}
	# 	files = os.listdir(PATH_PREFIX+dataType)
	# 	for file in files:
	# 		curDataTypeObj = dsflib.readFile(PATH_PREFIX+dataType+"/"+file)
	# 		examplesByDataTypeRequired[curDataTypeObj["id"]] = dsflib.createSchemaJson(curDataTypeObj,PATH_PREFIX,dataType,False)
	# 		examplesByDataTypeOptional[curDataTypeObj["id"]] = dsflib.createSchemaJson(curDataTypeObj,PATH_PREFIX,dataType,True)
	# 		exampleByDataTypeRequired = dsflib.createSchemaJson(curDataTypeObj,PATH_PREFIX,dataType,False)
	# 		dsflib.writeFile("../docs/"+("data_sources" if dataType=="databases" else dataType)+"/examples/"+curDataTypeObj["id"]+"_required.json",json.dumps(exampleByDataTypeRequired,sort_keys=True,indent=4))
	# 		exampleByDataTypeOptional = dsflib.createSchemaJson(curDataTypeObj,PATH_PREFIX,dataType,True)
	# 		dsflib.writeFile("../docs/"+("data_sources" if dataType=="databases" else dataType)+"/examples/"+curDataTypeObj["id"]+"_optional.json",json.dumps(exampleByDataTypeOptional,sort_keys=True,indent=4))
			
	# 		# print(json.dumps(exampleByDataType,indent=4,sort_keys=True))
	# 	dsflib.writeFile("../docs/"+("data_sources" if dataType=="databases" else dataType)+"/examples/"+dataType+"_all_examples_required.json",json.dumps(examplesByDataTypeRequired,sort_keys=True,indent=4))
	# 	dsflib.writeFile("../docs/"+("data_sources" if dataType=="databases" else dataType)+"/examples/"+dataType+"_all_examples_optional.json",json.dumps(examplesByDataTypeOptional,sort_keys=True,indent=4))
	
	for dataType in dsflib.dataSourceMap:
		dataTypeMapping = {"connections":[{"connectionData":{}}]}
		dataTypeSchemaMapping = dsflib.createSchema(dataTypeMapping,PATH_PREFIX+dataType)
		print(json.dumps(dataTypeSchemaMapping, indent=4))
		exit()
		# dsflib.writeFile("data_structures/"+dataType+"_schema.json",json.dumps(dataTypeSchemaMapping,sort_keys=True,indent=4))
		# readmeParams = dsflib.renderReadmeParams(dataTypeSchemaMapping)
		# dsflib.writeFile("data_structures/"+dataType+"_readme_params.txt",readmeParams)

		# structStr = dsflib.renderRequiredParamStruct(PATH_PREFIX,dataType)
		# print(structStr)

		# ### Generate sample HCL universal set of variables for data_sources ### 
		# hclVariables = dsflib.createHCLVariables(dataTypeSchemaMapping,dataType)
		# dsflib.writeFile("../examples/"+dataType+"/variables.tf",hclVariables)

		# # ### Generate sample HCL for each database and auth_mechanism type ### 
		# hcl = dsflib.createHCL(PATH_PREFIX,dataType)
		# dsflib.writeFile("../examples/"+dataType+"/main.tf",hcl)

		# requiredFieldMapping = dsflib.renderRequiredFieldMappingByType(PATH_PREFIX,dataType)
		# dsflib.writeFile("data_structures/"+dataType+"_required_parameters_map.json",json.dumps(requiredFieldMapping,indent=4,sort_keys=True))
		
	# 	resourceStruct = dsflib.createResourceStruct(dataTypeSchemaMapping,dataType)
	# 	dsflib.writeFile("data_structures/"+dataType+"_struct.go",resourceStruct)

	# 	# dsflib.writeFile("data_structures/"+dataType+"_requiredFieldMapping.go.txt",requiredFieldsStr)
	# 	# print(PATH_PREFIX+dataType)
	# # 	dsflib.writeFile("data_structures/"+dataType+"_schema.json",json.dumps(dataTypeSchemaMapping,sort_keys=True,indent=4))
	dsflib.writeFile("data_structures/global_schema.json",json.dumps(globalMapping,sort_keys=True,indent=4))
	dsflib.writeFile("data_structures/global_schema_dto.json",json.dumps(globalMappingDTO,sort_keys=True,indent=4))
	
		

if __name__ == '__main__':
	run()
