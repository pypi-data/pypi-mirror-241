import sqlglot
from sqlglot.optimizer.qualify import qualify
from sqlglot.optimizer.qualify_tables import qualify_tables
import sqlparse as sqlparse


def process_query(query, read, case_sensitive, quote_identifiers):
    expression = sqlglot.parse_one(query, read=read)

    if case_sensitive == '1':
        return qualify_tables(expression, case_sensitive=True).sql() + ';'
    elif case_sensitive == '2':
        return qualify_tables(expression, case_sensitive=False).sql() + ';'
    elif quote_identifiers:
        return qualify(expression, quote_identifiers=False).sql() + ';'
    else:
        return query + ';'


def main(sql_query, read, write, source, case_sensitive, quote_identifiers):
    result = ''
    queries = sqlglot.transpile(sql_query, read=read, write=write)
    if source == 'text':
        if case_sensitive =='0' and quote_identifiers == False:
            result = sqlparse.format(queries[0], reindent_aligned=True) + ";"
        else:
            result = sqlparse.format(process_query(sql_query, read, case_sensitive, quote_identifiers), reindent_aligned=True)

    elif source == 'file':
        if case_sensitive == '0' and quote_identifiers == False:
            result = sqlparse.format(';'.join(queries), reindent=True)
        else:
            queries = sql_query.split(';')
            result = sqlparse.format(''.join(process_query(query, read, case_sensitive, quote_identifiers) for query in queries), reindent=True)
    else:
        print("Invalid method specified.")

    print(result)





sql = """
SELECT '1'::json;
"""


main(sql, "postgres", "doris", 'text', '0', False)