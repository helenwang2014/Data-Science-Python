file_for_reading = open('reading_file.txt', 'r')

file_for_writing = open('writing_file.txt', 'w')

file_for_appending = open('appending_file.txt', 'a')

file_for_writing.close()



with open(filename,'r') as f:
	data = function_that_gets_data_from(f)
	process(data)

# read a whole text file, you can just iterate over the lines of the file using for:
starts_with_hash = 0

with open('input.txt', 'r') as f:
	for line in file:
		if re.match("^#", line):
			starts_with_hash += 1



def get_domain(email_address):
	'''split on '@' and return the last piece
	return email_address.lower().split("@")[-1]


with open('email_address.txt', 'r') as f:
	doman_counts = Counter(get_domain(line.strip())
						   for line in f
						   if "@" in line)





