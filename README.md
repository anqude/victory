# Victory

## Simple quiz game

### Instruction
**Input file format**
```sh
question|answer
```

**Args**
```sh
./victory.py -f or --file "Path_to_file"
./victory.py -c or --count "Number_of_questions"
```

**What does it do**
- Opens the file selection dialog
- Asks the number of questions in the quiz
- Read question and answers from file
- Conducts a quiz with the input of answers
- Displays the result and correct answers

**Showing errors**
- "Неправильный формат файла" **checking the file for the validity of the data inside**
- "Нет Файла", "Файл не выбран" **checking the presence of the file**
