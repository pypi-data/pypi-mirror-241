import fnmatch,logging
from localstack.aws.api import RequestContext
from localstack.aws.chain import Handler,HandlerChain
from localstack.http import Response
from outages.config import OUTAGE_CONFIG
from outages.exceptions import ServiceUnavailableException
LOG=logging.getLogger(__name__)
class OutageHandler(Handler):
	def __call__(F,chain,context,response):
		A=context
		if A.is_internal_call:return
		for(E,B)in enumerate(OUTAGE_CONFIG):
			C=B['service'];D=B['region']
			if fnmatch.fnmatchcase(A.region,D)and fnmatch.fnmatchcase(A.service.service_name,C):LOG.debug(f"Outage config rule #{E} match: service '{C}', region '{D}'");raise ServiceUnavailableException(f"Service '{A.service.service_name}' not accessible in '{A.region}' region due to an outage")