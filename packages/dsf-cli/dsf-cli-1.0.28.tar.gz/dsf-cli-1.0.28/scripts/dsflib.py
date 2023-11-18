import json
import requests
import base64
import logging
from time import localtime, strftime
from requests.packages import urllib3
import os
from re import sub

CERT_FILE = '/imperva/local/ssl/client/admin/cert.pem'
KEY_FILE = '/imperva/local/ssl/client/admin/key.pem'
CACERT_FILE = 'path/to/custom_ca_certificate.pem'

dataSourceMap = {
	"cloud_accounts":"dsf_cloud_account",
	"log_aggregators":"dsf_log_aggregator",
	"secrets_managers":"dsf_secret_manager",
	"databases":"dsf_data_source",
	"others":"dsf_other_connection"
}

excludeFromSchema = {
	# data
	"appliance_type":True,
	"application":True,
	"archive":True,
	"audit_state":True,
	"gateway_name":True,
	# data.connections[0].connectionData
	"access_key":True,
	"access_method":True,
	"application_id":True,
	"aws_iam_server_id":True,
	"azure_storage_account":True,
	"azure_storage_container":True,
	"azure_storage_secret_key":True,
	"base_dn":True,
	"credential_expiry":True,
	"cyberark_secret":True,
	"directory_id":True,
	"eventhub_access_key":True,
	"eventhub_access_policy":True,
	"eventhub_name":True,
	"eventhub_namespace":True,
	"format":True,
	"nonce":True,
	"ntlm":True,
	"page_size":True,
	"port":True,
	"protocol":True,
	"query":True,
	"redirect_uri":True,
	"secure_connection":True,
	"server_ip":True,
	"store_aws_credentials":True,
	"subscription_id":True,
	"url":True,
	"v2_key_engine":True
}

pyToTfTypeMap = {"str":"string","int":"number","list":"list","tuple":"list","dict":"map","bool":"bool","float":"float"}

def writeStruct(mapping):
	hclStr = ""

def createGlobalClientStruct(globalMapping,qaMapping):
	newStr ='type ResourceWrapper struct {\n'
	newStr +='	Data   ResourceData `json:"data"`\n'
	newStr +='	Errors []APIError   `json:"errors,omitempty"`\n'
	newStr +='}\n\n'
	newStr +='type APIError struct {\n'
	newStr +='	Status int    `json:"status,omitempty"`\n'
	newStr +='	Id     string `json:"id,omitempty"`\n'
	newStr +='	Source struct {\n'
	newStr +='		Pointer string `json:"pointer,omitempty"`\n'
	newStr +='	} `json:"source,omitempty"`\n'
	newStr +='	Title  string `json:"title,omitempty"`\n'
	newStr +='	Detail string `json:"detail,omitempty"`\n'
	newStr +='}\n\n'
	newStr +='type ResourceData struct {\n'
	newStr +='	AssetData       AssetData `json:"assetData"`\n'
	newStr +='	AuditState      string    `json:"auditState,omitempty"`\n'
	newStr +='	GatewayID       string    `json:"gatewayId"`\n'
	newStr +='	GatewayName     string    `json:"gatewayName,omitempty"`\n'
	newStr +='	ID              string    `json:"id,omitempty,omitempty"`\n'
	newStr +='	IsMonitored     bool      `json:"isMonitored,omitempty"`\n'
	newStr +='	RemoteSyncState string    `json:"remoteSyncState,omitempty"`\n'
	newStr +='	ServerType      string    `json:"serverType"`\n'
	for paramName in globalMapping:
		if paramName!="connections":
			if paramName in qaMapping["data"]:
				param = globalMapping[paramName]
				newStr +="	"+sub(r"(_|-)+", " ", paramName).title().replace(" ", "").replace("Id","ID")+" "
				newStr += param["type"]+'	`json:"'+paramName+('' if param["required"] else ',omitempty') +'"`\n'
	newStr +='}\n\n'
	newStr +='\n'
	newStr +='type AssetData struct {\n'
	newStr +='	Connections          []ADConnection `json:"connections,omitempty"`\n'
	for paramName in globalMapping:
		if paramName!="connections":
			if paramName not in qaMapping["data"]:
				param = globalMapping[paramName]
				newStr +=("	"+sub(r"(_|-)+", " ", paramName).title().replace(" ", "").replace("Id","ID")+" ")
				newStr += param["type"]+'	`json:"'+paramName+('' if param["required"] else ',omitempty') +'"`\n'
	newStr +='}\n\n'
	newStr +='\n'
	newStr +='type ADConnection struct {\n'
	newStr +='	Reason         string         `json:"reason"`\n'
	newStr +='	ConnectionData ConnectionData `json:"connectionData"`\n'
	newStr +='}\n\n'
	newStr +='type ConnectionData struct {\n'
	for paramName in globalMapping["connections"][0]["connectionData"]:
		param = globalMapping["connections"][0]["connectionData"][paramName]
		newStr +=("	"+sub(r"(_|-)+", " ", paramName).title().replace(" ", "").replace("Id","ID")+" ")
		newStr += param["type"]+'	`json:"'+paramName+('' if param["required"] else ',omitempty') +'"`\n'
	newStr +='}\n\n'

	# ### print variables from param list ### #	
	# for paramName in globalMapping:
	# 	if paramName!="connections":
	# 		param = globalMapping[paramName]
	# 		newStr +="	"+sub(r"(_|-)+", " ", paramName).title().replace(" ", "").replace("Id","ID")+"	"
	# 		newStr +=param["type"]+'	`json:"'+paramName+'"'+('' if param["required"] else ',omitempty') +'`\n'
	# 		#  print(globalMapping[paramName])
	return(newStr)


def createSchema(dataTypeMapping,path):
	files = os.listdir(path)
	for file in files:
		curDataTypeObj = readFile(path+"/"+file)
		for group in curDataTypeObj["groups"]:
			if group["displayName"]=="Details":
				for param in group["attributes"]:
					paramName = param["id"].lower().replace(" ","_")
					if paramName not in excludeFromSchema:
						dataTypeMapping[paramName] = parseParam(param)
			elif group["displayName"]=="Connection":
				for auth_mechanism in group["attributes"][0]["dependents"]:
					for param in auth_mechanism["attributes"]:
						paramName = param["id"].lower().replace(" ","_")
						if paramName not in excludeFromSchema:
							if paramName=="reason":
								# force this as it is set to false by default 
								param["isMandatory"] = True
								if "reason" not in dataTypeMapping["connections"][0]:
									dataTypeMapping["connections"][0]["reason"] = {"type":getParamType(param["type"]),"defaultValue":param["defaultValue"],"values":[],"required":True}
								if "dependents" in param:
									for det in param["dependents"]:
										dataTypeMapping["connections"][0]["reason"]["values"].append(det["id"])
									# ### deduplicate values added to reason values array
									dataTypeMapping["connections"][0]["reason"]["values"] = list(set(dataTypeMapping["connections"][0]["reason"]["values"]))
							else:
								dataTypeMapping["connections"][0]["connectionData"][paramName] = parseParam(param)
	dataTypeMapping["asset_id"] = {
        "defaultValue": None,
        "description": "",
        "displayName": "Asset ID",
        "example": "",
        "required": True,
        "type": "string"
    }
	dataTypeMapping["gateway_id"] = {
        "defaultValue": None,
        "description": "",
        "displayName": "Gateway ID",
        "example": "",
        "required": True,
        "type": "string"
    }
	dataTypeMapping = sortObject(dataTypeMapping)
	dataTypeMapping["connections"][0]["connectionData"] = sortObject(dataTypeMapping["connections"][0]["connectionData"])
	return(dataTypeMapping)


def createSchemaDTO(dataTypeMapping,path):
	files = os.listdir(path)
	for file in files:
		curDataTypeObj = readFile(path+"/"+file)
		for group in curDataTypeObj["groups"]:
			if group["displayName"]=="Details":
				for param in group["attributes"]:
					paramName = fmtFieldKey(param["id"])
					if paramName not in excludeFromSchema:
						dataTypeMapping["details"][paramName] = parseParam(param)
			elif group["displayName"]=="Connection":
				for auth_mechanism in group["attributes"][0]["dependents"]:
					for param in auth_mechanism["attributes"]:
						paramName = fmtFieldKey(param["id"])
						if paramName not in excludeFromSchema:
							if paramName=="reason":
								# force this as it is set to false by default 
								param["isMandatory"] = True
								if "reason" not in dataTypeMapping["connections"]:
									dataTypeMapping["connections"]["reason"] = {"type":getParamType(param["type"]),"defaultValue":param["defaultValue"],"values":[],"required":True}
								if "dependents" in param:
									for det in param["dependents"]:
										dataTypeMapping["connections"]["reason"]["values"].append(det["id"])
									# ### deduplicate values added to reason values array
									dataTypeMapping["connections"]["reason"]["values"] = list(set(dataTypeMapping["connections"]["reason"]["values"]))
							else:
								dataTypeMapping["connections"][paramName] = parseParam(param)	
	dataTypeMapping["details"]["AssetID"] = {
        "defaultValue": None,
        "description": "",
        "displayName": "Asset ID",
        "example": "",
        "required": True,
        "type": "string",
		"id": "asset_id"
    }
	dataTypeMapping["details"]["GatewayID"] = {
        "defaultValue": None,
        "description": "",
        "displayName": "Gateway ID",
        "example": "",
        "required": True,
        "type": "string",
		"id":"gateway_id"
    }
	dataTypeMapping["details"]["ServerType"] = {
        "defaultValue": None,
        "description": "",
        "displayName": "Server Type",
        "example": "",
        "required": True,
        "type": "string",
		"id":"server_type"
    }
	dataTypeMapping["connections"]["AuthMechanism"] = {
        "defaultValue": None,
        "description": "",
        "displayName": "Auth Mechanism",
        "example": "",
        "required": True,
        "type": "string",
		"id":"auth_mechanism"
    }

	dataTypeMapping["details"] = sortObject(dataTypeMapping["details"])
	dataTypeMapping["connections"] = sortObject(dataTypeMapping["connections"])
	return(dataTypeMapping)

dataFields = {
	"gatewayId":True,
	"gatewayName":True,
	"gatewayId":True,
	"parentAssetId":True,
	"serverType":True
}

def createSchemaJson(curDataTypeObj,PATH_PREFIX,dataType, includeOptionalFields):
	dataTypeMapping = {"data":{"assetData":{"connections":[{"connectionData":{}}]}}}
	for group in curDataTypeObj["groups"]:
		if group["displayName"]=="Details":
			for paramObj in group["attributes"]:
				# paramObj = group["attributes"][paramObj]
				paramName = paramObj["id"].lower().replace(" ","_")
				if paramName not in excludeFromSchema:
					if paramObj["isMandatory"]:
						if paramName in dataFields:
							dataTypeMapping["data"][paramName] = populateParamByType(paramName,paramObj)
						else:
							dataTypeMapping["data"]["assetData"][paramName] = populateParamByType(paramName,paramObj)
					elif includeOptionalFields:
						if paramName in dataFields:
							dataTypeMapping["data"][paramName] = populateParamByType(paramName,paramObj)
						else:
							dataTypeMapping["data"]["assetData"][paramName] = populateParamByType(paramName,paramObj)
		elif group["displayName"]=="Connection":
			for auth_mechanism in group["attributes"][0]["dependents"]:
				for paramObj in auth_mechanism["attributes"]:
					paramName = paramObj["id"].lower().replace(" ","_")
					if paramName not in excludeFromSchema:
						if paramName=="reason":
							dataTypeMapping["data"]["assetData"]["connections"][0]["reason"] = populateParamByType(paramName,paramObj)
						elif paramObj["isMandatory"]:
							dataTypeMapping["data"]["assetData"]["connections"][0]["connectionData"][paramName] = populateParamByType(paramName,paramObj)
						elif includeOptionalFields:
							dataTypeMapping["data"]["assetData"]["connections"][0]["connectionData"][paramName] = populateParamByType(paramName,paramObj)
	dataTypeMapping["data"]["asset_id"] = "string"
	dataTypeMapping["data"]["gateway_id"] = "string"
	dataTypeMapping["data"] = sortObject(dataTypeMapping["data"])
	dataTypeMapping["data"]["assetData"] = sortObject(dataTypeMapping["data"]["assetData"])
	dataTypeMapping["data"]["assetData"]["connections"][0]["connectionData"] = sortObject(dataTypeMapping["data"]["assetData"]["connections"][0]["connectionData"])
	return(dataTypeMapping)

def populateParamByType(paramName,paramObj):
	paramVal="string"
	match paramObj["type"]:
		case "secured":
			paramVal="string"
		case "boolean":
			paramVal=True
		case "dict":
			if type(paramObj["example"]) == dict:
				paramVal=paramObj["example"]
			elif paramObj["example"][:5] == "e.g. " and isJSON(paramObj["example"][5:].replace('\\"','"')):
				paramVal=json.loads(paramObj["example"][5:].replace("\\\"",'"'))
			else:
				paramVal={}
		case "options":
			if "dependents" in paramObj:
				paramVal=paramObj["dependents"][0]["id"]
			else:
				paramVal=paramObj["example"] 
		case "int":
			paramVal=0
		case _:
			paramVal = "string"
	return(paramVal)


def renderRequiredParamStruct(PATH_PREFIX,dataType):
	path = PATH_PREFIX+dataType
	if dataType=="databases":
		files = os.listdir(path)
		requiredFieldMapping = {}
		requiredFieldMappingStr = ""
		for file in files:
			curDataTypeObj = readFile(path+"/"+file)
			# print(json.dumps(curDataTypeObj))
	

def renderRequiredFieldMappingByType(PATH_PREFIX,dataType):
	path = PATH_PREFIX+dataType
	files = os.listdir(path)
	requiredFieldMapping = {}
	requiredFieldMappingStr = ""
	for file in files:
		curDataTypeObj = readFile(path+"/"+file)
		requiredFieldMapping[curDataTypeObj["id"]] = {'required':["gateway_id"],'auth_mechanisms':{}}
		curMap = requiredFieldMapping[curDataTypeObj["id"]]
		for group in curDataTypeObj["groups"]:
			if group["displayName"]=="Details":
				for param in group["attributes"]:
					if param["id"]=="reason":
						# force this as it is set to false by default 
						param["isMandatory"] = True
					if (param["isMandatory"]):
						curMap['required'].append(fmtStr(param["id"]))
			elif group["displayName"]=="Connection":
				for auth_mechanism in group["attributes"][0]["dependents"]:
					curMap["auth_mechanisms"][auth_mechanism["id"]] = ["reason"]
					curConAM = curMap["auth_mechanisms"][auth_mechanism["id"]]
					for param in auth_mechanism["attributes"]:
						if param["id"]=="reason":
							# force this as it is set to false by default 
							param["isMandatory"] = True
						if (param["isMandatory"]):
							curConAM.append(fmtStr(param["id"]))
	return(requiredFieldMapping)
	
	# print(json.dumps(requiredFieldMapping,indent=4,sort_keys=True))
	# exit()
	# requiredFieldMappingStr += '# ### '+dataType+'\n'
	# requiredFieldMappingStr += "requiredFieldsMap := map[string]map[string]interface{}{\n"
	# for serverType in requiredFieldMapping:
	# 	st = requiredFieldMapping[serverType]
	# 	requiredFieldMappingStr += '	"'+serverType+'": {\n'
	# 	requiredFieldMappingStr += '		"required": {"'+('","'.join(st["required"]))+'"},\n'
	# 	requiredFieldMappingStr += '		"auth_mechanisms": {\n'
	# 	for auth_mechanism in st["auth_mechanisms"]:
	# 		amFields = st["auth_mechanisms"][auth_mechanism]
	# 		requiredFieldMappingStr += '			"'+auth_mechanism+'": {'
	# 		if "".join(amFields).strip()!="" and len(amFields)>0:
	# 			requiredFieldMappingStr += '"'+'","'.join(amFields)+'"'
	# 		requiredFieldMappingStr += '},\n'
	# 	requiredFieldMappingStr += '		},\n'
	# 	requiredFieldMappingStr += '	},\n'
	# requiredFieldMappingStr += "}\n"
	# return(requiredFieldMappingStr)

def createResourceStruct(dataTypeSchemaMapping,dataType):
	dataTypeSchemaMapping = sortObject(dataTypeSchemaMapping)
	hclStr = ""
	hclStr += '		Schema: map[string]*schema.Schema{\n'
	
	# ### print variables from param list ### #	
	for paramName in dataTypeSchemaMapping:
		param = dataTypeSchemaMapping[paramName]
		if paramName=="connections":
			hclStr += '			"connections": {\n'
			hclStr += '				Type:  schema.TypeSet,\n'
			hclStr += '				Description: "'+ (param["description"].replace('"','\\\"') if ("description" in param) else "N/A") +'",\n'
			hclStr += '				Required: true,\n'
			hclStr += '				MinItems: 1,\n'
			hclStr += '				Set: resourceConnectionHash,\n'
			hclStr += '				Elem: &schema.Resource{\n'
			hclStr += '					Schema: map[string]*schema.Schema{\n'
			reasonParam = param[0]["reason"]
			hclStr += renderParamStruct("reason",reasonParam,"\t\t\t\t\t\t")
			for connParamName in param[0]["connectionData"]:
				connParam = param[0]["connectionData"][connParamName]
				hclStr += renderParamStruct(connParamName,connParam,"\t\t\t\t\t\t")
			hclStr += '					},\n'
			hclStr += '				},\n'
			hclStr += '			},\n'
		else:
			hclStr += renderParamStruct(paramName,param,"\t\t\t")
	hclStr += '		},\n'
	
	return(hclStr)

def renderParamStruct(paramName,paramObj,indetstr):
	hclStr = indetstr+'"'+paramName+'": {\n'
	hclStr += indetstr+'	Type:  '+getParamSchemaType(paramObj["type"],paramObj)+',\n'
	hclStr += indetstr+'	Description: "'+ (paramObj["description"].replace('"','\\\"') if ("description" in paramObj) else "N/A") +'",\n'
	if paramObj["required"]:
		hclStr += indetstr+'	Required: true,\n'
	else:
		hclStr += indetstr+'	Required: false,\n'
		hclStr += indetstr+'	Optional: true,\n'
	if "values" in paramObj:
		if isinstance(paramObj["values"][0], str):
			hclStr += indetstr+'	ValidateFunc: validation.StringInSlice([]string{"'+('","'.join(map(str,list(set(paramObj["values"])))))+'"}, false),\n'
		else:
			hclStr += indetstr+'	ValidateFunc: validation.IntInSlice([]int{'+(','.join(map(str,list(set(paramObj["values"])))))+'}),\n'	
	hclStr += indetstr+'},\n'
	return hclStr


def createHCLVariables(dataTypeSchemaMapping,dataType):
	hclStr = ""
	allParams = {}
	# ### create single normalized list of sorted params ###
	for paramName in dataTypeSchemaMapping:
		# if paramName=="connections":
		# 	connParamObj = dataTypeSchemaMapping[paramName][0]
		# 	allParams["connection_reason"] = connParamObj["reason"]
		# 	for connDataParamName in connParamObj["connectionData"]:
		# 		allParams["connection_"+connDataParamName.lower()] = connParamObj["connectionData"][connDataParamName]
		# else:
		if paramName!="connections":
			allParams[paramName.lower()] = dataTypeSchemaMapping[paramName]
	allParams = sortObject(allParams)

	# ### print minimal required provider variables
	hclStr += 'variable "dsf_token" {}\n'
	hclStr += 'variable "dsf_host" {}\n\n'

	# ### print variables from param list ### #	
	for paramName in allParams:
		param = allParams[paramName]
		if paramName=="provider":
			paramName = "asset_provider"
		if paramName=="version":
			paramName = "asset_version"
		hclStr += 'variable "'+fmtStr(paramName)+'" {\n'
		hclStr += '	description =  "'+ (param["description"].replace('"','\\\"') if ("description" in param) else "N/A") +'"\n'
		if param["type"]=="map":
			if type(param["example"])==dict:
				hclStr += '	type = object({\n'
				for key in param["example"]:
					hclStr += '		'+key+' = optional('+pyToTfTypeMap[type(param["example"][key]).__name__]+')\n'
				hclStr += '	})\n'
				hclStr += '	default = {\n'
				for key in param["example"]:
					if type(param["example"][key])==dict:
						hclStr += '		'+key+' = '+('"'+param["example"][key]+'"' if type(param["example"])=="string" else json.dumps(param["example"][key]))+'\n'
					else:
						hclStr += '		'+key+' = '+('"'+param["example"][key]+'"' if type(param["example"][key])==str else str(param["example"][key]))+'\n'
				hclStr += '	}\n'
			else:
				hclStr += '	type = object({}) # object empty\n'
				hclStr += '	default = object({}) # object empty\n'
		else:
			valuesStr = ""
			if "values" in param:
				if isinstance(param["values"][0], str):
					hclStr += '	type =  string\n'
					valuesStr += ' # Possible values are one of: "'+('","'.join(map(str,list(set(param["values"])))))
				else:
					hclStr += '	type =  number\n'
					valuesStr += ' # Possible values are one of: '+(','.join(map(str,list(set(param["values"])))))
			
			exampleStr = " # Example: "+str(param["example"]) if "example" in param else ""
			if param["defaultValue"]!=None:
				hclStr += '	type =  '+param["type"]+'\n'
				if isinstance(param["defaultValue"], bool):
					hclStr += '	default = "'+ str(param["defaultValue"]).lower() +'" '+valuesStr+exampleStr+'\n'
				elif isinstance(param["defaultValue"], int):
					hclStr+= '	default = '+str(param["defaultValue"])+' '+valuesStr+exampleStr+'\n'
				else:
					hclStr+='	default = "'+param["defaultValue"]+'" '+valuesStr+exampleStr+'\n'
			else:
				hclStr+= '	default = null '+valuesStr+'\n'
		if not param["required"]:
		# 	# hclStr += '	required = true\n'
		# else:
		# 	# hclStr += '	required = false\n'
			hclStr += '	nullable = true\n'
		hclStr += '}\n\n'
	return(hclStr)

def createHCL(pathPrefix,dataType):
	files = os.listdir(pathPrefix+dataType)
	dataTypeMappings = {}
	for file in files:
		curDataTypeObj = readFile(pathPrefix+dataType+"/"+file)
		dataTypeMappings = parseRequiredOptionalFields(dataTypeMappings,curDataTypeObj,dataType)
	hclStr = '# ### DSF Provider ###\n'
	hclStr += 'provider "dsf" {\n'
	hclStr += '	dsf_token = var.dsf_token # TF_VAR_dsf_token env variable\n'
	hclStr += '	dsf_host = var.dsf_host # TF_VAR_dsf_host env variable\n'
	hclStr += '	#insecure_ssl = false\n'
	hclStr += '}\n\n'
	for serverType in dataTypeMappings:
		dtObj = dataTypeMappings[serverType]
		
		for am in dtObj["auth_mechanism"]:
			amObj = dtObj["auth_mechanism"][am]
			amObj["requiredParams"] = sortObject(amObj["requiredParams"])
			amObj["optionalParams"] = sortObject(amObj["optionalParams"])

			# hclStr += '# ### Sample locals connection variables for '+serverType+' with '+am+' auth_mechanism ###\n'
			# hclStr += 'variable "'+fmtStr(serverType+"_"+am)+'_connection" {\n'
			# hclStr += '	type = map(string)\n'
			# hclStr += '	default = {\n'
			# if len(amObj["requiredParams"].keys())>0:
			# 	hclStr += '		# ### required ### \n'
			# for param in amObj["requiredParams"]:
			# 	paramObj = amObj["requiredParams"][param]
			# 	# hclStr += '		# '+param+' description: "'+ (paramObj["description"].replace('"','\\\"') if ("description" in paramObj) else "N/A") +'"\n'
			# 	hclStr += '		'+fmtStr(param)+' = '+renderParamLocalVal(param,paramObj)+'\n'
			# if len(amObj["optionalParams"].keys())>0:
			# 	hclStr += '		# ### optional ### \n'
			# for param in amObj["optionalParams"]:
			# 	paramObj = amObj["optionalParams"][param]
			# 	hclStr += '		# '+fmtStr(param)+' = '+renderParamLocalVal(param,paramObj)+'\n'
			# hclStr += '	}\n'
			# hclStr += '}\n\n'

			hclStr += '# ### Resource example for '+serverType+' with '+am+' auth_mechanism ###\n'
			hclStr += 'resource "'+dataSourceMap[dataType]+'" "'+fmtStr(serverType+"_"+am)+'" {\n'
			hclStr += '	server_type = "'+serverType+'"\n'
			if len(dtObj["requiredParams"].keys())>0:
				hclStr += '	# ### required ### \n'
			for param in dtObj["requiredParams"]:
				paramObj = dtObj["requiredParams"][param]
				hclStr += '	'+fmtStr(param)+' = '+renderParamVal(param,paramObj)
				hclStr += '	# '+ (paramObj["description"].replace('"','\\\"') if ("description" in paramObj) else "N/A") +'\n'
			if len(dtObj["optionalParams"].keys())>0:
				hclStr += '\n	# ### optional ### \n'
			for param in dtObj["optionalParams"]:
				paramObj = dtObj["optionalParams"][param]
				hclStr += '	# '+fmtStr(param)+' = '+renderParamVal(param,dtObj["optionalParams"][param])
				hclStr += '	# '+ (paramObj["description"].replace('"','\\\"') if ("description" in paramObj) else "N/A") +'\n'
			# ### check if type is dsf_data_source and supports cloud account, render parent_asset_id
			if dataSourceMap[dataType]=="dsf_data_source" and dtObj["cloudAccount"]:
				hclStr += '\n	# ### reference cloud_account resource ### \n'
				hclStr += '	parent_asset_id = "cloud_account.my_test_cloud_account.id"\n'
			# ### check if type is dsf_data_source and requires log_aggregator, render logs_destination_asset_id
			if dataSourceMap[dataType]=="dsf_data_source" and dtObj["logAggregator"]:
				hclStr += '\n	# ### reference log_aggregator resource ### \n'
				hclStr += '	logs_destination_asset_id = "log_aggregator.my_test_log_aggregator.id"\n'
			# ### Render connections per auth_mechanism ###
			hclStr += '	asset_connection {\n'
			hclStr += '		auth_mechanism = "'+am+'"\n'
			if len(amObj["requiredParams"].keys())>0:
				hclStr += '		# ### required ### \n'
			for param in amObj["requiredParams"]:
				paramObj = amObj["requiredParams"][param]
				hclStr += '		'+fmtStr(param)+' = '+renderParamLocalVal(param,paramObj)
				hclStr += ' # '+param+' description: "'+ (paramObj["description"].replace('"','\\\"') if ("description" in paramObj) else "N/A") +'"\n'
			if len(amObj["optionalParams"].keys())>0:
				hclStr += '		# ### optional ### \n'
			for param in amObj["optionalParams"]:
				paramObj = amObj["optionalParams"][param]
				hclStr += '		# '+fmtStr(param)+' = '+renderParamLocalVal(param,paramObj)
				hclStr += ' # '+param+' description: "'+ (paramObj["description"].replace('"','\\\"') if ("description" in paramObj) else "N/A") +'"\n'				
			hclStr += '	}\n'
			hclStr += '}\n\n\n'
	return(hclStr)

def parseRequiredOptionalFields(dataTypeMappings,sourceDataTypeObj,dataType):
	dataTypeMapping = {"optionalParams":{},"requiredParams":{},"auth_mechanism":{}}
	for group in sourceDataTypeObj["groups"]:
		group["attributes"].append({
			"defaultValue": "",
			"description": "Gateway ID",
			"displayName": "Gateway ID",
			"example": "",
			"id": "gateway_id",
			"isEditable": True,
			"isMandatory": True,
			"isVisible": True,
			"type": "str"
		})
		group["attributes"].append({
			"defaultValue": "",
			"description": "Asset ID",
			"displayName": "Asset ID",
			"example": "",
			"id": "asset_id",
			"isEditable": True,
			"isMandatory": True,
			"isVisible": True,
			"type": "str"
		})
		if group["displayName"]=="Details":
			for param in group["attributes"]:
				if param["isMandatory"]:	
					dataTypeMapping["requiredParams"][param["id"].lower()] = parseParam(param)
				else:
					dataTypeMapping["optionalParams"][param["id"].lower()] = parseParam(param)
			if dataType=="databases":
				if "parent_asset_id" in dataTypeMapping["requiredParams"] or "parent_asset_id" in dataTypeMapping["optionalParams"]:
					dataTypeMapping["cloudAccount"]=True
				else:
					dataTypeMapping["cloudAccount"]=False
				if "logs_destination_asset_id" in dataTypeMapping["requiredParams"] or "logs_destination_asset_id" in dataTypeMapping["optionalParams"]:
					dataTypeMapping["logAggregator"]=True
				else:
					dataTypeMapping["logAggregator"]=False
		elif group["displayName"]=="Connection":
			for auth_mechanism in group["attributes"][0]["dependents"]:
				am = {"requiredParams":{},"optionalParams":{}}
				for param in auth_mechanism["attributes"]:
					# hard code this as it is not marked at mandatory
					if param["id"]=="reason":
						param["isMandatory"]=True
					if param["isMandatory"]:
						am["requiredParams"][param["id"].lower()] = parseParam(param)
					else:
						am["optionalParams"][param["id"].lower()] = parseParam(param)
				am["requiredParams"] = sortObject(am["requiredParams"])
				am["optionalParams"] = sortObject(am["optionalParams"])
				dataTypeMapping["auth_mechanism"][auth_mechanism["id"]] = am
	dataTypeMapping["requiredParams"] = sortObject(dataTypeMapping["requiredParams"])
	dataTypeMapping["optionalParams"] = sortObject(dataTypeMapping["optionalParams"])
	dataTypeMappings[sourceDataTypeObj["id"]] = dataTypeMapping
	dataTypeMappings = sortObject(dataTypeMappings)
	return(dataTypeMappings)

def parseParam(curParam):
	newParam = {
		"type":getParamType(curParam["type"]),
		"defaultValue":curParam["defaultValue"],
		"displayName":curParam["displayName"],
		"description":curParam["description"],
		"id":curParam["id"].lower().replace(" ","_")
	}
					
	if type(curParam["example"])==dict:
		newParam["example"] = curParam["example"]
	elif type(curParam["example"])==bool:
		newParam["example"] = curParam["example"]
	elif type(curParam["example"])==int:
		newParam["example"] = curParam["example"]
	else:
		exampleJsonStr = curParam["example"].replace("e.g. ","").replace('\\\"','"')
		newParam["example"] = json.loads(exampleJsonStr) if isJSON(exampleJsonStr) else exampleJsonStr

	if curParam["isMandatory"]:
		newParam["required"] = True
		newParam["optional"] = False
	else: 
		newParam["required"] = False
	if "dependents" in curParam:
		newParam["values"] = []
		for det in curParam["dependents"]:
			newParam["values"].append(det["id"])
	return(newParam)

def renderParamLocalVal(paramName,paramObj):
	paramStr = ""
	if paramObj["defaultValue"]!=None and paramObj["defaultValue"]!="":
		if isinstance(paramObj["defaultValue"], bool):
			paramStr+=str(paramObj["defaultValue"]).lower()
		elif isinstance(paramObj["defaultValue"], int):
			paramStr+=str(paramObj["defaultValue"])
		else:
			paramStr+='"'+paramObj["defaultValue"]+'"'
	else:
		paramStr+='null'
	if "values" in paramObj:
		paramStr += ' # Example Values: "'+'", "'.join(map(str,paramObj["values"]))+'"'
	return paramStr


def renderParamVal(paramName,paramObj):
	paramStr = ""
	if paramObj["defaultValue"]!=None and paramObj["defaultValue"]!="":
		if isinstance(paramObj["defaultValue"], bool):
			paramStr+=str(paramObj["defaultValue"]).lower()
		elif isinstance(paramObj["defaultValue"], int):
			paramStr+=str(paramObj["defaultValue"])
		else:
			paramStr+='"'+paramObj["defaultValue"]+'"'
	else:
		paramStr+='var.'+fmtStr(paramName)
	if "values" in paramObj:
		paramStr += ' # Example Values: "'+'", "'.join(map(str,paramObj["values"]))+'"'
	return paramStr

def getQAMapping():
	dataSourcesMap = {"data":{"assetData":{"connections":[{"connectionData":{}}]}}}
	dataSourcesQA = readFile("data_structures/archive/data_sources_qa.json")
	for ds in dataSourcesQA:
		dsData = ds["data"]
		for paramName in dsData:
			if paramName!="assetData":
				dataSourcesMap["data"][paramName.lower().replace(" ","_")] = pyToTfTypeMap[type(dsData[paramName]).__name__]
		
		dsAssetData = ds["data"]["assetData"]
		for paramName in dsAssetData:
			if paramName!="connections":
				dataSourcesMap["data"]["assetData"][paramName.lower().replace(" ","_")] = pyToTfTypeMap[type(dsAssetData[paramName]).__name__]

		dataSourcesMap["data"]["assetData"]["connections"][0]["reason"] = "string"

		if len(ds["data"]["assetData"]["connections"])>0:
			dsConnData = ds["data"]["assetData"]["connections"][0]["connectionData"]
			for paramName in dsConnData:
				if paramName!="assetData":
					dataSourcesMap["data"]["assetData"]["connections"][0]["connectionData"][paramName.lower().replace(" ","_")] = pyToTfTypeMap[type(dsConnData[paramName]).__name__]

	return(dataSourcesMap)

def renderReadmeParams(dataTypeSchemaMapping):
	str = ""
	for paramName in dataTypeSchemaMapping:
		if paramName != "connections":
			str+=renderReadmeParam(paramName, dataTypeSchemaMapping[paramName],"data.")	
	renderReadmeParam("reason", dataTypeSchemaMapping["connections"][0]["reason"],"data.connections[].")
	for paramName in dataTypeSchemaMapping["connections"][0]["connectionData"]:
		str+=renderReadmeParam(paramName, dataTypeSchemaMapping["connections"][0]["connectionData"][paramName],"data.connections[].connectionData.")
	str += "\n\n"
	return(str)

def renderJsonExample(dataTypeSchemaMapping):
	str = ""
	for paramName in dataTypeSchemaMapping:
		if paramName != "connections":
			str+=renderReadmeParam(paramName, dataTypeSchemaMapping[paramName],"data.")	
	renderReadmeParam("reason", dataTypeSchemaMapping["connections"][0]["reason"],"data.connections[].")
	for paramName in dataTypeSchemaMapping["connections"][0]["connectionData"]:
		str+=renderReadmeParam(paramName, dataTypeSchemaMapping["connections"][0]["connectionData"][paramName],"data.connections[].connectionData.")
	str += "\n\n"
	return(str)


def renderReadmeParam(paramName, paramObj, prefix):	
	paramStr = ""
	required = "required" if paramObj["required"] else "optional"
	paramStr +="`"+prefix+paramName+"` ["+paramObj["type"]+"] - _("+required+")_ "
	paramStr += paramObj["description"]+" " if "description" in paramObj else ""
	if isinstance(paramObj["defaultValue"],object):
		paramStr +=("Default Value: "+(json.dumps(paramObj["defaultValue"])))
	else:
		paramStr +=("Default Value: "+str(paramObj["defaultValue"]) if str(paramObj["defaultValue"])!="" else "")
	
	if "values" in paramObj and paramName!="criticality":
		if len(paramObj["values"])>0:
			paramStr +=' Possible Values: '+('`, `'.join(paramObj["values"]))
	paramStr += "\n\n"
	return(paramStr)


def makeCall(url, method="GET", data=None):
	urllib3.disable_warnings()

	headers = {
		'Accept': 'application/json',
		'Content-Type': 'application/json'
	}
	session = requests.Session()
	session.verify = CACERT_FILE
	session.cert = (CERT_FILE, KEY_FILE)

	if data == None:
		content = None
	else:
		content = data.encode("utf-8")
	try:
		if method == 'POST':
			logging.warning("API REQUEST (" + method + " " + url + ") " + str(content))
			response = session.post(url, content, headers=headers, verify=False, cert=('', ''))
		elif method == 'GET':
			logging.warning("API REQUEST (" + method + " " + url + ") ")
			response = session.get(url, headers=headers, verify=False)
		elif method == 'DELETE':
			logging.warning("API REQUEST (" + method + " " + url + ") ")
			response = session.delete(url, headers=headers, verify=False)
		elif method == 'PUT':
			logging.warning("API REQUEST (" + method + " " + url + ") " + str(content))
			response = session.put(url, content, headers=headers, verify=False)
		if response.status_code == 404:
			logging.warning("API ERROR (" + method + " " + url + ") status code: "+str(response.status_code))
		elif response.status_code != 200:
			logging.warning("API ERROR (" + method + " " + url + ") "+str(response.status_code)+" | response: "+json.dumps(response.json()))
		else:
			logging.warning("API RESPONSE (" + method + " " + url + ") status code: "+str(response.status_code))
		return response
	except Exception as e:
		logging.warning("ERROR - "+str(e))

def readFile(filename):
	with open(filename, 'r') as content_file:
		return(json.loads(content_file.read()))

def writeFile(filename,data):
	open(filename, 'w+').close()
	csv_file=open(filename,"w+")
	csv_file.write(data)
	csv_file.close()

def getParamType(paramType):
	match paramType:
		case "secured":
			paramType="string"
		case "boolean":
			paramType="bool"
		case "dict":
			paramType="map"
		case "options":
			paramType="options"
		case _:
			paramType = "string"
	return(paramType)

def fmtStr(str):
	return(str.lower().replace(" ","_"))

def fmtFieldKey(str):
	str = sub(r"(_|-)+", " ", str).title().replace(" ", "")
	str = str.replace("Id","ID").replace("id","ID").replace("Ip","IP")
	return str

def getParamSchemaType(paramType,paramObj):
	match paramType:
		case "secured":
			paramType="schema.TypeString"
		case "boolean":
			paramType="schema.TypeBool"
		case "dict":
			paramType="schema.TypeSet"
		case "options":
			paramType="schema.TypeSet"
		case "int":
			paramType="schema.TypeInt"
		case "map":
			if "values" in paramObj:
				if isinstance(paramObj["values"][0], int):
					paramType="schema.TypeInt"
				else:
					paramType="schema.TypeString"
			else: 
				paramType="schema.TypeString"
		case _:
			paramType = "schema.TypeString"
	return(paramType)

def sortObject(sourceObj):
	objSortedKeys = {}
	objSortedKeys = list(sourceObj.keys())
	objSortedKeys.sort()
	sourceObj = {i: sourceObj[i] for i in objSortedKeys}
	return(sourceObj)


def isJSON(jsonstr):
    try:
        json_object = json.loads(jsonstr)
    except ValueError as e:
        return False
    return True