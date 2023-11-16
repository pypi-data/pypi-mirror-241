_A='test'
import time
from localstack.utils.net import get_free_tcp_port,wait_for_port_open
from localstack_ext.utils.postgresql import Postgresql
class State:server=None
def start_postgres(user=_A,password=_A,database=_A):
	if not State.server:
		A=get_free_tcp_port();State.server=Postgresql(port=A,user=user,password=password,database=database,boot_timeout=30,include_python_venv_libs=True);time.sleep(1)
		try:B=20;wait_for_port_open(A,retries=B,sleep_time=.8)
		except Exception:raise Exception('Unable to start up Postgres process (health check failed after 10 secs)')
		define_util_functions(State.server)
	return State.server
def define_util_functions(server):A=server;A.run_query('CREATE EXTENSION IF NOT EXISTS plpython3u');B='\n    CREATE OR REPLACE FUNCTION parse_json (\n       content text\n    ) RETURNS text\n    LANGUAGE plpython3u IMMUTABLE\n    AS $$\n        return content\n    $$;\n    ';A.run_query(B);B='\n    CREATE OR REPLACE FUNCTION load_data (\n       file_ref text,\n       file_format text\n    ) RETURNS SETOF RECORD\n    LANGUAGE plpython3u IMMUTABLE\n    AS $$\n        from snowflake_local.extension_functions import load_data\n        return load_data(file_ref, file_format)\n    $$;\n    ';A.run_query(B)