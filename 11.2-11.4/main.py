print("===== Завдання 2 =====\n")
fin = open("file1.txt", "r")
fout = open("file1_1.txt", "w")
tmp = fin.read()
fout.write("«Отак подивишся здаля на москаля…»\n\n{}\n\nТарас Шевченко".format(tmp))
fin.close()
fout.close()

# print("===== Завдання 3 =====\n")
# fin = open("file2.txt", "r")
# fout = open("file2_2.txt", "w")
# for tmp in fin:
#     tmp2 = list(tmp)
#     if tmp[-1] == '\n':
#         tmp2[-1] = '!'
#     else:
#         tmp2.append('!')
#     for i in tmp2:
#         fout.write(i)
#     fout.write('\n')
# fin.close()
# fout.close()
#
# print("===== Завдання 4 =====\n")
# fin = open("file3.txt", "r")
# fout = open("file3.txt", "a")
# tmpi = []
# for i in fin:
#     tmp = i.split()
#     tmpi = [int(x) for x in tmp]
# maxx = -2147483647
# minn = 2147483648
# for i in tmpi:
#     if i < minn:
#         minn = i
#     if i > maxx:
#         maxx = i
# fout.write("\nСума чисел - {}".format(minn+maxx))
# fin.close()
# fout.close()