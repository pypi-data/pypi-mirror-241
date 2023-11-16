import base64,logging,re
from localstack.utils.strings import to_bytes,to_str,truncate
from simple_ddl_parser import DDLParser
from snowflake_local.db_server import start_postgres
LOG=logging.getLogger(__name__)
def execute_query(query,params,database=None):
	B=params;A=query;D=start_postgres();A=fix_query(A,B);LOG.debug('Running query: %s - %s',A,B)
	try:return D.run_query(A,*B,database=database)
	except Exception as C:
		if'already exists'in str(C):
			if'database'in str(C):return
			if'relation'in str(C):E=re.match('.*relation \\"(.+)\\" already exists',str(C)).group(1);D.run_query(f"DROP TABLE {E}",*B);return D.run_query(A,*B)
		raise
def fix_query(query,params):
	C=params;A=query;A=A.replace('\n',' ')
	def B(search,replace):return re.sub(search,replace,A,flags=re.IGNORECASE)
	if _is_create_table_query(A):A=B('(.+\\s)string(\\s*[,)].*)','\\1text\\2')
	A=B('^\\s*CREATE\\s+DATABASE\\s+IF\\s+NOT\\s+EXISTS','CREATE DATABASE');A=B('^\\s*CREATE\\s+OR\\s+REPLACE\\s+TABLE','CREATE TABLE');A=B('::\\s*VARIANT','');A=B('\\s+VARIANT',' TEXT');A=B('\\s+IDENTIFIER\\s*\\(([^\\)]+)\\)',' \\1');A=B('^\\s*DESC(RIBE)?\\s+TABLE\\s+([^\\)\\s]+)','SELECT * FROM information_schema.columns WHERE table_name=\\2');A=_create_tmp_table_for_file_queries(A);A=B('([\\(,\\s=<>])\\?([\\),\\s]|$)','\\1%s\\2')
	if _is_create_table_query(A)and C:A=A%tuple(C);C.clear()
	return A
def insert_rows_into_table(table,rows,schema=None,database=None):
	I=database;H=schema;G=table;F=', ';A=rows;J=f'"{H}"."{G}"'if H else G
	if A and isinstance(A[0],dict):
		B=set()
		for C in A:B.update(C.keys())
		B=list(B);K=F.join(B);D=F.join(['%s'for A in B]);E=f"INSERT INTO {J} ({K}) VALUES ({D})"
		for C in A:L=[C.get(A)for A in B];execute_query(E,list(L),database=I)
	elif A and isinstance(A[0],(list,tuple)):
		for C in A:M=len(C);D=F.join(['%s'for A in range(M)]);E=f"INSERT INTO {J} VALUES ({D})";execute_query(E,list(C),database=I)
	elif A:raise Exception(f"Unexpected values when storing list of rows to table: {truncate(str(A))}")
def _is_create_table_query(query):
	A=DDLParser(query).run()
	if not A:return False
	return bool(A[0].get('table_name')and not A[0].get('alter'))
def _create_tmp_table_for_file_queries(query):
	A=query;C='(\\s*SELECT\\s+.+\\sFROM\\s+)(@[^\\(\\s]+)(\\s*\\([^\\)]+\\))?';F=re.match(C,A)
	if not F:return A
	G=re.findall('\\$\\d+',A);D='_col1 TEXT';B=[int(A.removeprefix('$'))for A in G]
	if B:H=list(range(1,max(B)+1));D=','.join([f"_col{A} TEXT"for A in H])
	def I(match):A=match;B=to_str(base64.b64encode(to_bytes(A.group(3)or'')));return f"{A.group(1)} load_data('{A.group(2)}', '{B}') as _tmp({D})"
	A=re.sub(C,I,A)
	if B:
		for E in range(max(B),0,-1):A=A.replace(f"${E}",f"_col{E}")
	return A