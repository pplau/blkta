import sys
sys.path.append('/Users/PP/Documents/Paper\ \&\ Book/Myself/NEW/blkta')

import os
import re


class Analysis:
	
	def __init__(self, file_path='./log'):
		# do not need to give the file path if the log is stored in the same documnet and name as 'log'
		self.file_path = file_path
		self.blk_file = open(file_path)
		self.total_count = {'read_total':0, 'write_total':0}
		self.read_count = {'io_4k':0, 'io_4kto8k':0, 'io_8kto16k':0, 'io_16kto32k':0, 'io_32kto64k':0, 'io_big':0}
		self.write_count = {'io_4k':0, 'io_4kto8k':0, 'io_8kto16k':0, 'io_16kto32k':0, 'io_32kto64k':0, 'io_big':0}
		self.read_res = {}
		self.write_res = {}

	def __IO_statistc__(self):
		self.read_res['perc_4k'] = round(float(self.read_count['io_4k']) / float(self.total_count['read_total']), 2)
		self.read_res['perc_4kto8k'] = round(float(self.read_count['io_4kto8k']) / float(self.total_count['read_total']), 2)
		self.read_res['perc_8kto16k'] = round(float(self.read_count['io_8kto16k']) / float(self.total_count['read_total']), 2)
		self.read_res['perc_16kto32k'] = round(float(self.read_count['io_16kto32k']) / float(self.total_count['read_total']), 2)
		self.read_res['perc_32kto64k'] = round(float(self.read_count['io_32kto64k']) / float(self.total_count['read_total']), 2)
		self.read_res['perc_big'] = round(float(self.read_count['io_big']) / float(self.total_count['read_total']), 2)

		self.write_res['perc_4k'] = round(float(self.write_count['io_4k']) / float(self.total_count['write_total']), 2)
		self.write_res['perc_4kto8k'] = round(float(self.write_count['io_4kto8k']) / float(self.total_count['write_total']), 2)
		self.write_res['perc_8kto16k'] = round(float(self.write_count['io_8kto16k']) / float(self.total_count['write_total']), 2)
		self.write_res['perc_16kto32k'] = round(float(self.write_count['io_16kto32k']) / float(self.total_count['write_total']), 2)
		self.write_res['perc_32kto64k'] = round(float(self.write_count['io_32kto64k']) / float(self.total_count['write_total']), 2)
		self.write_res['perc_big'] = round(float(self.write_count['io_big']) / float(self.total_count['write_total']), 2)

	def run(self):
		for line in self.blk_file.readlines():
			value_list = re.split(r'\s+', line)

			if value_list[5] == 'C':
				# success write/read to/from  disk
				if value_list[6] == 'W' or value_list[6] == 'WM':
					# write to disk
					self.total_count['write_total'] +=1
					io_size = int(value_list[9])
					if io_size <= 8:
						self.write_count['io_4k'] +=1

					if io_size > 8 and io_size <= 16:
						self.write_count['io_4kto8k'] +=1

					if io_size > 16 and io_size <= 32:
						self.write_count['io_8kto16k'] +=1

					if io_size > 32 and io_size <= 64:
						self.write_count['io_16kto32k'] +=1

					if io_size > 64 and io_size <= 128:
						self.write_count['io_32kto64k'] +=1

					if io_size > 128:
						self.write_count['io_big'] +=1

				if value_list[6] == 'R' or value_list[6] == 'RM':
					# read from disk
					self.total_count['read_total'] +=1
					io_size = int(value_list[9])
					if io_size <= 8:
						self.read_count['io_4k'] +=1

					if io_size > 8 and io_size <= 16:
						self.read_count['io_4kto8k'] +=1

					if io_size > 16 and io_size <= 32:
						self.read_count['io_8kto16k'] +=1

					if io_size > 32 and io_size <= 64:
						self.read_count['io_16kto32k'] +=1

					if io_size > 64 and io_size <= 128:
						self.read_count['io_32kto64k'] +=1

					if io_size > 128:
						self.read_count['io_big'] +=1

		self.__IO_statistc__()
		print self.read_res
		print self.write_res



if __name__=='__main__':
	anyls = Analysis()
	anyls.run()

