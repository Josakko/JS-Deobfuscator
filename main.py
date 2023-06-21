import jsbeautifier, sys
import argparse
import os
import rich



class Deobfuscator:
    def __init__(self, parser):
        self.parser = parser
        self.parser.add_argument("-i", help="File to deobfuscate", default="")
        self.parser.add_argument("-o", help="Deobfuscated file, do not specify if you want to show output in stdout", default="stdout")
        arg = self.parser.parse_args()

        file = arg.i
        if not file: 
            rich.print(f"""
usage: {os.path.basename(sys.argv[0])} [-h] [-i I] [-o O]

options:
-h, --help  show this help message and exit
-i I        File to deobfuscate
-o O        Deobfuscated file, do not specify if you want to show output in stdout
            """)
            sys.exit(1)


        if os.path.isfile(file):
            string = self.deobfuscate(file)
            if arg.o == "stdout":
                print(string)
            else:
                try: open(arg.o, "w", encoding="utf-8").write(string)
                except: rich.print("[bold red][-] Error: Could not write output to specified file!")
        else:
            rich.print("[bold red][-] Entered file does not exist or isnt a file!")
        

    def deobfuscate(self, input):
        try: string = open(input, "r", encoding="utf-8").read()
        except: return False

        try:
            deobfuscated = jsbeautifier.Beautifier().beautify(string, jsbeautifier.default_options())
        except: return False

        return deobfuscated
        #open(output, "w", encoding="utf-8").write(deobfuscated)



if __name__ == "__main__":
    Deobfuscator(argparse.ArgumentParser())

