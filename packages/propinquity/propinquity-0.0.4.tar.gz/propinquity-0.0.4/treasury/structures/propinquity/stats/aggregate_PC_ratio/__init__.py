
'''
	import propinquity.stats.aggregate_PC_ratio as aggregate_PC_ratio
	evaluation = aggregate_PC_ratio.calc (example_1)
	
	import json
	print ("evaluation:", json.dumps (evaluation, indent = 4))
'''

'''
	OUTPUT:
	
	{
		"expirations": [{
			"expiration": "2023-10-27",
			"sums": {
				"puts": {
					"ask":
					"bid":
					"last"
				},
				"calls": {
					"ask":
					"bid":
					"last"
				}
			},
			"PC ratios": {
				"ask":
				"bid":
				"last"
			}
		}],
		"sums": {
			"puts": {
				"ask":
				"bid":
				"last"
			},
			"calls": {
				"ask":
				"bid":
				"last"
			}
		},
		"PC ratios": {
			"ask":
			"bid":
			"last"
		}
	}
'''

from propinquity.utilities.ratio import calculate_ratio

import pydash
def RETURN_NUMBER (OBJECT, PATH, DEFAULT):
	FOUND = pydash.get (
		OBJECT,
		PATH,
		DEFAULT
	)
	
	TYPE = type (FOUND)
	if (TYPE == int or TYPE == float):
		return FOUND
		
	if (FOUND == None):
		return DEFAULT;

	print ("FOUND WAS NOT ACCOUNTED FOR:", FOUND)
	raise Exception (f"FOUND WAS NOT ACCOUNTED FOR: { FOUND }")
		
	return DEFAULT

def RETRIEVE_MULTIPLICAND (strike):
	return strike ["contract size"] * strike ["open interest"]
 
	try:
		pass;
	
	except Exception as E:
		pass;
		

def EQUALITY_CHECK (PARAM_1, PARAM_2):
	try:
		assert (PARAM_1 == PARAM_2)
	except Exception as E:
		import traceback
		
		print ("PARAM 1", PARAM_1)
		print ("PARAM 2", PARAM_2)	
		
		print (traceback.print_exception (E))

		raise Exception (E)

	return
	

def calc (CHAIN):
	expirations = CHAIN ["expirations"]
	
	evaluation = {
		"expirations": [],
		"sums": {
			"puts": {
				"ask": 0,
				"bid": 0,
				"last": 0
			},
			"calls": {
				"ask": 0,
				"bid": 0,
				"last": 0
			}
		},
		"PC ratios": {
			"ask": 0,
			"bid": 0,
			"last": 0
		}
	}
	
	
	for expiration in expirations:
		calls_strikes = expiration ["calls"]["strikes"]
		puts_strikes = expiration ["puts"]["strikes"]
		
		expiration_NOTE = {
			"expiration": expiration ["expiration"],
			"sums": {
				"puts": {
					"ask": 0,
					"bid": 0,
					"last": 0
				},
				"calls": {
					"ask": 0,
					"bid": 0,
					"last": 0
				}
			},
			"PC ratios": {
				"ask": 0,
				"bid": 0,
				"last": 0
			}
		}
		
		EQUALITY_CHECK (len (calls_strikes), len (puts_strikes))
		
		DIRECTION = "calls"
		for strike in calls_strikes:		
			expiration_NOTE ["sums"][ DIRECTION ]["ask"] += RETURN_NUMBER (strike, [ "prices", "ask" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["sums"][ DIRECTION ]["bid"] += RETURN_NUMBER (strike, [ "prices", "bid" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["sums"][ DIRECTION ]["last"] += RETURN_NUMBER (strike, [ "prices", "last" ], 0) * RETRIEVE_MULTIPLICAND (strike)
		
		DIRECTION = "puts"
		for strike in puts_strikes:		
			expiration_NOTE ["sums"][ DIRECTION ]["ask"] += RETURN_NUMBER (strike, [ "prices", "ask" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["sums"][ DIRECTION ]["bid"] += RETURN_NUMBER (strike, [ "prices", "bid" ], 0) * RETRIEVE_MULTIPLICAND (strike)
			expiration_NOTE ["sums"][ DIRECTION ]["last"] += RETURN_NUMBER (strike, [ "prices", "last" ], 0) * RETRIEVE_MULTIPLICAND (strike)
		
		expiration_NOTE ["PC ratios"]["ask"] = calculate_ratio (
			expiration_NOTE ["sums"][ "puts" ]["ask"],
			expiration_NOTE ["sums"][ "calls" ]["ask"]
		)
		expiration_NOTE ["PC ratios"]["bid"] = calculate_ratio (
			expiration_NOTE ["sums"][ "puts" ]["bid"],
			expiration_NOTE ["sums"][ "calls" ]["bid"]
		)
		expiration_NOTE ["PC ratios"]["last"] = calculate_ratio (
			expiration_NOTE ["sums"][ "puts" ]["last"],
			expiration_NOTE ["sums"][ "calls" ]["last"]
		)
		
		evaluation ["sums"][ "calls" ]["ask"] += RETURN_NUMBER (expiration_NOTE, [ "sums", "calls", "ask" ], 0)
		evaluation ["sums"][ "calls" ]["bid"] += RETURN_NUMBER (expiration_NOTE, [ "sums", "calls", "bid" ], 0)
		evaluation ["sums"][ "calls" ]["last"] += RETURN_NUMBER (expiration_NOTE, [ "sums", "calls", "last" ], 0)
		
		evaluation ["sums"][ "puts" ]["ask"] += RETURN_NUMBER (expiration_NOTE, [ "sums", "puts", "ask" ], 0)
		evaluation ["sums"][ "puts" ]["bid"] += RETURN_NUMBER (expiration_NOTE, [ "sums", "puts", "bid" ], 0)
		evaluation ["sums"][ "puts" ]["last"] += RETURN_NUMBER (expiration_NOTE, [ "sums", "puts", "last" ], 0)
		
		evaluation ["expirations"].append (expiration_NOTE)
		
	evaluation ["PC ratios"]["ask"] = calculate_ratio (
		evaluation ["sums"][ "puts" ]["ask"],
		evaluation ["sums"][ "calls" ]["ask"]
	)
	
	evaluation ["PC ratios"]["bid"] = calculate_ratio (
		evaluation ["sums"][ "puts" ]["bid"],
		evaluation ["sums"][ "calls" ]["bid"]
	)
	
	evaluation ["PC ratios"]["last"] = calculate_ratio (
		evaluation ["sums"][ "puts" ]["last"],
		evaluation ["sums"][ "calls" ]["last"]
	)

	return evaluation