import fnmatch,json,logging,re,threading
from typing import Optional
from jsonschema import ValidationError,validate
from localstack.http import Request,Response
from outages.config import OUTAGE_CONFIG
from outages.constants import CONFIG_JSON_SCHEMA
LOG=logging.getLogger(__name__)
OUTAGE_CONFIG_LOCK=threading.Lock()
def validate_request(request):
	C='error'
	try:
		D=json.loads(request.data);validate(instance=D,schema=CONFIG_JSON_SCHEMA)
		for E in D:re.compile(fnmatch.translate(E['service']));re.compile(fnmatch.translate(E['region']))
	except json.JSONDecodeError as B:A=f"Error decoding JSON: {B}";LOG.debug(A);return Response.for_json({C:A},status=400)
	except ValidationError as B:A=f"Error validating JSON schema: {B.message}";LOG.debug(A);return Response.for_json({C:A},status=400)
	except re.error as B:A=f"Invalid regex: {B.msg}";LOG.debug(A);return Response.for_json({C:A},status=400)
def handle_get_config(request,**A):return Response.for_json(OUTAGE_CONFIG,status=200)
def handle_post_config(request,**E):
	A=request
	if(B:=validate_request(A)):return B
	C=json.loads(A.data)
	with OUTAGE_CONFIG_LOCK:
		OUTAGE_CONFIG.clear()
		for D in C:OUTAGE_CONFIG.append(D)
	return Response.for_json(OUTAGE_CONFIG,status=200)
def handle_delete_config(request,**E):
	A=request
	if(C:=validate_request(A)):return C
	D=json.loads(A.data)
	with OUTAGE_CONFIG_LOCK:
		for B in D:
			if B in OUTAGE_CONFIG:OUTAGE_CONFIG.remove(B)
	return Response.for_json(OUTAGE_CONFIG,status=200)
def handle_patch_config(request,**E):
	A=request
	if(C:=validate_request(A)):return C
	D=json.loads(A.data)
	with OUTAGE_CONFIG_LOCK:
		for B in D:
			if B not in OUTAGE_CONFIG:OUTAGE_CONFIG.append(B)
		return Response.for_json(OUTAGE_CONFIG,status=200)