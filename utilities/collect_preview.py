import os
import re
import glob
import platform
import shutil
from subprocess import call

ext = ".mov"

if platform.system() == 'Windows':
	search_pattern = r"//alpha/projects/3033/episodes/ep01/*/*_*/preview"
	dst_dir = r"//alpha/projects/3033/previews"
if platform.system() == 'Darwin':
	search_pattern = r"/Volumes/projects/3033/episodes/ep01/*/*_*/preview"
	dst_dir = r"/Volumes/projects/3033/previews"

def collect_mov(arg):
	for _dirname in glob.glob(search_pattern):
		files = [os.path.join(_dirname, x) for x in os.listdir(_dirname) if '_comp_' in x and x.split('.')[-1] == 'mov']
		try:
			src_file = max(files, key=os.path.getmtime)
			print(src_file)

			src_name = os.path.basename(src_file).split('.')[0]
			dst_name = '_'.join(src_name.split('_')[:2]) + '.mov'		
			dst_file = os.path.join(dst_dir, dst_name).replace('\\', '/')		

			if arg == 'mklink':
				call(['mklink', dst_file, src_file], shell=True)
			if arg == 'copy':
				shutil.copy(src_file, dst_file)
		except:
			pass

collect_mov('copy')

input('Done!!!')