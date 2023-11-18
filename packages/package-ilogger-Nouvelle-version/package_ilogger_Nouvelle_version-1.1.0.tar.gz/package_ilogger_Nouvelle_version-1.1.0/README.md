# Titre de mon Projet
Yon pwojè Python ki la pou kreye lòg nan yon fichye error.log si se yon log erè, oubyen warning.log si se nan yon lòg atansyon.

from ilogger import log
log("<MESAJ>", LEVEL)
LEVEL la kapab (ERROR, WARNING)

from ilogger import get_logs

get_logs(ERROR) 
# ki ap afiche tout lòg erè yo nan stil sa:
# ERROR: [12/12/2023 12:23:03] <MESAJ>
# ERROR: [12/12/2023 11:04:23] <MESAJ>

get_logs(WARNING) ki ap afiche tout lòg atansyon yo
KONTRENT:

Mesaj la pa dwe depase 100 karaktè
2 tip levèl sèlman, ERROR, WARNING
Pou w afiche lòg yo, se sèlman fichye ki gen ekstansyon .log epi ki respekte fòma ou anrejistre yo a.
