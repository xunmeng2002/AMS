#coding:utf-8
import xml.etree.cElementTree as ET
import codecs,sys

reload(sys)
sys.setdefaultencoding("utf-8-sig")
out_file = codecs.open("./Source/Mdb/MdbTables.cpp","w+","utf-8-sig")

curr_node = ET.Element("root")
curr_node.append(ET.parse("./Model/Mdb/Tables.xml").getroot())
parent_map = {}
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

pumpid = -1
parent2 = curr_node
for node2 in curr_node:
    curr_node = node2
    parent_map[curr_node] = parent2
    pumpid += 1
    tableName =  get_attr(curr_node, "name")
    className =  get_attr(curr_node, "name") + 'Table'
    out_file.write("%s" % str(className))
    out_file.write("::")
    out_file.write("%s" % str(className))
    out_file.write("()\n")
    out_file.write("{\n")
    out_file.write("}\n")
    out_file.write("")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* ")
    out_file.write("%s" % str(className))
    out_file.write("::Alloc()\n")
    out_file.write("{\n")
    out_file.write("	")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record = m_MemCache.Allocate();\n")
    out_file.write("	::memset(record, 0, sizeof(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("));\n")
    out_file.write("	return record;\n")
    out_file.write("}\n")
    out_file.write("void ")
    out_file.write("%s" % str(className))
    out_file.write("::Free(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record)\n")
    out_file.write("{\n")
    out_file.write("	m_MemCache.Free(record);\n")
    out_file.write("}\n")
    out_file.write("bool ")
    out_file.write("%s" % str(className))
    out_file.write("::Insert(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record)\n")
    out_file.write("{\n")
    out_file.write("")
    entry_name = "uniquekeys"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    out_file.write("	if (!m_PrimaryKey.CheckInsert(record)")
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        out_file.write(" && !m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("UniqueKey.CheckInsert(record)")
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    out_file.write(")\n")
    out_file.write("	{\n")
    out_file.write("		printf(\"Insert Failed for ")
    out_file.write("%s" % str(tableName))
    out_file.write(":[%s]\\n\", record->GetString());\n")
    out_file.write("		return false;\n")
    out_file.write("	}\n")
    out_file.write("")
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("	m_PrimaryKey.Insert(record);\n")
    out_file.write("")
    entry_name = "uniquekeys"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        out_file.write("	m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("UniqueKey.Insert(record);\n")
        out_file.write("")
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("")
    entry_name = "indexes"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        out_file.write("	m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index.Insert(record);\n")
        out_file.write("")
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("	return true;\n")
    out_file.write("}\n")
    out_file.write("bool ")
    out_file.write("%s" % str(className))
    out_file.write("::Erase(")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* record)\n")
    out_file.write("{\n")
    out_file.write("")
    entry_name = "uniquekeys"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    out_file.write("	if (!m_PrimaryKey.Erase(record)")
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        out_file.write(" && !m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("UniqueKey.Erase(record)")
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    out_file.write(")\n")
    out_file.write("	{\n")
    out_file.write("		printf(\"Erase Failed for ")
    out_file.write("%s" % str(tableName))
    out_file.write(":[%s]\\n\", record->GetString());\n")
    out_file.write("		return false;\n")
    out_file.write("	}\n")
    out_file.write("")
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("")
    entry_name = "indexes"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        out_file.write("	m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("Index.Erase(record);\n")
        out_file.write("")
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("	return true;\n")
    out_file.write("}\n")
    out_file.write("bool ")
    out_file.write("%s" % str(className))
    out_file.write("::Update(const ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* oldRecord, const ")
    out_file.write("%s" % get_attr(curr_node, "name"))
    out_file.write("* newRecord)\n")
    out_file.write("{\n")
    out_file.write("")
    entry_name = "uniquekeys"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    out_file.write("	if (!m_PrimaryKey.CheckUpdate(oldRecord, newRecord)")
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        out_file.write(" && !m_")
        out_file.write("%s" % get_attr(curr_node, "name"))
        out_file.write("UniqueKey.CheckUpdate(oldRecord, newRecord)")
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    out_file.write(")\n")
    out_file.write("	{\n")
    out_file.write("		printf(\"Update Failed for ")
    out_file.write("%s" % str(tableName))
    out_file.write(":[%s], [%s]\\n\", oldRecord->GetString(), newRecord->GetString());\n")
    out_file.write("		return false;\n")
    out_file.write("	}\n")
    out_file.write("")
    
    curr_node = parent_map[curr_node]
    out_file.write("\n")
    out_file.write("")
    entry_name = "indexes"
    parent3 = curr_node
    curr_node = curr_node.find(entry_name)
    parent_map[curr_node] = parent3
    
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
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
    
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
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
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("	\n")
    out_file.write("	m_MemCache.Free((")
    out_file.write("%s" % str(tableName))
    out_file.write("*)newRecord);\n")
    out_file.write("	return true;\n")
    out_file.write("}\n")
    out_file.write("void ")
    out_file.write("%s" % str(className))
    out_file.write("::Dump(const char* dir)\n")
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
    
    pumpid = -1
    parent4 = curr_node
    for node4 in curr_node:
        curr_node = node4
        parent_map[curr_node] = parent4
        pumpid += 1
        if pumpid > 0:
            out_file.write(", ")
        out_file.write("%s" % get_attr(curr_node, "name"))
        
    if curr_node != parent4:
        curr_node = parent_map[curr_node]
    
    curr_node = parent_map[curr_node]
    out_file.write("\\n\");\n")
    out_file.write("	char buff[4096] = { 0 };\n")
    out_file.write("	for (auto it = m_PrimaryKey.m_Index.begin(); it != m_PrimaryKey.m_Index.end(); ++it)\n")
    out_file.write("	{\n")
    out_file.write("		fprintf(dumpFile, \"%s\\n\", (*it)->GetString());\n")
    out_file.write("	}\n")
    out_file.write("	fclose(dumpFile);\n")
    out_file.write("}\n")
    out_file.write("\n")
    out_file.write("")
    
if curr_node != parent2:
    curr_node = parent_map[curr_node]

curr_node = parent_map[curr_node]
out_file.write("\n")
out_file.write("")
out_file.close()
