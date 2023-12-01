import asyncio
import tornado

from pg import Database
from settings import db_url


class BaseHandler(tornado.web.RequestHandler):
    @property
    def backend(self):
        return Backend()


class MainHandler(BaseHandler):
    def get(self):
        user_id = self.backend.get_user()
        self.write(user_id)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


class Backend(object):
    def __init__(self):
        self.db = Database(db_url)

    def get_user(self):
        user_id = self.db.get(
            "SELECT id FROM auth_user WHERE email='bmwasaru@gmail.com'"
        )
        return user_id


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
