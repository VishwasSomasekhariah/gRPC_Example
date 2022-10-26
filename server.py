from concurrent import futures
import grpc
import example_pb2
import example_pb2_grpc
import pandas as pd
from pprint import pprint

def get_iris(col_name):
	csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
	col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
	iris = pd.read_csv(csv_url, names=col_names)
	if col_name in col_names:
		return list(str(x) for x in iris[col_name])
	else:
		return ["NO COLUMN FOUND"]


class Computator(example_pb2_grpc.ComputatorServicer):
	def getMeInformation(self, request, context):
		df = pd.DataFrame()
		df[request.col_name] = get_iris(request.col_name)

		return example_pb2.getMeDataResponse(df=df.to_markdown())

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	example_pb2_grpc.add_ComputatorServicer_to_server(Computator(), server)
	server.add_insecure_port('[::]:20001')
	server.start()
	server.wait_for_termination()

if __name__ == '__main__':
	print("Server Running>>>")
	serve()