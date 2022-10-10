#coding:utf-8
import xml.etree.cElementTree as ET
import codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8-sig")
out_file = codecs.open("./Source/Index/Indexes.cpp","w+","utf-8-sig")

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

out_file.write("#include \"Indexes.h\"\n")
out_file.write("\n")
out_file.write("\n")
out_file.write("")
entry_name = "tables"
parent1 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent1

pumpidlist.append(0)
pumpid = -1
parent2 = curr_node
for node2 in curr_node:
    curr_node = node2
    parent_map[curr_node] = parent2
    pumpid += 1
    pumpidlist.append(pumpid)
    tableName =  get_attr(curr_node, "name")
    entry_name = "indexes"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    pumpidlist.append(0)
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        pumpidlist.append(pumpid)
        out_file.write("void ")
        out_file.write("%s" % str(tableName))
        out_file.write("IndexFor")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("::Insert(")
        out_file.write("%s" % str(tableName))
        out_file.write("* const record)\n")
        out_file.write("{\n")
        out_file.write("	m_Index.insert(record);\n")
        out_file.write("}\n")
        out_file.write("void ")
        out_file.write("%s" % str(tableName))
        out_file.write("IndexFor")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("::Erase(")
        out_file.write("%s" % str(tableName))
        out_file.write("* const record)\n")
        out_file.write("{\n")
        out_file.write("	m_Index.erase(record);\n")
        out_file.write("}\n")
        out_file.write("bool ")
        out_file.write("%s" % str(tableName))
        out_file.write("IndexFor")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("::NeedUpdate(const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const oldRecord, const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const newRecord)\n")
        out_file.write("{\n")
        out_file.write("	return !(")
        out_file.write("%s" % str(tableName))
        out_file.write("EqualFor")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("()(oldRecord, newRecord));\n")
        out_file.write("}\n")
        out_file.write("\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("")
    
pumpidlist.pop()
if curr_node != parent2:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
out_file.write("\n")
out_file.write("")
out_file.close()
