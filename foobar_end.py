import base64

MESSAGE = '''
GksWDREMBAcSS0VCUkgGBgQNEV9eT0YXDgAJHRMIFBFGTF9YVQoSAAQJCB0WSE1URgkDHh0dFQdG TF9YVQYPFxMJAREQAwRTTUxCGREHCBEXCQgdHBtGVFtMQg0cAw4XCgkBX15PRgYADgcRBhxGVFtM QgsTCQRTTUxCHh0ARlRbTEIPGwFAUxw=
'''

KEY = 'alexroat'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
