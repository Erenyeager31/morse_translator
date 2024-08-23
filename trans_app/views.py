from django.shortcuts import render,HttpResponse

from django.http.response import StreamingHttpResponse 

# Create your views here.
def index(request):
    return render(request,'index.html')

def mtot(request):
    morse_to_text = {
        ".-":"A",
        "-...":"B",
        "-.-.":"C",
        "-..":"D",
        ".":"E",
        "..-.":"F",
        "--.":"G",
        "....":"H",
        "..":"I",
        ".---":"J",
        "-.-":"K",
        ".-..":"L",
        "--":"M",
        "-.":"N",
        "---":"O",
        ".--.":"P",
        "--.-":"Q",
        ".-.":"R",
        "...":"S",
        "-":"T",
        "..-":"U",
        "...-":"V",
        ".--":"W",
        "-..-":"X",
        "-.--":"Y",
        "--..":"Z",
        ".----":"1",
        "..---":"2",
        "...--":"3",
        "....-":"4",
        ".....":"5",
        "-....":"6",
        "--...":"7",
        "---..":"8",
        "----.":"9",
        "-----":"0",
        ".-.-.-":".",
        "--..--":",",
        "..--..":"?",
        "//":"\t"
    }
    value = ""
    if request.method == "POST":
        input = request.POST.get('texti')
        input = input.replace("_","-")
        input_array = input.split("  ")  # Split by double spaces

        for i in input_array:
            if i.strip():  # Ensure we don't process empty strings
                words = i.split(" ")  # Split by single space to get individual Morse codes
                for word in words:
                    if word in morse_to_text:
                        value += morse_to_text[word]
                value += " "  # Add a single space between the converted words

    conversion = {
        "value": value.strip()  # Strip any leading or trailing spaces
    }
    
    return render(request, 'morse_to_text.html', conversion)

def ttom(request):
    text_to_morse = {
        "A":".-",
        "B":"-...",
        "C":"-.-.",
        "D":"-..",
        "E":".",
        "F":"..-.",
        "G":"--.",
        "H":"....",
        "I":"..",
        "J":".---",
        "K":"-.-",
        "L":".-..",
        "M":"--",
        "N":"-.",
        "O":"---",
        "P":".--.",
        "Q":"--.-",
        "R":".-.",
        "S":"...",
        "T":"-",
        "U":"..-",
        "V":"...-",
        "W":".--",
        "X":"-..-",
        "Y":"-.--",
        "Z":"--..",
        "1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
        "5":".....",
        "6":"-....",
        "7":"--...",
        "8":"---..",
        "9":"----.",
        "0":"-----",
        ".":".-.-.-",
        ",":"--..--",
        "?":"..--..",
        " ":"\t"
    }
    value = ""
    if request.method == "POST":
        input = request.POST.get('texti')
        input = input.upper()
        value = ""
        for i in input:
            value += text_to_morse[i]+"/"
        print(value)
        conversion = {
        "value":value
        }
    else:
        conversion = {
            "value":""
        }
    # print(input_array)
    return render(request,'text_to_morse.html',conversion)