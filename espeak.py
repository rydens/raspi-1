import subprocess as sp


def say(text=None,voice=None):
<<<<<<< HEAD
  text = " '" + text + "'"
  if voice != None:
    voice = " -v " + voice
  else:
    voice = ""
  sp.call("espeak" + voice + text, shell=True)
=======
    text = "'" + text + "'"
    if voice != None:
        voice = " -v " + voice
    else:
        voice = ""
    sp.call("espeak" + voice + text, shell=True)
>>>>>>> 4bf319c530ebe026f307d3cddc4aa5d9491b0af2
