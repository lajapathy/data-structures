import subprocess

config = 'test'
bulkstats_folder = 'sss'


bulkstats_parser_proc = subprocess.Popen(['subprocess3.py', ' -S ',config,' -B ',bulkstats_folder],stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)