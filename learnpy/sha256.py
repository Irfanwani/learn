import hashlib
import time

hacked_password = '2b57bf26d8e30b64cc53525f01de68e953d7fcaef007b7551bec5660e0a4073f'

with open('pass.txt', 'r') as file:
	content = file.readlines()

#with open('hashes.txt', 'w') as file:
#	for i in content:
#		newstr = i.replace('\n', '')
#		file.write(f"{newstr} >>>   {hashlib.sha256(newstr.encode('utf-8')).hexdigest()}\n")

start = time.time()

for i in content:
	newstr = i.replace('\n', '')
	hash = hashlib.sha256(newstr.encode('utf-8')).hexdigest()
	print(f'{newstr} >> {hash}')
	if hash == hacked_password:
		print('Password cracked!!!!')
		print('Password:', newstr)
		break
else:
	print("password cracking failed! No password from the pass.txt file is correct.")

end = time.time()

print('Execution time: ', '{:.2f} s'.format(end-start))
