import tweepy, re, time
from nltk.tokenize import word_tokenize
from nltk.corpus import words
from credentials import *

cant_find = []

#need to make a lookup of words that sound similar, homophones
#ie  two/2  be/b 



lookup = {

	"a":"alpha",
	"b":"bravo",
	"c":"charlie",
	"d":"delta",
	"e":"echo",
	"f":"foxtrot",
	"g":"golf",
	"h":"hotel",
	"i":"india",
	"j":"juliet",
	"k":"kilo",
	"l":"lima",
	"m":"mike",
	"n":"november",
	"o":"oscar",
	"p":"papa",
	"q":"quebec",
	"r":"romeo",
	"s":"sierra",
	"t":"tango",
	"u":"uniform",
	"v":"victor",
	"w":"whiskey",
	"x":"xray",
	"y":"yankee",
	"z":"zulu"
	}


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

homophone_list = []

 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


def getTweetsFromFile(filename):

	with open(filename, 'r') as f:

		rows = f.readlines()
		#for row in rows:

		#print(row)
		#print(rows[0])
		readTweet(rows[0])

	return

def getTweetsFromWeb():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	public_tweets = api.home_timeline()

	with open(filename, 'w') as f:
		
		for tweet in public_tweets:
    			readTweet(tweet.text.encode('utf8'))


def saveTweets(filename):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	public_tweets = api.home_timeline()

	with open(filename, 'w') as f:
		
		for tweet in public_tweets:
			f.write(tweet.text.encode('utf8') + "\n")

def build_homophone_list():

	with open("/home/jdoe93410/Projects/message_passing/src/homophones-1.01.txt", "r") as f:
		rows = f.readlines()

	counter = 0
	start = 0
	for row in rows:
		if "----------------" in row:
			start = counter+1
		counter +=1


	homophone_list = []	
	for i in range(start, len(rows)):
		for j in rows[i].strip().split(','):
			homophone_list.append(j)

	return homophone_list



def is_word(token):

	if token in words.words():
		return True
	else:
		return False

def is_mixed_group(token):

	pattern = re.compile('^[a-zA-Z0-9]+')

	if pattern.match(token) and token not in words.words() :
		return True
	else:
		return False

def is_homophone(token, homophone_list):

	if token in homophone_list:
		return True
	else:
		return False

		
def readTweet(tweet):

	tokens = preprocess(tweet)

	#test for homophone, if yes say "I spell"
		#ie Two/2, bee/be/b

		#check out python package Fuzzy


	#test for letter group, if yes say "Letter group"
		#ie ARRL
	#test for initial, if yes say "Initial" 
		#ie R. or St. or Dr
		#State abbreviations.

	#test for street address, if yes say "Direction" 

	#test if number, if yes say "Figures"
		#ie August Figure 7
		#ie has figure 1 apple

	#test if mixed group, say "mixed group"
		#ie ke8crv

	

	print("Reading new tweet")
	for token in tokens:

		if is_word(token) and not is_homophone(token, homophone_list):
			
			print(token)
		else:
			print("I spell")
			for letter in token:
				if letter.lower() in lookup:
					word = lookup[letter.lower()]
					print(word)
				else:
					cant_find.append(letter.lower())
			print("space")

		time.sleep(1)

	#time.sleep(3)
	print(tweet)	
def main():


	#saveTweets("tweets.txt")
	getTweetsFromFile("tweets.txt")
	#getTweets()
	print(cant_find)

if __name__ == "__main__":

	main()

