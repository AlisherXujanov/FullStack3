import time


def print_time_taken(request, response):
    time_taken = time.time() - request.start_time
    print(f'Time taken: {round(time_taken, 5)} seconds')
    return response


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the view function name

        # Code to be executed for each request before
        print('I am before the view is called')

        request.start_time = time.time()
        response = self.get_response(request)
        response = print_time_taken(request, response)
        # Do something after the view is called

        view_name = request.resolver_match.view_name
        if view_name is not None:
            print(f'I am after the {view_name} view is called')

        return response
