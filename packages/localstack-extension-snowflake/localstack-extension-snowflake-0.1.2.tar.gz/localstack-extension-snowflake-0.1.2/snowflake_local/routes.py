_I='type'
_H='value'
_G='test'
_F='data'
_E='status_code'
_D='name'
_C='success'
_B='POST'
_A=True
import gzip,json,logging,re
from typing import Any
from localstack.aws.connect import connect_to
from localstack.http import Request,Response,route
from localstack.utils.strings import to_str
from localstack_ext.services.rds.engine_postgres import get_type_name
from snowflake_local.constants import PATH_QUERIES,PATH_SESSION,PATH_V1_STREAMING
from snowflake_local.conversions import to_pyarrow_table_bytes_b64
from snowflake_local.encodings import get_parquet_from_blob
from snowflake_local.files.file_ops import handle_copy_into_query,handle_put_file_query
from snowflake_local.files.staging import get_stage_s3_location
from snowflake_local.models import QueryResponse
from snowflake_local.queries import execute_query,insert_rows_into_table
from snowflake_local.storage import FileRef
LOG=logging.getLogger(__name__)
REGEX_FILE_FORMAT='\\s*(CREATE|DROP)\\s+.*FILE\\s+FORMAT\\s+(?:IF\\s+NOT\\s+EXISTS\\s+)?(.+)(\\s+TYPE\\s+=(.+))?'
TMP_UPLOAD_STAGE='@tmp-stage-internal'
ENCRYPTION_KEY=_G
class RequestHandler:
	@route(PATH_SESSION,methods=[_B])
	def session_request(self,request,**B):
		if request.args.get('delete')=='true':LOG.info('Deleting session data...')
		A={_C:_A};return Response.for_json(A,status=200)
	@route(f"{PATH_SESSION}/v1/login-request",methods=[_B])
	def session_login(self,request,**B):A={_F:{'nextAction':None,'token':'token123','masterToken':'masterToken123','parameters':[{_D:'AUTOCOMMIT',_H:_A}]},_C:_A};return Response.for_json(A,status=200)
	@route(f"{PATH_QUERIES}/query-request",methods=[_B])
	def start_query(self,request,**H):
		B=_get_data(request);E=B.get('sqlText','');F=B.get('bindings',{});C=[]
		for G in range(1,100):
			D=F.get(str(G))
			if not D:break
			C.append(D.get(_H))
		A=handle_query_request(E,C);A=A.to_dict();return Response.for_json(A,status=200)
	@route(f"{PATH_QUERIES}/abort-request",methods=[_B])
	def abort_query(self,request,**A):return{_C:_A}
	@route(f"{PATH_V1_STREAMING}/client/configure",methods=[_B])
	def streaming_configure_client(self,request,**D):A=FileRef.parse(TMP_UPLOAD_STAGE);B=get_stage_s3_location(A);C={_C:_A,_E:0,'prefix':_G,'deployment_id':_G,'stage_location':B,_F:{}};return C
	@route(f"{PATH_V1_STREAMING}/channels/open",methods=[_B])
	def streaming_open_channel(self,request,**H):F='VARIANT';E='BINARY';D='variant';C='logical_type';B='physical_type';G=_get_data(request);A={_C:_A,_E:0,'client_sequencer':1,'row_sequencer':1,'encryption_key':ENCRYPTION_KEY,'encryption_key_id':123,'table_columns':[{_D:'record_metadata',_I:D,B:E,C:F},{_D:'record_content',_I:D,B:E,C:F}],_F:{}};A.update(G);return A
	@route(f"{PATH_V1_STREAMING}/channels/status",methods=[_B])
	def streaming_channel_status(self,request,**B):A={_C:_A,_E:0,'message':'test channel','channels':[{_E:0,'persisted_row_sequencer':1,'persisted_client_sequencer':1,'persisted_offset_token':'1'}]};return A
	@route(f"{PATH_V1_STREAMING}/channels/write/blobs",methods=[_B])
	def streaming_channel_write_blobs(self,request,**T):
		H='blobs';D='/';I=_get_data(request);J=FileRef.parse(TMP_UPLOAD_STAGE);K=get_stage_s3_location(J)['location'];E=[]
		for A in I.get(H,[]):
			B=A.get('path')or D;L=B if B.startswith(D)else f"/{B}";M=K+L;N,U,O=M.partition(D);P=connect_to().s3;C=P.get_object(Bucket=N,Key=O);Q=C['Body'].read()
			try:R=get_parquet_from_blob(Q,key=ENCRYPTION_KEY,blob_path=B)
			except Exception as S:LOG.warning('Unable to parse parquet from blob: %s - %s',A,S);continue
			F=A.get('chunks')or[]
			if not F:LOG.info('Chunks information missing in incoming blob: %s',A)
			for G in F:insert_rows_into_table(table=G['table'],database=G['database'],rows=R)
			E.append({})
		C={_C:_A,_E:0,H:E};return C
	@route('/telemetry/send/sessionless',methods=[_B])
	def send_telemetry_sessionless(self,request,**B):A={_C:_A,_F:{}};return A
def handle_query_request(query,params):
	B=query;A=QueryResponse();A.data.parameters.append({_D:'TIMEZONE',_H:'UTC'});B=B.strip(' ;');H=re.match('^\\s*PUT\\s+.+',B,flags=re.IGNORECASE)
	if H:return handle_put_file_query(B,A)
	I=re.match('^\\s*COPY\\s+INTO\\s.+',B,flags=re.IGNORECASE)
	if I:return handle_copy_into_query(B,A)
	J=re.match('^\\s*CREATE\\s+WAREHOUSE\\s.+',B,flags=re.IGNORECASE)
	if J:return A
	K=re.match('^\\s*USE\\s.+',B,flags=re.IGNORECASE)
	if K:return A
	L=re.match('^\\s*CREATE\\s+STORAGE\\s.+',B,flags=re.IGNORECASE)
	if L:return A
	M=re.match(REGEX_FILE_FORMAT,B,flags=re.IGNORECASE)
	if M:return A
	C=execute_query(B,params)
	if C and C._context.columns:
		D=[];N=C._context.columns
		for O in C:D.append(list(O))
		F=[]
		for E in N:F.append({_D:E[_D],_I:get_type_name(E['type_oid']),'length':E['type_size'],'precision':0,'scale':0,'nullable':_A})
		A.data.rowset=D;A.data.rowtype=F;A.data.total=len(D)
	G=re.match('.+FROM\\s+@',B);A.data.queryResultFormat='arrow'if G else'json'
	if G:A.data.rowsetBase64=to_pyarrow_table_bytes_b64(A);A.data.rowset=[];A.data.rowtype=[]
	return A
def _get_data(request):
	A=request.data
	if isinstance(A,bytes):
		try:A=gzip.decompress(A)
		except gzip.BadGzipFile:pass
		A=json.loads(to_str(A))
	return A