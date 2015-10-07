from CasperAPI import CasperAPI, CasperException

def main():
	casper = CasperAPI("your_api_key", "your_api_secret")
	try:
		token = casper.getSnapchatClientAuth("username", "password", "1234567890")

		print "X-Snapchat-Client-Auth: {0}".format(token)
	except CasperException, e:
		print "Oops! {0}".format(e)

if __name__ == "__main__":
	main()