#echo.py 

def echo(text: str, repetitions: int = 3) -> str:

    res = ""

    while repetitions > 0:
        
        text = text[len(text) - repetitions:]
        res += text + "\n"
        repetitions -= 1
    
    res += "."
    
    return res

if __name__ == "__main__":
    text = input("Yell at a mountain: ")
    print(echo(text))