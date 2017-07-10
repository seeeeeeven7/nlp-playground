import os

novelId = "3600493"
chapterCount = 118

filename = novelId + ".out"
#os.makedirs(os.path.dirname(filename), exist_ok=True)

with open(filename, "w") as fout:
	for chapterId in range(1, chapterCount):
		with open(str(chapterId), "r") as fin:
			for line in fin:
				fout.write(line)