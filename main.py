from fastapi import FastAPI
import uvicorn,io

app = FastAPI()

@app.get('/convert')
def converter(text:str):
    ascii_names = ['=','!','#','$','%','+','(',')','*',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','{','}','?','@','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','[',']','^','_']

    with open('fonts.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines(False)
        font_chars = [lines[n:n + 6] for n in range(0, len(lines), 6)]
    def align(letter):
        maxlen = max(len(line) for line in letter)
        return [f'{line:<{maxlen}}' for line in letter]

    font_chars = map(align, font_chars)
    charmap = dict(zip(ascii_names, font_chars))
    charmap[' '] = [' ' * 5] * 6 
    
    letters = []
    for char in text:
        letters.append(charmap[char.lower()])
    letters = map(align, letters) 
    buf = io.StringIO()
    for letter_parts in zip(*letters):
        print(*letter_parts, file=buf)
    
    return {"data": f"{buf.getvalue()}"}


uvicorn.run(app=app,host='0.0.0.0',port=8080)
