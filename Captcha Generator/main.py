from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha

# Image captcha
image = ImageCaptcha()
imageData = image.generate('1234')
image.write('1234', 'captcha.png')

# Audio captcha
audio = AudioCaptcha()
audioData = audio.generate('1234')
audio.write('1234', 'captcha.wav')