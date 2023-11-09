
import io

def readFileToList(filename):
  lines = []
  try:
    with io.open(filename, "r", encoding="utf-8") as f:
      for line in f:
        lines.append(line.strip())
  except Exception as e:
    print(f"An error occurred while reading file {filename}.")
    print(e)

  return lines

def writeToFile(filename, content):
  try:
    with io.open(filename, "w", encoding="utf-8") as f:
      f.write(content)
  except Exception as e:
    print(f"An error occurred while writing to file {filename}.")
    print(e)
 

def splitString(to_split):
    list= to_split.split(" ")
    return list

def readUserInput(message):
    print(message)
    user_input = input()
    return user_input
