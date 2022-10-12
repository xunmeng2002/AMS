#coding:utf-8
import xml.etree.cElementTree as ET
import codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8-sig")
out_file = codecs.open("./Source/Index/PrimaryKeys.cpp","w+","utf-8-sig")

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

out_file.write("#include \"PrimaryKeys.h\"\n")
out_file.write("\n")
out_file.write("using std::unordered_set;\n")
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
        fieldTypes[ get_attr(curr_node, "name")] =  get_attr(curr_node, "type")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
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
        className = tableName + 'PrimaryKey' +  get_attr(curr_node, "name")
        out_file.write("%s" % str(className))
        out_file.write("::")
        out_file.write("%s" % str(className))
        out_file.write("(size_t buckets)\n")
        out_file.write("	:m_Index(buckets), m_Select")
        out_file.write("%s" % str(tableName))
        out_file.write("()\n")
        out_file.write("{\n")
        out_file.write("}\n")
        out_file.write("bool ")
        out_file.write("%s" % str(className))
        out_file.write("::Insert(")
        out_file.write("%s" % str(tableName))
        out_file.write("* const record)\n")
        out_file.write("{\n")
        out_file.write("	return m_Index.insert(record).second;\n")
        out_file.write("}\n")
        out_file.write("bool ")
        out_file.write("%s" % str(className))
        out_file.write("::Erase(")
        out_file.write("%s" % str(tableName))
        out_file.write("* const  record)\n")
        out_file.write("{\n")
        out_file.write("	return  m_Index.erase(record) > 0;\n")
        out_file.write("}\n")
        out_file.write("bool ")
        out_file.write("%s" % str(className))
        out_file.write("::CheckInsert(")
        out_file.write("%s" % str(tableName))
        out_file.write("* const record)\n")
        out_file.write("{\n")
        out_file.write("	return m_Index.find(record) == m_Index.end();\n")
        out_file.write("}\n")
        out_file.write("bool ")
        out_file.write("%s" % str(className))
        out_file.write("::CheckUpdate(const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const oldRecord, const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* const newRecord)\n")
        out_file.write("{\n")
        out_file.write("	return ")
        out_file.write("%s" % str(tableName))
        out_file.write("EqualFor")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("PrimaryKey()(oldRecord, newRecord);\n")
        out_file.write("}\n")
        out_file.write("const ")
        out_file.write("%s" % str(tableName))
        out_file.write("* ")
        out_file.write("%s" % str(className))
        out_file.write("::Select(")
        pumpidlist.append(0)
        pumpid = -1
        parent5 = curr_node
        for node5 in curr_node:
            curr_node = node5
            parent_map[curr_node] = parent5
            pumpid += 1
            pumpidlist.append(pumpid)
            fieldType=fieldTypes[ get_attr(curr_node, "name")]
            if str(pumpid) >= '1':
                out_file.write(", ")
            out_file.write("const C")
            out_file.write("%s" % str(fieldType))
            out_file.write("Type& ")
            out_file.write("%s" % get_attr(curr_node, "name"))
            
        pumpidlist.pop()
        if curr_node != parent5:
            curr_node = parent_map[curr_node]
        out_file.write(")\n")
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
            fieldType=fieldTypes[ get_attr(curr_node, "name")]
            type = types[fieldType]
            if str(type) == 'string':
                out_file.write("	strcpy(m_Select")
                out_file.write("%s" % str(tableName))
                out_file.write(".")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(", ")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(");\n")
                out_file.write("")
            else:
                out_file.write("	m_Select")
                out_file.write("%s" % str(tableName))
                out_file.write(".")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(" = ")
                out_file.write("%s" % get_attr(curr_node, "name"))
                out_file.write(";\n")
                out_file.write("")
            
        pumpidlist.pop()
        if curr_node != parent5:
            curr_node = parent_map[curr_node]
        out_file.write("\n")
        out_file.write("	auto it = m_Index.find(&m_Select")
        out_file.write("%s" % str(tableName))
        out_file.write(");\n")
        out_file.write("	if (it == m_Index.end())\n")
        out_file.write("	{\n")
        out_file.write("		return nullptr;\n")
        out_file.write("	}\n")
        out_file.write("	return *it;\n")
        out_file.write("}\n")
        out_file.write("\n")
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
