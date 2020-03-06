import lxml.etree as ET
from tqdm import tqdm

prod_xml = ET.parse('users_prod.xml').getroot()
cat_xml = ET.parse('users_cat.xml').getroot()

with tqdm(total=len(cat_xml)) as progress:
    for su in cat_xml.iter('sys_user'):
        user = su.find('user_name').text
        old_sys_id = su.find('sys_id')
        for su_fix in prod_xml.xpath('.//*[user_name="{}"]'.format(user)):
            new_sys_id = su_fix.find('sys_id')
            tqdm.write('Fixing {:35s} : {} -> {}'.format(user, old_sys_id.text, new_sys_id.text))
            old_sys_id.text = new_sys_id.text
            assert su[58].text == su_fix[58].text
            progress.update(1)

ET.ElementTree(cat_xml).write('users_cat_fixed.xml', pretty_print=True, xml_declaration=True, encoding="utf-8")
