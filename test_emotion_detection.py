from EmotionDetection.emotion_detection import *
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        res1 = emotion_detection("I am glad this happened")
        self.assertEqual(res1, 'joy')

        res2 = emotion_detection("I am really mad about this")
        self.assertEqual(res1, 'anger')

        res3 = emotion_detection("I feel disgusted just hearing about this")
        self.assertEqual(res1, 'disgust')

        res4 = emotion_detection("I am so sad about this")
        self.assertEqual(res1, 'sadness')

        res5 = emotion_detection("I am really afraid that this will happen")
        self.assertEqual(res1, 'fear')

unittest.main()