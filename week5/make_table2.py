r = 5
c = 4


print("<table>")

for row in range(r):
    print("<tr>")
    for col in range(c):
        print("<td>({}, {})</td>".format(col, row))
    print("</tr>")
print("</table>")
