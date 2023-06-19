import base64
import xml.etree.ElementTree as ET
from odoo import fields, models, _, tools, api
from odoo.exceptions import ValidationError


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    # Add more fields as needed

    @api.model
    def generate_xml_file(self,ids):
        # Perform the database query
        records = self.env['my.model'].search([])

        # Create the root element for the XML file
        root = ET.Element('data')

        # Iterate over the records and create XML elements
        for record in records:
            record_element = ET.SubElement(root, 'record')
            name_element = ET.SubElement(record_element, 'name')
            name_element.text = record.name
            age_element = ET.SubElement(record_element, 'age')
            age_element.text = str(record.age)
            # Add more elements as needed

        # Create the XML tree
        tree = ET.ElementTree(root)

        # Save the XML tree to a file
        tree.write('/home/test/Talha/newodoo/custom/CRMS/static/hello.xml', encoding='utf-8', xml_declaration=True)
