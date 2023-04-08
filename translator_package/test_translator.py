import requests
import unittest

class FromFrenchToEnglishTextTranslation(unittest.TestCase):
    def testTwo(self):
        response = requests.post('http://localhost:8080/frenchToEnglish', json={"textToTranslate": "Bonjour"}, headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"translation": "Hello"}])
        self.assertNotEqual(response.json(), [{"translation": "Bonjour"}])

class FromEnglishToFrenchTextTranslation(unittest.TestCase):
    def testOne(self):
        response = requests.post('http://localhost:8080/englishToFrench', json={"textToTranslate": "Hello"}, headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"translation": "Bonjour"}])



class FromEnglishToSpanishTextTranslation(unittest.TestCase):
    def testThree(self):
        response = requests.post('http://localhost:8080/englishToSpanish', json={"textToTranslate": "Hello my name is Alex"}, headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"translation": "Hola mi nombre es Alex"}])
        self.assertNotEqual(response.json(), [{"translation": "Hello my name is Alex"}])

unittest.main()