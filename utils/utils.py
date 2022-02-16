



def listToString(l):
	'''
	Convert list contains multiple sentences to a string
	Args:
                l (list): false for live stream and true for video 
	Outputs:
                s (string): whole sentence
        '''
	s, length = "", len(l)-1
	for i, item in enumerate(l):
		s = s + str(item) + ", " if i != length else s + "and "+ str(item)
	return s

