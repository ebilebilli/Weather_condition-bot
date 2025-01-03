with open('api_key.txt', 'r') as file:
    API_KEY = file.read()

if __name__ == '__main__':
    print(API_KEY)