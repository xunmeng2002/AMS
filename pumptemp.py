#coding:utf-8
import xml.etree.cElementTree as ET
import codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8-sig")
out_file = codecs.open("./Source/Mdb/MdbTables.h","w+","utf-8-sig")

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

out_file.write("#pragma once\n")
out_file.write("#include \"DataStruct.h\"\n")
out_file.write("#include \"PrimaryKeys.h\"\n")
out_file.write("#include \"Indexes.h\"\n")
out_file.write("#include \"MemCacheTemplate.h\"\n")
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
    out_file.write("class ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table\n")
    out_file.write("{\n")
    out_file.write("public:\n")
    out_file.write("	")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table();\n")
    out_file.write("	")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* Alloc();\n")
    out_file.write("	void Free(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record);\n")
    out_file.write("	bool Insert(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record);\n")
    out_file.write("	bool Erase(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record);\n")
    out_file.write("	bool Update(const ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* oldRecord, const ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* newRecord);\n")
    out_file.write("	void Dump(const char* dir);\n")
    out_file.write("\n")
    out_file.write("public:\n")
    out_file.write("")
    entry_name = "primarykeys"
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
        out_file.write("	")
        out_file.write("%s" % str(tableName))
        out_file.write("PrimaryKey")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write(" m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("PrimaryKey;\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("")
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
        out_file.write("	")
        out_file.write("%s" % str(tableName))
        out_file.write("Index")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write(" m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index;\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("private:\n")
    out_file.write("	MemCacheTemplate<Account> m_MemCache;\n")
    out_file.write("};\n")
    out_file.write("\n")
    out_file.write("")
    
pumpidlist.pop()
if curr_node != parent2:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
out_file.write("\n")
out_file.write("")
out_file.close()
