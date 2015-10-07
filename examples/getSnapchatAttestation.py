from CasperAPI import CasperAPI, CasperException

def main():
	casper = CasperAPI("your_api_key", "your_api_secret")
	try:
		nonce = casper.generateSnapchatNonce("username", "password", "1234567890")
		attestation = casper.getSnapchatAttestation(nonce)

		print "Attestation: {0}".format(attestation)
	except CasperException, e:
		print "Oops! {0}".format(e)

if __name__ == "__main__":
	main()