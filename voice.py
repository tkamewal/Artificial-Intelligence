from win32com.client import Dispatch
Windows_Speak = Dispatch('SAPI.Spvoice')

Windows_Speak.Voice = Windows_Speak.GetVoices().Item(2)
Windows_Speak.Rate = 3
print(Windows_Speak.GetVoices().Item(2).GetDescription()) #just to see what voice is used

Windows_Speak.Speak('Tomato')