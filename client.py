import grpc
import example_pb2
import example_pb2_grpc

def run_client():
	with grpc.insecure_channel('localhost:20001') as channel:
		stub = grpc.example_pb2_grpc.ComputatorStub(channel)
		response = stub.getMeInformation(example_pb2.getMeDataRequest(col_name = "something_goes_here"))
		print("Client recieved the response successfully:")
		print(response)

if __name__ == '__main__':
	run_client()
