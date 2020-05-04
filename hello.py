
def app(environ, start_response):
    data = b''
    print(environ['PATH_INFO'])
    print(environ['QUERY_STRING'])
    if environ['QUERY_STRING']:
        params = environ['QUERY_STRING'].split('&')
        print(params)
        for item in params:
            data = data + item.encode() + b'\n'
    status = '200 OK'
#    with open('environ.txt', 'w') as f:
#        for k, v in environ.items():
#            f.write(f'{k}-------{v}\n')
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

