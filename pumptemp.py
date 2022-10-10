#coding:utf-8
import xml.etree.cElementTree as ET
import codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8-sig")
out_file = codecs.open("./Source/Mdb/MdbTables.cpp","w+","utf-8-sig")

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

out_file.write("#include \"MdbTables.h\"\n")
out_file.write("#include <string>\n")
out_file.write("\n")
out_file.write("using std::string;\n")
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
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table::")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table()\n")
    out_file.write("{\n")
    out_file.write("}\n")
    out_file.write("")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table::Alloc()\n")
    out_file.write("{\n")
    out_file.write("	return m_MemCache.Allocate();\n")
    out_file.write("}\n")
    out_file.write("void ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table::Free(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record)\n")
    out_file.write("{\n")
    out_file.write("	m_MemCache.Free(record);\n")
    out_file.write("}\n")
    out_file.write("bool ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table::Insert(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record)\n")
    out_file.write("{\n")
    out_file.write("")
    entry_name = "primarykeys"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    out_file.write("	if (")
    pumpidlist.append(0)
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        pumpidlist.append(pumpid)
        if str(pumpid) >= '1':
            out_file.write(" && ")
        out_file.write("(!m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("PrimaryKey.CheckInsert(record))")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    out_file.write(")\n")
    out_file.write("	{\n")
    out_file.write("		printf(\"")
    out_file.write("%s" % str(tableName))
    out_file.write("Table Insert Failed for ")
    out_file.write("%s" % str(tableName))
    out_file.write(":[%s]\\n\", record->GetString());\n")
    out_file.write("		return false;\n")
    out_file.write("	}\n")
    out_file.write("")
    pumpidlist.append(0)
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        pumpidlist.append(pumpid)
        out_file.write("	m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("PrimaryKey.Insert(record);\n")
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
        out_file.write("	m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index.Insert(record);\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("	return true;\n")
    out_file.write("}\n")
    out_file.write("bool ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table::Erase(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record)\n")
    out_file.write("{\n")
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
        out_file.write("	if (!m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("PrimaryKey.Erase(record))\n")
        out_file.write("	{\n")
        out_file.write("		printf(\"")
        out_file.write("%s" % str(tableName))
        out_file.write("Table Erase Failed for ")
        out_file.write("%s" % str(tableName))
        out_file.write(":[%s]\\n\", record->GetString());\n")
        out_file.write("		return false;\n")
        out_file.write("	}\n")
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
        out_file.write("	m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index.Erase(record);\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("	return true;\n")
    out_file.write("}\n")
    out_file.write("bool ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table::Update(const ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* oldRecord, const ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* newRecord)\n")
    out_file.write("{\n")
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
        out_file.write("	if (!m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("PrimaryKey.CheckUpdate(oldRecord, newRecord))\n")
        out_file.write("	{\n")
        out_file.write("		printf(\"")
        out_file.write("%s" % str(tableName))
        out_file.write("Table Update Failed for ")
        out_file.write("%s" % str(tableName))
        out_file.write(":[%s], [%s]\\n\", oldRecord->GetString(), newRecord->GetString());\n")
        out_file.write("		return false;\n")
        out_file.write("	}\n")
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
        out_file.write("	bool ")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("IndexUpdate = m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index.NeedUpdate(oldRecord, newRecord);\n")
        out_file.write("	if (")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("IndexUpdate)\n")
        out_file.write("	{\n")
        out_file.write("		m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index.Erase((")
        out_file.write("%s" % str(tableName))
        out_file.write("*)oldRecord);\n")
        out_file.write("	}\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("	::memcpy((void*)oldRecord, newRecord, sizeof(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("));\n")
    out_file.write("	\n")
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
        out_file.write("	if (")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("IndexUpdate)\n")
        out_file.write("	{\n")
        out_file.write("		m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index.Insert((")
        out_file.write("%s" % str(tableName))
        out_file.write("*)oldRecord);\n")
        out_file.write("	}\n")
        out_file.write("")
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("	return true;\n")
    out_file.write("}\n")
    out_file.write("void ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("Table::Dump(const char* dir)\n")
    out_file.write("{\n")
    out_file.write("	string fileName = string(dir) + \"//t_")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write(".csv\";\n")
    out_file.write("	FILE* dumpFile = fopen(fileName.c_str(), \"w\");\n")
    out_file.write("	if (dumpFile == nullptr)\n")
    out_file.write("	{\n")
    out_file.write("		return;\n")
    out_file.write("	}\n")
    out_file.write("\n")
    out_file.write("	fprintf(dumpFile, \"")
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
        if str(pumpid) >= '1':
            out_file.write(", ")
        out_file.write("%s" % get_attr(curr_node, "name"))
        
    pumpidlist.pop()
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\\n\");\n")
    out_file.write("	char buff[4096] = { 0 };\n")
    out_file.write("	for (auto it = m_DefaultPrimaryKey.m_Index.begin(); it != m_DefaultPrimaryKey.m_Index.end(); ++it)\n")
    out_file.write("	{\n")
    out_file.write("		fprintf(dumpFile, \"%s\\n\", (*it)->GetString());\n")
    out_file.write("	}\n")
    out_file.write("	fclose(dumpFile);\n")
    out_file.write("}\n")
    out_file.write("\n")
    out_file.write("")
    
pumpidlist.pop()
if curr_node != parent2:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
out_file.write("\n")
out_file.write("")
out_file.close()
