from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
import binascii

message = 'To be encrypted'
h = SHA.new(message)
pubkey = b'-----BEGIN PUBLIC KEY-----\nMzA4MTg5MDI4MTgxMDBDNDU2MEVBMUU0QjAwQUYwODUyNzgzMjBFMzQ2MTYyMTRGRTZERjM2RkRCNUU1NzJEMEM3Q0Y2QjkwRDc5OUY1NDBFODc1MDU1QkRFODcyOTVDNzNGMUNBQkFCQUY2REUxOTczRTVFNkQwQjMzRUJDRDFFM0RERTg3NEIxREU0MzhGRjk3NzcwRTczQ0MyQTIwNTQxM0E4RTk2QjQzNDVBNzdEQTlGMDQ5RDk0Qjk0MjM0OUJFNDY4MENBMDgzNjEzOUEzODk5MkY2M0M0RTI4MEY3Njg3MkFFRjU4MDlGMDkxQzBCQUREMkU0MTJBNTFCQTJFQzYyNTdDNEVGRDMxMDIwMzAxMDAwMQ==\n-----END PUBLIC KEY-----'
prikey = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDq+qbaMTZtPH3LuXLrAn37YGzcgrL7ieTILtkXTl5PIozJUQZ0\n6bQXr/uS+FtvYNSvaT53ZpSyKmVmWtoX7lFzA6FWsILFTgFUDNRnPIQv1rQb16wi\n694rKPRe1uIr8/hthXtTec8b2aJovizQOlkXY0PqZohNGofi02xlUD8KsQIDAQAB\nAoGBAMkKEI0ng8Br+9i8XqTQ6gaTVjBHpmhtbw8SfexhwXCFR9zJ9PM8LDgD+gKh\neGFPgEhfi/FOE7Rnb3/mBShqXsWbqz7STJ05GOxtKo+L1z5K7X4E9WmVjIEVU46I\nhF43LJQvoDjQRbZh2cUMSYUR8+LqJJd6MFdhLJhEIf+LhCbBAkEA71lRBiSwZH/8\nsaUE4qZ/vxkS65czBcWLSCgn+7D/kvunX1hxqi3zTxMn4gyluw3IICzvLFgdDG6f\nUZk23aDcyQJBAPtTgvi4lYAIoeh6Xx8NZxroVNVBlP9BzJTBCcnX1Ym0aC/p+6n8\n7Lu9bkKk/hb0r7Oy76wzxObWv9uvRQNp+qkCQQCoOy8oEkGpYgxLEKIObNj9iLIz\nxWKne+IaJZ902UPKG/fYnGHIK+QIgH5X9GvIvjcb5nl1wbkpM9fnkrltrdOBAkBe\n7LbuHEGTHy+P8BBXWSeVOSU5etC87GxJzvNUginMHhCv8C82kCoV6sFneIvjvb1T\nIQV3RAJdscS7Q+LMHE4pAkEAzp2o8+2+9QJwzkpxGyNjJ7ZECQsZIb7MOH7LYhX0\ncnwffXFt4ttcwbyX2SdhCVPBDkczkJkOzcnEqtjoWt+dBw==\n-----END RSA PRIVATE KEY-----'

key = RSA.importKey(pubkey)
key1 = RSA.importKey(prikey)

cipher = PKCS1_v1_5.new(key)
cipher1 = PKCS1_v1_5.new(key1)

ciphertext = cipher.encrypt(message+h.digest())

dsize = SHA.digest_size
sentinel = Random.new().read(15+dsize)      # Let's assume that average data length is 15
TestCipher = cipher1.decrypt(ciphertext, sentinel)
print TestCipher