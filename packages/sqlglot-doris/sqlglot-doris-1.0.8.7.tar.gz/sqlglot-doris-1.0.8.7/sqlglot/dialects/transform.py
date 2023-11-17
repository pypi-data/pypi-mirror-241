import sqlglot
from sqlglot.optimizer.qualify import qualify
from sqlglot.optimizer.qualify_tables import qualify_tables
import sqlparse as sqlparse

def process_query(query, read, case_sensitive, quote_identifiers):
    try:
        expression = sqlglot.parse_one(query, read=read)
    except Exception as e:
        return f"Error parsing query: {e}"

    if case_sensitive == '1':
        return qualify_tables(expression, case_sensitive=True).sql() + ';'
    elif case_sensitive == '2':
        return qualify_tables(expression, case_sensitive=False).sql() + ';'
    elif quote_identifiers:
        return qualify(expression, quote_identifiers=False).sql() + ';'
    else:
        return query + ';'

def main(sql_query, read, write, source, case_sensitive, quote_identifiers):
    # Check if the SQL contains DDL keywords
    ddl_keywords = ['CREATE', 'ALTER', 'DROP', 'TRUNCATE', 'COMMENT']
    first_word = sql_query.strip().split()[0].upper()
    if first_word in ddl_keywords:
        result = "DDL transformation is not supported. Only DML transformation is supported."

    else:
        try:
            queries = sqlglot.transpile(sql_query, read=read, write=write)
            if source == 'text':
                if case_sensitive == '0' and quote_identifiers == False:
                    result = sqlparse.format(queries[0], reindent_aligned=True) + ';'
                else:
                    result = sqlparse.format(process_query(sql_query, read, case_sensitive, quote_identifiers),
                                             reindent_aligned=True)

            elif source == 'file':
                if case_sensitive == '0' and quote_identifiers == False:
                    result = sqlparse.format(';'.join(queries), reindent=True)
                else:
                    queries = sql_query.split(';')
                    result = sqlparse.format(
                        ''.join(process_query(query, read, case_sensitive, quote_identifiers) for query in queries),
                        reindent=True)
            else:
                result = "Invalid method specified."
        except Exception as e:
            result = f"Error transpiling query: {e}"

    print(result)

sql = """
select a.id, a.name, b.cate, rownum as rn from table_1, table_2
where a.id = b.a_id(+)

"""


main(sql, "oracle", "doris", 'text', '1', False)
