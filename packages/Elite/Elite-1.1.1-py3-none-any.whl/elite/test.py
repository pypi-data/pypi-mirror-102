from unittest import TestCase, main
from .scheme import *
from .cipher import *
from .secret import *
import os

class SchemeTestCase(TestCase):
    def setUp(self):
        self.s1 = getscheme()
        self.s2 = getscheme()
        self.s1.importBinaryKey(self.s2.exportBinaryKey())
        self.s2.importHexKey(self.s1.exportHexKey())
        self.other = P384r1AesGcmScheme()
    def testKeyAgreement(self):
        self.assertEqual(self.s1.secret(), self.s2.secret())
    def testSignature(self):
        data = os.urandom(16)
        signature = self.s1.sign(data)
        self.assertTrue(self.s2.verify(data, signature))
        data = os.urandom(16)
        signature = self.s2.sign(data)
        self.assertTrue(self.s1.verify(data, signature))
    def testEncryption(self):
        data = os.urandom(16)
        encrypted = self.s1.encrypt(data)
        self.assertEqual(self.s2.decrypt(encrypted), data)
        data = os.urandom(16)
        encrypted = self.s2.encrypt(data)
        self.assertEqual(self.s1.decrypt(encrypted), data)
    def testInvalidCurve(self):
        self.assertRaises(CurveKindMismatch, self.s1.importBinaryKey, self.other.exportBinaryKey())

class CipherTestCase(TestCase):
    def setUp(self):
        self.provider = getprovider()
        self.other = AesGcmCryptoProvider()
    def testEncryption(self):
        key, data = os.urandom(16), os.urandom(16)
        encrypted = self.provider.encrypt(key, data)
        self.assertEqual(data, self.provider.decrypt(key, encrypted))
        self.assertRaises(AuthorizationCodeInvalid, self.provider.decrypt, key, b'invalid data!')
        self.assertRaises(AuthorizationCodeInvalid, self.other.decrypt, key, encrypted)

class SecretTestCase(TestCase):
    def setUp(self):
        self.publicKey = generate_pair(CurveKind.CK_SECP256K1)[1]
    def testKeyExport(self):
        export1 = self.publicKey.export().binary
        export2 = PublicKey.fromBinary(export1, CurveKind.CK_SECP256K1).export().binary
        self.assertEqual(export1, export2)
    def testInvalidCurve(self):
        self.assertRaises(CurveKindMismatch, PublicKey.fromHex, self.publicKey.export().hexadecimal, CurveKind.CK_SECP384R1)
    def testUnsupportedCurve(self):
        self.assertRaises(UnsupportedCurve, generate, CurveKind.CK_UNKNOWN)

if __name__ == '__main__':
    main()
