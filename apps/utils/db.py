from django.db import connection


def procedure(procedure_name, *proc_params):
    cursor = connection.cursor()
    cursor.execute(
        "select * from %s (%s);" % \
        (
            procedure_name,
            ', '.join(('\'' + str(x) + '\'') if type(x) == str else str(x) \
                for x in proc_params)
        )
    )
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results


def single_procedure(procedure_name, *proc_params):
    cursor = connection.cursor()
    cursor.execute(
        "select * from %s (%s);" % \
        (
            procedure_name,
            ', '.join(('\'' + str(x) + '\'') if type(x) == str else str(x) \
                for x in proc_params)
        )
    )
    results = cursor.fetchall()
    return results


def complex_procedure(fields, procedure_name, *proc_params):
    cursor = connection.cursor()
    cursor.execute(
        "select %s from %s (%s);" % \
        (
            ', '.join(field for field in fields),
            procedure_name,
            ', '.join(('\'' + str(x) + '\'') if type(x) == str else str(x) \
                for x in proc_params)
        )
    )
    results = cursor.fetchall()
    return results

def full_complex_procedure(fields, procedure_name, *proc_params):
    cursor = connection.cursor()
    cursor.execute(
        "select %s from %s (%s);" % \
        (
            ', '.join(field for field in fields),
            procedure_name,
            ', '.join(('\'' + str(x) + '\'') if type(x) == str else str(x) \
                for x in proc_params)
        )
    )
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results

def wh_procedure(procedure_name, wh, *proc_params):
    cursor = connection.cursor()
    cursor.execute(
        "select * from %s (%s) WHERE %s LIKE  '%s%s%s';" % \
        (
            procedure_name,
            ', '.join(('\'' + str(x) + '\'') if type(x) == str else str(x)
                for x in proc_params),
            wh[0],
            '%',
            wh[1],
            '%'
        )
    )
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results
