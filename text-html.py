a=open("texts/remember.txt", mode="r")
b=open("html/remember.html", mode="w")

for line in a.readlines():
    b.write("<p>"+line.strip("\n")+"</p>")
#
# for line in a.readlines():
#     if '\n\n' in line:
#         b.write("<br><br><p>" + line.strip("\n") + "</p>\n")
#         i+=1
#     else:
#         b.write("<p>"+line.strip("\n")+"</p>")
#
#         i=1
