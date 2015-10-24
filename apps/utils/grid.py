import math
from django.db import connection


def jqgrid(procedure_name, wh, sidx, sord, start, limit):
    cursor = connection.cursor()
    cursor.execute(
        "select * from %s () where %s ORDER BY %s %s limit %s offset %s;" %
        (
            procedure_name,
            wh,
            sidx,
            sord,
            limit,
            start
        )
    )
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results


def jqgrid_count(procedure_name, wh):
    cursor = connection.cursor()
    cursor.execute(
        "select count(*) from %s () WHERE %s;" %
        (
            procedure_name,
            wh
        )
    )
    results = cursor.fetchall()
    return results[0][0]


def jqgrid_generic(request, function_name, cols):
    page = int(request.GET['page'])
    limit = int(request.GET['rows'])
    sidx = request.GET['sidx']
    sord = request.GET['sord']

    wh = "1=1 "
    if request.GET['_search'] == 'true':
        for r in request.GET:
            if r not in ('page', 'sidx', 'sord', 'rows', 'nd', '_search'):
                wh += "AND %s LIKE '%s%s%s' " % (r, '%', request.GET[r], '%')

    count = jqgrid_count(function_name, wh)
    total_pages = 0

    if sidx:
        sidx = 1
    if count > 0 and limit > 0:
        total_pages = math.ceil(count / limit)
    if page > total_pages:
        page = total_pages
    start = limit * page - limit
    if start < 0:
        start = 0
    row = []
    row_result = jqgrid(function_name, wh, sidx, sord, start, limit)
    for row_item in row_result:
        call = {'id': row_item['id'],
                'cell': [row_item[x] for x in cols]}
        row.append(call)
    resultado = {
        'page': page,
        'total': total_pages,
        'records': count,
        'rows': row
    }
    return resultado
