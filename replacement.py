import xml.etree.ElementTree

# Open original file
# et = xml.etree.ElementTree.parse('sys_user.xml')

# Append new tag: <a x='1' y='abc'>body text</a>
new_tag = xml.etree.ElementTree.SubElement(et.getroot(), 'a')
new_tag.text = 'body text'
new_tag.attrib['x'] = '1' # must be str; cannot be an int
new_tag.attrib['y'] = 'abc'
new_tag.attrib['y'] = 'abc'


# Write back to file
# Write back to file
#et.write('file.xml')
et.write('file_sys.xml')