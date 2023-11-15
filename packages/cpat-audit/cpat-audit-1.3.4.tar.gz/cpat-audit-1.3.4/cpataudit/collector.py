import logging, os , pytz, json
from rq import Queue
from cpataudit.auditoria import Auditoria

from flask import request
from datetime import datetime
import redis
from functools import wraps

logger = logging.getLogger(__name__)

TIME_ZONE = os.getenv('TIME_ZONE','Chile/Continental')
TIME_FORMAT = os.getenv('TIME_FORMAT',"%Y-%m-%dT%H:%M:%S+03:00")
santiagoTz = pytz.timezone(TIME_ZONE)

HOST_HEADER_NAME = os.getenv('HOST_HEADER_NAME', 'host')


class CollectorException(Exception):
    pass

def register_record(queue,record):
    auditoria = Auditoria()
    try:
        task = queue.enqueue(
            auditoria.save_audit_register,
            record, 
            job_timeout=os.getenv('JOB_TIME_OUT',1800), 
            result_ttl=os.environ.get('JOB_TTL_TIME', 5000)
        )
        logger.debug(task.id)
    except Exception as e:
        logger.exception(e)
        logger.warning('El registro no se ha procesado.')
        logger.warning(record)


class AuditContext(object):

    def __init__(self, queue_name, redis_host = 'redis',redis_port=6379):
        self.queue_name = queue_name
        host = os.getenv('REDIS_HOST', redis_host)
        port = os.getenv('REDIS_PORT',redis_port)
        logger.info(f'Conectando a redis {host}:{port}')
        conn = redis.Redis(host=host, port=port)

        # Cola de tareas (tasks)
        self._queue = Queue(queue_name,connection=conn)

    
    ACTION_MAP = {
        "POST": "crear",
        "GET": "leer",
        "PATCH": "modificar",
        "DELETE": "borrar",
        "PUT" : "actualizar",
    }

    def _create_record(self, request, seccion, request_method):
        detalle_data = None
        try:
            detalle_data = request.data.decode('utf-8')
            detalle_dict = json.loads(detalle_data)
        except (UnicodeDecodeError, json.JSONDecodeError):
            detalle_dict = {}

        detalle_json_str = json.dumps(detalle_dict, ensure_ascii=False, single_quote=True)


        record = {
            "usuario_id": request.headers.get('rut'),
            "institucion_id" : request.headers.get('oae'),
            "seccion" : seccion + '/' + self.ACTION_MAP[request_method],
            "accion" : self.ACTION_MAP[request_method],
            "status" : "ok",
            "periodo_id" :1,
            "nombre_periodo" :"",
            "registro_afectado": 1,
            "detalle": detalle_json_str,
            "direccion_ip": request.headers[HOST_HEADER_NAME],
            "fecha_creacion": datetime.now(santiagoTz).strftime(TIME_FORMAT)
        } 
        return record


    def web_audit(self, seccion, method_to_filter: list = []):

        def decorator(func):
            logger.debug(f'Func decorator: {func}')
            @wraps(func)
            def wrapper(*args,**kwargs):

                # Check if request method is in method_to_filter
                flag_method = False
                request_method = request.method
                logger.warning(f'Se recibió método {request_method}')
                if request_method in method_to_filter:
                    flag_method = True

                logger.debug(f'Headers: {request.headers}')
                logger.debug(request.data)
    
                # Check flag_method
                if not flag_method:
                    record = self._create_record(request, seccion=seccion, request_method=request_method)
                    logger.debug(f'Registro creado: {record}')

                error = False
                try:
                    return func(*args,**kwargs)
                except Exception:
                    error = True
                    logger.exception('La ejeucución de la operación a encontrado un error')
                    raise
                finally:
                    #No se registra nada acá, por que ya se ha registrado en el bloque except
                    if error:
                        record['estatus'] = 'error'
                    if not flag_method:
                        logger.info('Adding to queue')
                        register_record(self._queue,record)
            
            return wrapper
        return decorator 
