from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

def check_mongo_connection(client_uri):
    connection = MongoClient(client_uri)

    try:
        connection.database_names()
        print('Data Base Connection Established........')

    except OperationFailure as err:
        print("Data Base Connection failed. Error: {err}")


def throw_if_mongodb_is_unavailable(host, port):
    import socket
    sock = None
    try:
        sock = socket.create_connection(
            (host, port),
            timeout=1) # one second
    except socket.error as err:
        raise EnvironmentError(
            "Can't connect to MongoDB at {host}:{port} because: {err}"
            .format(**locals()))
    finally:
        if sock is not None:
            sock.close()


if __name__ == "__main__":
    check_mongo_connection("mongodb://localhost:27017")
    throw_if_mongodb_is_unavailable(MONGODB_HOST, MONGODB_PORT)
