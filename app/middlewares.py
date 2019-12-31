
def simple_middleware(get_response):
    def middleware(request):
        print('(From middleware)',request)
        response = get_response(request)
        print('(From middleware)',response)
        return response
    return middleware
