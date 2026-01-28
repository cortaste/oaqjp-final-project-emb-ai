import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        self.assertEqual(emotion_detector('I love this new technology'), 'test')



if __name__ == "__main__":
    unittest.main()
