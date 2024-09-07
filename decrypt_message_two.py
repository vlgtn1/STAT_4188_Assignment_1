encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

length = len(encrypted_message)

result = list(encrypted_message)
result1 = list(encrypted_message)
start = 1
end = length - 2


while start < end:
    result[start] = result1[end]
    result[end] = result1[start]

    start += 2
    end -= 2

final = ''
for i in result:
    final += i

print(final)
