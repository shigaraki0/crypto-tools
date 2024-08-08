import hashlib
from hashlib import sha256

def check_file_integrity(filename):
	hash256 = sha256()
	
	try:
		with open(filename, 'rb') as f:
			content = f.read()
			hash256.update(content)
		
		file_hash = input('Enter the sha256 hash of the file: ')
		if len(file_hash) != 64:
			print('Invalid hash format.')
			return
		    
		if hash256.hexdigest() == file_hash:
			print('File: ' + filename + ' is OK.')
		else:
			print('File: ' + filename + ' is NOT OK.')
			
	except FileNotFoundError:
		print('The file ' + filename + ' was not found.')
	except Exception as e:
		print('ERROR: ' + str(e))

filename = input('Enter the filename to check the file integrity: ')
check_file_integrity(filename)
