                                                                               
# import the emotion_detector function from the EmotionDetection package
from EmotionDetection.emotion_detection import emotion_detector
# import unittest library
import unittest
# Create a unittest class called 'TestEmotionDetector'
class TestEmotionDetector(unittest.TestCase):
    # Define function 'test_emotion_detector()' to run the unit tests
    def test_emotion_detector(self):
        # Test case for dominant joy emotion
        joy_emotion = emotion_detector("I am glad this  happened")
        self.assertEqual(joy_emotion['dominant_emotion'], 'joy')
        # Test case for dominant anger emotion
        anger_emotion = emotion_detector("I am rerally mad about this")
        self.assertEqual(anger_emotion['dominant_emotion'], 'anger')
        # Test case for dominant disgust emotion
        disgust_emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_emotion['dominant_emotion'], 'disgust')
        # Test case for dominant sadness  emotion
        sadness_emotion = emotion_detector("I am so sad about this")
        self.assertEqual(sadness_emotion['dominant_emotion'], 'sadness')
        # Test case for dominant fear emotion
        fear_emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_emotion['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
