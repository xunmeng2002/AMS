#coding:utf-8
import xml.etree.cElementTree as ET
import codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8-sig")
out_file = codecs.open("./Source/Mdb/Mdb.cpp","w+","utf-8-sig")

curr_node = ET.Element("root")
curr_node.append(ET.parse("./Model/Mdb/Tables.xml").getroot())
parent_map = {}
pumpidlist = []
def get_attr(node, name):
    while node != None:
        if node.get(name) == None:
            if node in parent_map:
                node = parent_map[node]
            else:
                break
        else:
            return node.get(name)
    return ""

out_file.write("#include \"Mdb.h\"\n")
out_file.write("\n")
out_file.write("\n")
out_file.write("")
entry_name = "tables"
parent1 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent1

out_file.write("\n")
out_file.write("Mdb::Mdb()\n")
out_file.write("{\n")
out_file.write("")
pumpidlist.append(0)
pumpid = -1
parent2 = curr_node
for node2 in curr_node:
    curr_node = node2
    parent_map[curr_node] = parent2
    pumpid += 1
    pumpidlist.append(pumpid)
    out_file.write("	t_")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write(" = new ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table();\n")
    out_file.write("")
    
pumpidlist.pop()
if curr_node != parent2:
    curr_node = parent_map[curr_node]
out_file.write("}\n")
out_file.write("void Mdb::Dump(const char* dir)\n")
out_file.write("{\n")
out_file.write("")
pumpidlist.append(0)
pumpid = -1
parent2 = curr_node
for node2 in curr_node:
    curr_node = node2
    parent_map[curr_node] = parent2
    pumpid += 1
    pumpidlist.append(pumpid)
    out_file.write("	t_")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("->Dump(dir);\n")
    out_file.write("")
    
pumpidlist.pop()
if curr_node != parent2:
    curr_node = parent_map[curr_node]
out_file.write("}\n")
out_file.write("void Mdb::Clear()\n")
out_file.write("{\n")
out_file.write("\n")
out_file.write("}\n")
out_file.write("\n")
out_file.write("")

curr_node = parent_map[curr_node]
out_file.close()
