#!/usr/bin/python2.7

import sys

import tornado.web
import tornado.ioloop
import tornado.httpserver


from execrest.handlers.MainHandler import MainHandler




def main():
    app = tornado.web.Application([
        (r'/kafka', MainHandler)
     ], debug=True, autoreload=True)

    server = tornado.httpserver.HTTPServer(app)

    # Single-process dev code:
    server.listen(2016)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
    sys.exit(0)
