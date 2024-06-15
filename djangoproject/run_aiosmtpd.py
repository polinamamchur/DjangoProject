import asyncio
from aiosmtpd.controller import Controller

class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        print('Message from:', envelope.mail_from)
        print('Message to:', envelope.rcpt_tos)
        print('Message data:', envelope.content.decode('utf8', errors='replace'))
        return '250 OK'

if __name__ == "__main__":
    handler = CustomHandler()
    controller = Controller(handler, hostname='localhost', port=1025)
    controller.start()
    print('SMTP server running at localhost:1025')
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        controller.stop()
