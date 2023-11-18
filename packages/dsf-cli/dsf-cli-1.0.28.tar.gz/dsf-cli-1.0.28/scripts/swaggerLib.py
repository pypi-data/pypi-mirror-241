import json
import requests
import base64
import logging
from time import localtime, strftime
from requests.packages import urllib3
import os
from re import sub

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
	"store_aws_credentials":True,
	"subscription_id":True,
	"url":True,
	"v2_key_engine":True
}

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