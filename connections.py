
from sqlalchemy import create_engine


print('Establish connections')

_local = create_engine('oracle+cx_oracle://loan:loan@localhost:1521/XE')

_sit = create_engine('oracle+cx_oracle://loan:SPrDDSAmAn0003031@172.17.5.52:1521/cbstest')


source = _local
destination = _local
defult_engine = _local