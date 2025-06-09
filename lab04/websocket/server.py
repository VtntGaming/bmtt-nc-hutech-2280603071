import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        self.clients.add(self)
        print("Có một client mới kết nối")

    def on_close(self):
        self.clients.remove(self)
        print("Client đã ngắt kết nối")
        
    @classmethod
    def send_message(cls, message):
        print(f"Gửi tin nhắn {message} đến các client: {len(cls.clients)}")
        for client in cls.clients:
            client.write_message(message)
            
class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)
    
def main():
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],
        websocket_ping_interval=10,
        websocket_ping_timeout=30,)
    
    app.listen(8888)
    print("WebSocket server đang chạy trên cổng 8888...")
    io_loop = tornado.ioloop.IOLoop.current()
    word_selector = RandomWordSelector(["apple", "banana", "cherry", "date", "elderberry"])
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()),
        3000  # Gửi tin nhắn mỗi 3 giây
    )
    
    periodic_callback.start()
    io_loop.start()
    
if __name__ == "__main__":
    main()