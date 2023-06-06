from Zoe import *
import CuteON

def main(message=[]):
        
        return Generator.generate_text(text = CuteON.Read_.Read(CuteON.Get_.getLine("Config.sws", "Text")), message=" ".join(message))

