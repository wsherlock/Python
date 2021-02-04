import subprocess

infile = 'video.ts'
outfile = 'video.mp4'

subprocess.run(['ffmpeg', '-i', infile, outfile])