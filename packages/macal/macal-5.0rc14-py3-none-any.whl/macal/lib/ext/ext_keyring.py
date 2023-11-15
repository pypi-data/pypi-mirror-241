# This is the supporting library for Macal 2.0 keyrings.

import keyring

def GetPassword(username):
    return keyring.get_password("passwords", username)

def SetPassword(username, password):
    keyring.set_password("passwords", username, password)

def DeletePassword(username):
    keyring.delete_password("passwords", username)

def SetMerakiApiKey(customer, key):
    keyring.set_password("meraki", customer, key)

def GetMerakiApiKey(customer):
    return keyring.get_password("meraki", customer)