import argparse
import re


def parsers() -> str:
    """
        Parse command arguments
        :return: file
        """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='name of the file')
    args = parser.parse_args()
    return args.file


def file_read(filename: str) -> str:
    """
       Function for opening and reading files
       :return: text
       """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def finding_men(text: str) -> int:
     """
        Finding the count of profiles with the pattern "Мужской"
        :return: count of mens
     """
     pattern = r'\bМужской\b'
     count = re.findall(pattern, text)
     return len(count)


def main():
     # filename = parsers()
     filename = "data.txt"
     try:
         file_content = file_read(filename)
         print("The count of men is:",finding_men(file_content))
     except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
     except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()