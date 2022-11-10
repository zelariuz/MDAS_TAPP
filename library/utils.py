import base64
import joblib
import pickle

def encodeFile(filename):
	base64_message = None
	with open(filename, 'rb') as binary_file:
		binary_file_data = binary_file.read()
		base64_encoded_data = base64.b64encode(binary_file_data)
		base64_message = base64_encoded_data.decode('utf-8')
	return base64_message

def decodeFile(filename, textBase64):
	base64_bytes = textBase64.encode('utf-8')
	with open(filename, 'wb') as file_to_save:
		decoded_image_data = base64.decodebytes(base64_bytes)
		file_to_save.write(decoded_image_data)

def _obj(x):
	return x

def createTestFile(filename):
	obj = ['hola', 'Exito']
	# pickle.dump(_obj, open(filename,'wb'))
	joblib.dump(_obj, filename)

def loadModelObjectFile(filename):
	return joblib.load(filename)
	# return pickle.load(open(filename,'rb'))