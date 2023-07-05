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

        # Define the path and filename for the XML file
        xml_file_path = '/home/test/Talha/newodoo/custom/CRMS/static/hello.xml'

        # Save the XML tree to the file
        tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

        # Prepare the file for download
        file_data = open(xml_file_path, 'rb').read()
        file_name = 'hello.xml'

        # Remove the XML file
        os.remove(xml_file_path)

        # Create a new attachment for the XML file
        attachment = self.env['ir.attachment'].create({
            'name': file_name,
            'datas': base64.b64encode(file_data),
            'mimetype': 'application/xml',
            'res_model': self._name,
            'res_id': self.id,
        })

        # Return the action to download the attachment
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'new'
        }
