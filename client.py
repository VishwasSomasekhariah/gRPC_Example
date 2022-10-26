import grpc
import example_pb2
import example_pb2_grpc
from pprint import pprint

def run_client():
	with grpc.insecure_channel('localhost:20001') as channel:
		stub = example_pb2_grpc.ComputatorStub(channel)
		response = stub.getMeInformation(example_pb2.getMeDataRequest(col_name = "Sepal_Length"))
		print("Client recieved the response successfully:")
		print(bytes(str(response),"utf-8").decode("unicode_escape"))

if __name__ == '__main__':
	run_client()
