from localstack.aws.api import ServiceException
class ServiceUnavailableException(ServiceException):code='ServiceUnavailableException';sender_fault=False;status_code=503;retryAfterSeconds='10'