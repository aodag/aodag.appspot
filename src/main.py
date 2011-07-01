from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from protorpc import messages
from protorpc.webapp import service_handlers
from protorpc import remote

pakcage = 'hello'

class HelloRequest(messages.Message):
    my_name = messages.StringField(1, required=True)

class HelloResponse(messages.Message):
    hello = messages.StringField(1, required=True)

class HelloService(remote.Service):

    @remote.remote(HelloRequest, HelloResponse)
    def hello(self, request):
        return HelloResponse(hello="Hello, there %s!" % request.my_name)




urls = [
    ('/hello', HelloService),
]



def main():
    application = webapp.WSGIApplication(service_handlers.service_mapping(urls),
        debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
