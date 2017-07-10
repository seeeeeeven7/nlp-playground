import os;

# Constant variables

windowWidth = 5

# Log file to moniter the process
logOut = open("train.log", "w");

# Useful functions
def isChZh(ch):
	if ch is None:
		return False
	return ord(ch) >= 0x4e00 and ord(ch) <= 0x9fff

# loading corpus from file system and clean

print("Loading corpus")

chs = []
with open("3600493.corpus", "r") as corpusIn:
	lastCh = None
	for line in corpusIn:
		for ch in line:
			if isChZh(ch):
				chs.append(ch);
				lastCh = ch
			else:
				if lastCh is not None:
					chs.append(None)
					lastCh = None

# Calculate word and its env-word pair

print("Pre-work on corpus")

chIdMapper = {}
idChMapper = {}
def getChId(ch):
	if chIdMapper.get(ch) is None:
		chIdMapper[ch] = len(chIdMapper)
		idChMapper[chIdMapper[ch]] = ch
	return chIdMapper[ch]

chPairCount = {}
for i in range(0, len(chs)):
	for j in range(max(i - windowWidth, 0), min(i + windowWidth + 1, len(chs))):
		if isChZh(chs[i]) and isChZh(chs[j]) and i != j:
			iChId = getChId(chs[i])
			jChId = getChId(chs[j])
			chPair = str(iChId) + '-' + str(jChId)
			if chPairCount.get(chPair) is None:
				chPairCount[chPair] = 0
			chPairCount[chPair] += 1

chPairCountPairs = sorted(chPairCount.items(), key = lambda kv: kv[1], reverse = True);
for chPairCountPair in chPairCountPairs:
	pair = chPairCountPair[0].split('-')
	# print(idChMapper[int(pair[0])], idChMapper[int(pair[1])], chPairCountPair[1], file = logOut)

#print(len(chPairCount))
#for chPair in chPairCount.keys():
#	print(chPair, chPairCount[chPair])