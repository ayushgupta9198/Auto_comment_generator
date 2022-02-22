import aqgFunction


# Main Function
def main(filepath):
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()

    inputTextPath = filepath
    readFile = open(inputTextPath, 'r+', encoding="utf8")
    #readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')

    inputText = readFile.read()
    #inputText = '''I am Dipta. I love codding. I build my carrier with this.'''

    questionList = aqg.aqgParse(inputText)
    question=aqg.display(questionList)
#    print(inputText)
#    aqg.DisNormal(questionList)

    return question


# Call Main Function
if __name__ == "__main__":
    main(filepath)

