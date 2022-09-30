#coding:utf-8
import xml.etree.cElementTree as ET
import codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8-sig")
out_file = codecs.open("./Source/Index/IndexComp.cpp","w+","utf-8-sig")

curr_node = ET.Element("root")
curr_node.append(ET.parse("./Model/Mdb/Tables.xml").getroot())
curr_node.append(ET.parse("./Model/Mdb/DataType.xml").getroot())
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

out_file.write("#include \"IndexComp.h\"\n")
out_file.write("#include <string>\n")
out_file.write("\n")
out_file.write("using std::string;\n")
out_file.write("\n")
out_file.write("")
types={}
entry_name = "types"
parent1 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent1

entry_name = "bools"
parent2 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent2

pumpidlist.append(0)
pumpid = -1
parent3 = curr_node
for node3 in curr_node:
    curr_node = node3
    parent_map[curr_node] = parent3
    pumpid += 1
    pumpidlist.append(pumpid)
    types[ get_attr(curr_node, "name")] = 'bool'
    
pumpidlist.pop()
if curr_node != parent3:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
entry_name = "ints"
parent2 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent2

pumpidlist.append(0)
pumpid = -1
parent3 = curr_node
for node3 in curr_node:
    curr_node = node3
    parent_map[curr_node] = parent3
    pumpid += 1
    pumpidlist.append(pumpid)
    types[ get_attr(curr_node, "name")] = 'int'
    
pumpidlist.pop()
if curr_node != parent3:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
entry_name = "int64s"
parent2 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent2

pumpidlist.append(0)
pumpid = -1
parent3 = curr_node
for node3 in curr_node:
    curr_node = node3
    parent_map[curr_node] = parent3
    pumpid += 1
    pumpidlist.append(pumpid)
    types[ get_attr(curr_node, "name")] = 'int64'
    
pumpidlist.pop()
if curr_node != parent3:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
entry_name = "doubles"
parent2 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent2

pumpidlist.append(0)
pumpid = -1
parent3 = curr_node
for node3 in curr_node:
    curr_node = node3
    parent_map[curr_node] = parent3
    pumpid += 1
    pumpidlist.append(pumpid)
    types[ get_attr(curr_node, "name")] = 'double'
    
pumpidlist.pop()
if curr_node != parent3:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
entry_name = "strings"
parent2 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent2

pumpidlist.append(0)
pumpid = -1
parent3 = curr_node
for node3 in curr_node:
    curr_node = node3
    parent_map[curr_node] = parent3
    pumpid += 1
    pumpidlist.append(pumpid)
    types[ get_attr(curr_node, "name")] = 'string'
    
pumpidlist.pop()
if curr_node != parent3:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
entry_name = "enums"
parent2 = curr_node
curr_node = curr_node.find(entry_name)
parent_map[curr_node] = parent2

pumpidlist.append(0)
pumpid = -1
parent3 = curr_node
for node3 in curr_node:
    curr_node = node3
    parent_map[curr_node] = parent3
    pumpid += 1
    pumpidlist.append(pumpid)
    types[ get_attr(curr_node, "name")] = 'enum'
    
pumpidlist.pop()
if curr_node != parent3:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
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
    fieldTypes = {}
    entry_name = "fields"
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
        fieldTypes[ get_attr(curr_node, "name")] = types[ get_attr(curr_node, "type")]
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
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
        out_file.write("bool ")
        out_file.write("%s" % str(tableName))
        out_file.write("EqualFor")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("::operator()(const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const left, const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const right) const\n")
        out_file.write("{\n")
        out_file.write("	return ")
        pumpidlist.append(0)
        pumpid = -1
        parent5 = curr_node
        for node5 in curr_node:
            curr_node = node5
            parent_map[curr_node] = parent5
            pumpid += 1
            pumpidlist.append(pumpid)
            if str(pumpid) >= '1':
                out_file.write("&& ")
            type = fieldTypes[ get_attr(curr_node, "name")]
            if type == 'string':
                out_file.write("strcmp(left->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(", right->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(") == 0")
            else:
                out_file.write("left->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(" == right->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(" ")
            
        pumpidlist.pop()
        if curr_node != parent5:
            curr_node = parent_map[curr_node]
        out_file.write(";\n")
        out_file.write("}\n")
        out_file.write("bool ")
        out_file.write("%s" % str(tableName))
        out_file.write("LessFor")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("::operator()(const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const left, const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const right) const\n")
        out_file.write("{\n")
        out_file.write("")
        pumpidlist.append(0)
        pumpid = -1
        parent5 = curr_node
        for node5 in curr_node:
            curr_node = node5
            parent_map[curr_node] = parent5
            pumpid += 1
            pumpidlist.append(pumpid)
            type = fieldTypes[ get_attr(curr_node, "name")]
            if type == 'string':
                out_file.write("	if (strcmp(left->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(", right->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(") < 0)\n")
                out_file.write("	{\n")
                out_file.write("		return true;\n")
                out_file.write("	}\n")
                out_file.write("	else if (strcmp(left->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(", right->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(") > 0)\n")
                out_file.write("	{\n")
                out_file.write("		return false;\n")
                out_file.write("	}\n")
                out_file.write("")
            else:
                out_file.write("	if (left->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(" < right->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(")\n")
                out_file.write("	{\n")
                out_file.write("		return true;\n")
                out_file.write("	}\n")
                out_file.write("	else if (left->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(" > right->")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(")\n")
                out_file.write("	{\n")
                out_file.write("		return false;\n")
                out_file.write("	}\n")
                out_file.write("")
            
        pumpidlist.pop()
        if curr_node != parent5:
            curr_node = parent_map[curr_node]
        out_file.write("	return false;\n")
        out_file.write("};\n")
        out_file.write("\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    
pumpidlist.pop()
if curr_node != parent2:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
out_file.close()
