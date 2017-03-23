from sys import argv

if len(argv) < 3: exit()
r = int(argv[1])
c = int(argv[2])


"""Print out a table with r rows and c cols, the contents of each cell
will be its coordinates."""


print("<html><head><style>table, tr, td {padding:4px;border-collapse:collapse; border: 1px solid black;</style></head><body>")
print("<table>")

for row in range(r):
    print("\t<tr>")
    for col in range(c):
        print("\t\t<td>({},{})</td>".format(col, row))
    print("</tr>")

print("</table>")
print("</body>")
print("</html>")
