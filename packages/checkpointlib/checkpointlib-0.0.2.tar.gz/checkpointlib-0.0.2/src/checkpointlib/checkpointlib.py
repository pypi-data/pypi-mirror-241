import random
from urllib.request import urlopen
class checkpointAccount:
  def __init__(self, givenKey):
    # Create a user key
    userKey = ""
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!$1234567890"
    for i in range(20):
      userKey = userKey + chars[random.randint(0, (len(chars)))]
    if (givenKey == 0):
      self.key = userKey
    else:
      self.key = givenKey
    self.url = "https://kendasi.com/checkpoints/" + self.key
  def saveCheckpoint(self, message):
    url = "https://kendasi.com/checkpoints/write.php?key=" + self.key + "&message=" + message.replace(" ", "%20")
    with urlopen(url) as response:
      status = response.read()
    return status
  def clear(self):
    url = "https://kendasi.com/checkpoints/write.php?key=" + self.key + "&message="
    with urlopen(url) as response:
      status = response.read()
    return status
  def delete(self):
    url = "https://kendasi.com/checkpoints/delete.php?key=" + self.key
    with urlopen(url) as response:
      status = response.read()
    return status