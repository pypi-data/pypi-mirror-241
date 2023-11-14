# Endpoints

## projects
ENDPOINT_URL_PROJECTS_ALL = "/api/nemo-projects/projects"

ENDPOINT_URL_PROJECTS_FILE_RE_UPLOAD_INITIALIZE = "/api/nemo-projects/file-re-upload/initialize"
ENDPOINT_URL_PROJECTS_FILE_RE_UPLOAD_KEEP_ALIVE = "/api/nemo-projects/projects/{projectId}/upload/{uploadId}/keep-alive"
ENDPOINT_URL_PROJECTS_FILE_RE_UPLOAD_FINALIZE ="/api/nemo-projects/file-re-upload/finalize"
ENDPOINT_URL_PROJECTS_FILE_RE_UPLOAD_ABORT = "/api/nemo-projects/file-re-upload/abort"

## meta data
ENDPOINT_URL_PERSISTENCE_PROJECT_PROPERTIES = "/api/nemo-persistence/ProjectProperty/{request}"
ENDPOINT_URL_PERSISTENCE_METADATA_IMPORTED_COLUMNS = "/api/nemo-persistence/metadata/Columns/project/{projectId}/exported"
ENDPOINT_URL_PERSISTENCE_METADATA_SET_COLUMN_PROPERTIES = "/api/nemo-persistence/metadata/Columns/{id}"
ENDPOINT_URL_PERSISTENCE_METADATA_CREATE_IMPORTED_COLUMN = "/api/nemo-persistence/metadata/Columns"
ENDPOINT_URL_PERSISTENCE_METADATA_DELETE_IMPORTED_COLUMN = "/api/nemo-persistence/metadata/Columns/{id}"

## reports
ENDPOINT_URL_REPORT_RESULT = "/api/nemo-report/report_results"
FILE_UPLOAD_CHUNK_SIZE = 5 * 1024 * 1024  # 5MB


## queue
ENDPOINT_URL_QUEUE_INGEST_DATA_V2 = "/api/nemo-queue/ingest_data_kubernetes_v2"
ENDPOINT_URL_QUEUE_TASK_RUNS  = "/api/nemo-queue/task_runs"

##  RESERVED KEY WORDS
RESERVED_KEYWORDS = [
        "abort", "abortsession", "abs", "absolute", "access", "accessible",
        "access_lock", "account", "acos", "acosh", "action", "add", "add_months", "admin", "after", "aggregate",
        "alias", "all", "allocate", "allow", "alter", "alterand", "amp", "analyse", "analyze", "and", "ansidate", "any",
        "are", "array", "array_agg", "array_exists", "array_max_cardinality", "as", "asc", "asensitive", "asin",
        "asinh", "assertion", "associate", "asutime", "asymmetric", "at", "atan", "atan2", "atanh", "atomic", "audit",
        "authorization", "aux", "auxiliary", "ave", "average", "avg", "backup", "before", "begin", "begin_frame",
        "begin_partition", "between", "bigint", "binary", "bit", "blob", "boolean", "both", "breadth", "break",
        "browse", "bt", "bufferpool", "bulk", "but", "by", "byte", "byteint", "bytes", "call", "called", "capture",
        "cardinality", "cascade", "cascaded", "case", "casespecific", "case_n", "cast", "catalog", "ccsid", "cd",
        "ceil", "ceiling", "change", "char", "char2hexint", "character", "characters", "character_length", "chars",
        "char_length", "check", "checkpoint", "class", "classifier", "clob", "clone", "close", "cluster", "clustered",
        "cm", "coalesce", "collate", "collation", "collect", "collection", "collid", "column", "column_value",
        "comment", "commit", "completion", "compress", "compute", "concat", "concurrently", "condition", "connect",
        "connection", "constraint", "constraints", "constructor", "contains", "containstable", "content", "continue",
        "convert", "convert_table_header", "copy", "corr", "corresponding", "cos", "cosh", "count", "covar_pop",
        "covar_samp", "create", "cross", "cs", "csum", "ct", "cube", "cume_dist", "current", "current_catalog",
        "current_date", "current_default_transform_group", "current_lc_ctype", "current_path", "current_role",
        "current_row", "current_schema", "current_server", "current_time", "current_timestamp", "current_timezone",
        "current_transform_group_for_type", "current_user", "currval", "cursor", "cv", "cycle", "data", "database",
        "databases", "datablocksize", "date", "dateform", "day", "days", "day_hour", "day_microsecond", "day_minute",
        "day_second", "dbcc", "dbinfo", "deallocate", "dec", "decfloat", "decimal", "declare", "default", "deferrable",
        "deferred", "define", "degrees", "del", "delayed", "delete", "dense_rank", "deny", "depth", "deref", "desc",
        "describe", "descriptor", "destroy", "destructor", "deterministic", "diagnostic", "diagnostics", "dictionary",
        "disable", "disabled", "disallow", "disconnect", "disk", "distinct", "distinctrow", "distributed", "div", "do",
        "document", "domain", "double", "drop", "dssize", "dual", "dump", "dynamic", "each", "echo", "editproc",
        "element", "else", "elseif", "empty", "enabled", "enclosed", "encoding", "encryption", "end", "end-exec",
        "ending", "end_frame", "end_partition", "eq", "equals", "erase", "errlvl", "error", "errorfiles", "errortables",
        "escape", "escaped", "et", "every", "except", "exception", "exclusive", "exec", "execute", "exists", "exit",
        "exp", "explain", "external", "extract", "fallback", "false", "fastexport", "fenced", "fetch", "fieldproc",
        "file", "fillfactor", "filter", "final", "first", "first_value", "float", "float4", "float8", "floor", "for",
        "force", "foreign", "format", "found", "frame_row", "free", "freespace", "freetext", "freetexttable", "freeze",
        "from", "full", "fulltext", "function", "fusion", "ge", "general", "generated", "get", "give", "global", "go",
        "goto", "grant", "graphic", "group", "grouping", "groups", "gt", "handler", "hash", "hashamp", "hashbakamp",
        "hashbucket", "hashrow", "having", "help", "high_priority", "hold", "holdlock", "host", "hour", "hours",
        "hour_microsecond", "hour_minute", "hour_second", "identified", "identity", "identitycol", "identity_insert",
        "if", "ignore", "ilike", "immediate", "in", "inclusive", "inconsistent", "increment", "index", "indicator",
        "infile", "inherit", "initial", "initialize", "initially", "initiate", "inner", "inout", "input", "ins",
        "insensitive", "insert", "instead", "int", "int1", "int2", "int3", "int4", "int8", "integer", "integerdate",
        "intersect", "intersection", "interval", "into", "io_after_gtids", "io_before_gtids", "is", "isnull", "isobid",
        "isolation", "iterate", "jar", "join", "journal", "json_array", "json_arrayagg", "json_exists", "json_object",
        "json_objectagg", "json_query", "json_table", "json_table_primitive", "json_value", "keep", "key", "keys",
        "kill", "kurtosis", "label", "lag", "language", "large", "last", "last_value", "lateral", "lc_ctype", "le",
        "lead", "leading", "leave", "left", "less", "level", "like", "like_regex", "limit", "linear", "lineno", "lines",
        "listagg", "ln", "load", "loading", "local", "locale", "localtime", "localtimestamp", "locator", "locators",
        "lock", "locking", "lockmax", "locksize", "log", "log10", "logging", "logon", "long", "longblob", "longtext",
        "loop", "lower", "low_priority", "lt", "macro", "maintained", "map", "master_bind",
        "master_ssl_verify_server_cert", "match", "matches", "match_number", "match_recognize", "materialized", "mavg",
        "max", "maxextents", "maximum", "maxvalue", "mcharacters", "mdiff", "mediumblob", "mediumint", "mediumtext",
        "member", "merge", "method", "microsecond", "microseconds", "middleint", "min", "mindex", "minimum", "minus",
        "minute", "minutes", "minute_microsecond", "minute_second", "mlinreg", "mload", "mlslabel", "mod", "mode",
        "modifies", "modify", "module", "monitor", "monresource", "monsession", "month", "months", "msubstr", "msum",
        "multiset", "named", "names", "national", "natural", "nchar", "nclob", "ne", "nested_table_id", "new",
        "new_table", "next", "nextval", "no", "noaudit", "nocheck", "nocompress", "nonclustered", "none", "normalize",
        "not", "notnull", "nowait", "no_write_to_binlog", "nth_value", "ntile", "null", "nullif", "nullifzero", "nulls",
        "number", "numeric", "numparts", "obid", "object", "objects", "occurrences_regex", "octet_length", "of", "off",
        "offline", "offset", "offsets", "old", "old_table", "omit", "on", "one", "online", "only", "open",
        "opendatasource", "openquery", "openrowset", "openxml", "operation", "optimization", "optimize",
        "optimizer_costs", "option", "optionally", "or", "order", "ordinality", "organization", "out", "outer",
        "outfile", "output", "over", "overlaps", "overlay", "override", "package", "pad", "padded", "parameter",
        "parameters", "part", "partial", "partition", "partitioned", "partitioning", "password", "path", "pattern",
        "pctfree", "per", "percent", "percentile_cont", "percentile_disc", "percent_rank", "period", "perm",
        "permanent", "piecesize", "pivot", "placing", "plan", "portion", "position", "position_regex", "postfix",
        "power", "precedes", "precision", "prefix", "preorder", "prepare", "preserve", "prevval", "primary", "print",
        "prior", "priqty", "private", "privileges", "proc", "procedure", "profile", "program", "proportional",
        "protection", "psid", "ptf", "public", "purge", "qualified", "qualify", "quantile", "query", "queryno",
        "radians", "raiserror", "random", "range", "range_n", "rank", "raw", "read", "reads", "readtext", "read_write",
        "real", "reconfigure", "recursive", "ref", "references", "referencing", "refresh", "regexp", "regr_avgx",
        "regr_avgy", "regr_count", "regr_intercept", "regr_r2", "regr_slope", "regr_sxx", "regr_sxy", "regr_syy",
        "relative", "release", "rename", "repeat", "replace", "replication", "repoverride", "request", "require",
        "resignal", "resource", "restart", "restore", "restrict", "result", "result_set_locator", "resume", "ret",
        "retrieve", "return", "returning", "returns", "revalidate", "revert", "revoke", "right", "rights", "rlike",
        "role", "rollback", "rollforward", "rollup", "round_ceiling", "round_down", "round_floor", "round_half_down",
        "round_half_even", "round_half_up", "round_up", "routine", "row", "rowcount", "rowguidcol", "rowid", "rownum",
        "rows", "rowset", "row_number", "rule", "run", "running", "sample", "sampleid", "save", "savepoint", "schema",
        "schemas", "scope", "scratchpad", "scroll", "search", "second", "seconds", "second_microsecond", "secqty",
        "section", "security", "securityaudit", "seek", "sel", "select", "semantickeyphrasetable",
        "semanticsimilaritydetailstable", "semanticsimilaritytable", "sensitive", "separator", "sequence", "session",
        "session_user", "set", "setresrate", "sets", "setsessrate", "setuser", "share", "show", "shutdown", "signal",
        "similar", "simple", "sin", "sinh", "size", "skew", "skip", "smallint", "some", "soundex", "source", "space",
        "spatial", "specific", "specifictype", "spool", "sql", "sqlexception", "sqlstate", "sqltext", "sqlwarning",
        "sql_big_result", "sql_calc_found_rows", "sql_small_result", "sqrt", "ss", "ssl", "standard", "start",
        "starting", "startup", "state", "statement", "static", "statistics", "stay", "stddev_pop", "stddev_samp",
        "stepinfo", "stogroup", "stored", "stores", "straight_join", "string_cs", "structure", "style", "submultiset",
        "subscriber", "subset", "substr", "substring", "substring_regex", "succeeds", "successful", "sum", "summary",
        "suspend", "symmetric", "synonym", "sysdate", "system", "system_time", "system_user", "systimestamp", "table",
        "tablesample", "tablespace", "tan", "tanh", "tbl_cs", "temporary", "terminate", "terminated", "textsize",
        "than", "then", "threshold", "time", "timestamp", "timezone_hour", "timezone_minute", "tinyblob", "tinyint",
        "tinytext", "title", "to", "top", "trace", "trailing", "tran", "transaction", "translate", "translate_chk",
        "translate_regex", "translation", "treat", "trigger", "trim", "trim_array", "true", "truncate", "try_convert",
        "tsequal", "type", "uc", "uescape", "uid", "undefined", "under", "undo", "union", "unique", "unknown", "unlock",
        "unnest", "unpivot", "unsigned", "until", "upd", "update", "updatetext", "upper", "uppercase", "usage", "use",
        "user", "using", "utc_date", "utc_time", "utc_timestamp", "validate", "validproc", "value", "values",
        "value_of", "varbinary", "varbyte", "varchar", "varchar2", "varcharacter", "vargraphic", "variable", "variadic",
        "variant", "varying", "var_pop", "var_samp", "vcat", "verbose", "versioning", "view", "virtual", "volatile",
        "volumes", "wait", "waitfor", "when", "whenever", "where", "while", "width_bucket", "window", "with", "within",
        "within_group", "without", "wlm", "work", "write", "writetext", "xmlcast", "xmlexists", "xmlnamespaces", "xor",
        "year", "years", "year_month", "zerofill", "zeroifnull", "zone", "frequency"
    ]