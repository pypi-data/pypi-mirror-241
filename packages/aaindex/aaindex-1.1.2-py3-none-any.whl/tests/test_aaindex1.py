################################################################################
################             AAindex1 Module Tests             #################
################################################################################

import os
import unittest
from importlib.metadata import metadata
from aaindex import aaindex1, __version__

class AAIndex1_Tests(unittest.TestCase):
    """
    Test suite for testing the aaindex1 module in the aaindex Python software package.

    Test Cases
    ==========
    test_aaindex_metadata:
        testing correct aaindex version and metadata.
    test_num_records:
        testing to check that the correct number of indices/records are present
        in the AAindex object. 
    test_records:
        testing to check that the correct record data and amino acid values 
        are returned for the accessiom number/index codes using the __getitem__ 
        function.
    test_records_dot_notation:
        testing to check that the correct record data and amino acid values 
        are returned for the accessiom number/index codes using the __getitem__ 
        function, accessing the elements using the dot notation created from 
        the Map class.
    test_search:
        testing search functionality where 1 or more aaindex1 records can be returned 
        if their description contains user-inputted keywords.
    test_record_codes:
        testing to check that correct feature/record codes are in the parsed JSON
        of all AAi1 records.
    test_record_names:
        testing to check that the correct names/description is returned for each index.
    test_last_updated:
        testing hard-coded date value that the AAindex database were last updated.
    """
    def setUp(self):
        """ Inititalise AAindex module variables and test data directory. """
        self.test_dir = 'test_data'

        #make test data directory, remove old one if exists
        if (os.path.isdir(self.test_dir)):
            os.rmdir(self.test_dir)
        os.mkdir(self.test_dir)

    def test_aaindex_metadata(self):
        """ Testing correct aaindex version and metadata. """
        self.assertEqual(__version__, "1.1.2",
            "aaindex version is not correct, got: {}.".format(metadata("aaindex")['version']))
        self.assertEqual(metadata("aaindex")['name'], "aaindex", 
            "aaindex software name is not correct, got: {}.".format(metadata("aaindex")['name']))
        self.assertEqual(metadata("aaindex")['author'], "AJ McKenna: https://github.com/amckenna41", 
            "aaindex author is not correct, got: {}.".format(metadata("aaindex")['author']))
        self.assertEqual(metadata("aaindex")['author-email'], "amckenna41@qub.ac.uk", 
            "aaindex author email is not correct, got: {}.".format(metadata("aaindex")['author-email']))
        self.assertEqual(metadata('aaindex')['home-page'], "https://github.com/amckenna41/aaindex", 
            "aaindex home page url is not correct, got: {}.".format(metadata('aaindex')['home-page']))
        self.assertEqual(metadata('aaindex')['maintainer'], "AJ McKenna", 
            "aaindex maintainer is not correct, got: {}.".format(metadata('aaindex')['maintainer']))
        self.assertEqual(metadata('aaindex')['license'], "MIT", 
            "aaindex license type is not correct, got: {}.".format(metadata('aaindex')['license']))
        # self.assertEqual(metadata('aaindex')['summary'], 
        #     "A lightweight Python software package for accessing the data in the various AAIndex databases, "
        #     "which represent the physiochemical, biochemical and structural properties of amino acids as numerical indices.", 
        #             "aaindex package summary is not correct, got:\n{}.".format(metadata('aaindex')['summary']))
        self.assertEqual(metadata('aaindex')['keywords'], 
            "amino acid index,aaindex,bioinformatics,protein engineering,python,pypi,physiochemical properties,"
            "biochemical properties,proteins,protein structure prediction,pysar", 
                "aaindex keywords are not correct, got:\n{}.".format(metadata('aaindex')['keywords']))

    def test_amino_acids(self):
        """ Test Case to check that only valid Amino Acids are used within the AAindex class. """
        valid_amino_acids = ['-', 'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
            'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
        amino_acids = aaindex1.amino_acids()
#1.)
        for aa in amino_acids:
            self.assertIn(aa, valid_amino_acids, 'Amino Acid {} not in list of valid amino acids:\n{}.'.format(aa, valid_amino_acids))

    def test_num_records(self):
        """ Test Case to check that the correct number of indices/records are present
        in the AAindex object. To date, 566 indices are present in the database. """
#1.)
        self.assertEqual(aaindex1.num_records(), 566, 
            'Incorrect number of records found in AAi1, expected 566, got {}.'.format(aaindex1.num_records()))

    def test_records(self):
        """ Test Case to check that the correct record data and amino acid values 
        are returned for the accessiom number/index codes using the __getitem__ function. """
#1.)
        #initialise test records codes and their correct and expected amino acid values
        index_code1 = 'AURR980103'
        expected_index_code1_vals = {'A': 1.05, 'L': 0.96, 'R': 0.81, 'K': 0.97, 'N': 0.91,
            'M': 0.99, 'D': 1.39, 'F': 0.95, 'C': 0.6, 'P': 1.05, 'Q': 0.87,
            'S': 0.96, 'E': 1.11, 'T': 1.03, 'G': 1.26, 'W': 1.06, 'H': 1.43,
            'Y': 0.94, 'I': 0.95, 'V': 0.62, '-': 0}

        index_code2 = 'FINA770101'
        expected_index_code2_vals = {'-': 0, 'A': 1.08, 'C': 0.95, 'D': 0.85, 'E': 1.15, 
            'F': 1.1, 'G': 0.55, 'H': 1.0, 'I': 1.05, 'K': 1.15, 'L': 1.25, 'M': 1.15, 
            'N': 0.85, 'P': 0.71, 'Q': 0.95, 'R': 1.05, 'S': 0.75, 'T': 0.75, 
            'V': 0.95, 'W': 1.1, 'Y': 1.1}

        index_code3 = 'nagk730101' #function can accept lowercase record codes
        expected_index_code3_vals = {'A': 1.29, 'L': 1.23, 'R': 0.83, 'K': 1.23, 'N': 0.77,
            'M': 1.23, 'D': 1.0, 'F': 1.23, 'C': 0.94, 'P': 0.7, 'Q': 1.1,
            'S': 0.78, 'E': 1.54, 'T': 0.87, 'G': 0.72, 'W': 1.06, 'H': 1.29,
            'Y': 0.63, 'I': 0.94, 'V': 0.97, '-': 0}

        index_code4 = 'TANS770103'
        expected_index_code4_vals = {'-': 0, 'A': 0.79, 'C': 1.268, 'D': 0.53, 'E': 0.643, 
            'F': 1.052, 'G': 0.725, 'H': 0.864, 'I': 1.361, 'K': 0.735, 'L': 1.111, 
            'M': 1.092, 'N': 0.832, 'P': 1.249, 'Q': 1.038, 'R': 1.087, 'S': 1.093, 
            'T': 1.214, 'V': 1.428, 'W': 1.114, 'Y': 1.34}

        index_code5 = "ABCDEFGH"
        index_code6 = "123456"
        index_code7 = "blahblahblah"
        index_code8 = ""
#1.)
        #get amino acid values for inputted feature/index codes
        record = aaindex1[index_code1] #AURR980103

        self.assertIn('description', list(record.keys()), "description key not found in aaindex record object.")
        self.assertIn('references', list(record.keys()), "references key not found in aaindex record object.")
        self.assertIn('notes', list(record.keys()), "notes key not found in aaindex record object.")
        self.assertIn('values', list(record.keys()), "values key not found in aaindex record object.")
        self.assertIn('category', list(record.keys()), "category key not found in aaindex record object.")
        self.assertIn('pmid', list(record.keys()), "pmid key not found in aaindex record object.")
        self.assertIn('correlation_coefficients', list(record.keys()), "correlation_coefficients key not found in aaindex record object.")

        self.assertEqual(record['description'], "Normalized positional residue frequency at helix termini N' (Aurora-Rose, 1998)",
            "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
        self.assertEqual(record['notes'], '', 
            "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
        self.assertEqual(record['references'], "Aurora, R. and Rose, G. 'Helix capping' Protein Science 7, 21-38 (1998)", 
            "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
        self.assertEqual(record['category'], 'sec_struct', 
            "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
        self.assertEqual(record['pmid'], '9514257', 
            "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
        self.assertEqual(record['correlation_coefficients'], {}, 
            "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
        self.assertEqual(record['values'], expected_index_code1_vals, 
            "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
        for aa, val in list(record['values'].items()):
            if (aa == '-'):
                continue 
            self.assertIsInstance(val, float, 
                "Values in record values not of correct datatype, expected float, got {}.".format(type(val)))
#2.)
        record = aaindex1[index_code2] #FINA770101

        self.assertIn('description', list(record.keys()), "description key not found in aaindex record object.")
        self.assertIn('references', list(record.keys()), "references key not found in aaindex record object.")
        self.assertIn('notes', list(record.keys()), "notes key not found in aaindex record object.")
        self.assertIn('values', list(record.keys()), "values key not found in aaindex record object.")
        self.assertIn('category', list(record.keys()), "category key not found in aaindex record object.")
        self.assertIn('pmid', list(record.keys()), "pmid key not found in aaindex record object.")
        self.assertIn('correlation_coefficients', list(record.keys()), "correlation_coefficients key not found in aaindex record object.")
        
        self.assertEqual(record['description'], 'Helix-coil equilibrium constant (Finkelstein-Ptitsyn, 1977)',
            "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
        self.assertEqual(record['notes'], '',
            "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
        self.assertEqual(record['references'], "Finkelstein, A.V. and Ptitsyn, O.B. 'Theory of protein molecule self-organization. "
                          "II. A comparison of calculated thermodynamic parameters of local secondary structures with experiments' "
                          "Biopolymers 16, 497-524 (1977) (Pro 0.096)", 
            "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
        self.assertEqual(record['category'], 'sec_struct', 
            "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
        self.assertEqual(record['pmid'], '843599', 
            "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
        self.assertEqual(record['correlation_coefficients'], {'AURR980109': '0.802', 
            'AURR980113': '0.849', 'AURR980114': '0.875', 'KANM800103': '0.823', 
            'MAXF760101': '0.810', 'PTIO830101': '0.826', 'QIAN880106': '0.810', 
            'QIAN880107': '0.814', 'SUEM840101': '0.883'}, 
            "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
        self.assertEqual(record['values'], expected_index_code2_vals, 
            "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
        for aa, val in list(record['values'].items()):
            if (aa == '-'):
                continue 
            self.assertIsInstance(val, float, 
                "Values in record values not of correct datatype, expected float, got {}.".format(type(val)))
#3.)
        record = aaindex1[index_code3] #nagk730101

        self.assertIn('description', list(record.keys()), "description key not found in aaindex record object.")
        self.assertIn('references', list(record.keys()), "references key not found in aaindex record object.")
        self.assertIn('notes', list(record.keys()), "notes key not found in aaindex record object.")
        self.assertIn('values', list(record.keys()), "values key not found in aaindex record object.")
        self.assertIn('category', list(record.keys()), "category key not found in aaindex record object.")
        self.assertIn('pmid', list(record.keys()), "pmid key not found in aaindex record object.")
        self.assertIn('correlation_coefficients', list(record.keys()), "correlation_coefficients key not found in aaindex record object.")
        
        self.assertEqual(record['description'], 'Normalized frequency of alpha-helix (Nagano, 1973)',
            "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
        self.assertEqual(record['notes'], '', 
            "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
        self.assertEqual(record['references'], "Nagano, K. 'Local analysis of the mechanism of protein folding. "
                        "I. Prediction of helices, loops, and beta-structures from primary structure' J. Mol. Biol. 75, 401-420 (1973)",
            "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
        self.assertEqual(record['category'], 'sec_struct',
            "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
        self.assertEqual(record['pmid'], '4728695', 
            "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
        self.assertEqual(record['correlation_coefficients'], 
            {'BURA740101': '0.883', 'CHOP780201': '0.886', 'CRAJ730101': '0.925', 
            'GEIM800101': '0.912', 'GEIM800104': '0.828', 'ISOY800101': '0.862', 
            'KANM800101': '0.883', 'LEVM780101': '0.894', 'LEVM780104': '0.918', 
            'MAXF760101': '0.877', 'NAGK730103': '-0.870', 'PALJ810101': '0.953', 
            'PALJ810102': '0.876', 'PRAM900102': '0.894', 'RACS820108': '0.820', 
            'ROBB760101': '0.910', 'TANS770101': '0.925'}, 
            "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
        self.assertEqual(record['values'], expected_index_code3_vals, 
            "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
        for aa, val in list(record['values'].items()):
            if (aa == '-'):
                continue 
            self.assertIsInstance(val, float, 
                "Values in record values not of correct datatype, expected float, got {}.".format(type(val)))
#4.)
        record = aaindex1[index_code4] #TANS770103

        self.assertIn('description', list(record.keys()), "description key not found in aaindex record object.")
        self.assertIn('references', list(record.keys()), "reference key not found in aaindex record object.")
        self.assertIn('notes', list(record.keys()), "notes key not found in aaindex record object.")
        self.assertIn('values', list(record.keys()), "values key not found in aaindex record object.")
        self.assertIn('category', list(record.keys()), "category key not found in aaindex record object.")
        self.assertIn('pmid', list(record.keys()), "pmid key not found in aaindex record object.")
        self.assertIn('correlation_coefficients', list(record.keys()), "correlation_coefficients key not found in aaindex record object.")

        self.assertEqual(record['description'], 'Normalized frequency of extended structure (Tanaka-Scheraga, 1977)',
            "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
        self.assertEqual(record['notes'], '', 
            "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
        self.assertEqual(record['references'], "Tanaka, S. and Scheraga, H.A. 'Statistical mechanical treatment of protein"
                        " conformation. 5. A multiphasic model for specific-sequence copolymers of amino acids' Macromolecules"
                        " 10, 9-20 (1977) Recalculated by Kidera as normalized frequencies", 
            "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
        self.assertEqual(record['category'], 'sec_struct', 
            "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
        self.assertEqual(record['pmid'], '557155', 
            "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
        self.assertEqual(record['correlation_coefficients'], 
            {'GEIM800105': '0.850', 'ISOY800102': '0.929', 'MAXF760102': '0.891', 
            'PALJ810103': '0.824', 'RACS820111': '0.841', 'ROBB760105': '0.871', 
            'WOEC730101': '-0.806'}, 
            "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
        self.assertEqual(record['values'], expected_index_code4_vals,
            "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
        for aa, val in list(record['values'].items()):
            if (aa == '-'):
                continue 
            self.assertIsInstance(val, float, 
                "Values in record values not of correct datatype, expected float, got {}.".format(type(val)))
#5.)
        #testing value error raised when erroneous indices sought from object
        with self.assertRaises(ValueError):
            record = aaindex1[index_code5]
            record = aaindex1[index_code6]
            record = aaindex1[index_code7]
            record = aaindex1[index_code8]

    def test_records_dot_notation(self):
            """ Test Case to check that the correct record data and amino acid values 
            are returned for the accessiom number/index codes using the __getitem__ 
            function, accessing the elements using the dot notation created from the 
            Map class. """
            #initialise test record codes and their correct and expected amino acid values
            index_code1 = 'KARP850103'
            expected_index_code1_vals = {'-': 0, 'A': 0.892, 'C': 0.925, 'D': 0.932, 
                'E': 0.933, 'F': 0.914, 'G': 0.923, 'H': 0.894, 'I': 0.872, 'K': 1.057, 
                'L': 0.921, 'M': 0.804, 'N': 0.93, 'P': 0.932, 'Q': 0.885, 'R': 0.901, 
                'S': 0.923, 'T': 0.934, 'V': 0.913, 'W': 0.803, 'Y': 0.837}

            index_code2 = 'PALJ810109'
            expected_index_code2_vals = {'-': 0, 'A': 1.15, 'C': 1.03, 'D': 1.0, 'E': 1.37, 
                'F': 0.92, 'G': 0.64, 'H': 0.95, 'I': 0.99, 'K': 1.2, 'L': 1.22, 'M': 1.45, 
                'N': 0.87, 'P': 0.72, 'Q': 1.43, 'R': 1.06, 'S': 0.84, 'T': 0.97, 'V': 0.82, 
                'W': 1.11, 'Y': 0.72}

            index_code3 = 'ROBB760112'
            expected_index_code3_vals = {'-': 0, 'A': -2.5, 'C': -4.7, 'D': 0.0, 'E': -4.4, 
                'F': -4.1, 'G': 4.9, 'H': 1.6, 'I': -3.3, 'K': -0.8, 'L': -2.0, 'M': -4.1, 
                'N': 4.6, 'P': 5.8, 'Q': -0.5, 'R': -1.2, 'S': 2.5, 'T': 1.7, 'V': -3.5, 
                'W': 1.2, 'Y': -0.6}

            index_code4 = 'TANS770103'
            expected_index_code4_vals = {'-': 0, 'A': 0.79, 'C': 1.268, 'D': 0.53, 'E': 0.643, 
                'F': 1.052, 'G': 0.725, 'H': 0.864, 'I': 1.361, 'K': 0.735, 'L': 1.111, 
                'M': 1.092, 'N': 0.832, 'P': 1.249, 'Q': 1.038, 'R': 1.087, 'S': 1.093, 
                'T': 1.214, 'V': 1.428, 'W': 1.114, 'Y': 1.34}

            index_code5 = "ABCDEFGH"
            index_code6 = "123456"
            index_code7 = "blahblahblah"
            index_code8 = ""
#1.)
            #get amino acid values for inputted record/index codes
            record = aaindex1[index_code1]

            self.assertEqual(record.description, "Flexibility parameter for two rigid neighbors (Karplus-Schulz, 1985)",
                "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
            self.assertEqual(record.notes, '',
                "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
            self.assertEqual(record.references, "Karplus, P.A. and Schulz, G.E. 'Prediction of chain flexibility in proteins' Naturwiss. 72, 212-213 (1985)",
                "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
            self.assertEqual(record.category, 'flexibility', 
                "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
            self.assertEqual(record.pmid, '', 
                "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
            self.assertEqual(record.correlation_coefficients, {}, 
                "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
            self.assertEqual(record.values, expected_index_code1_vals, 
                "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
#2.)
            record = aaindex1[index_code2]

            self.assertEqual(record.description, 'Normalized frequency of alpha-helix in alpha/beta class (Palau et al., 1981)',
                "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
            self.assertEqual(record.notes, '', 
                "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
            self.assertTrue(record.references.startswith("Palau, J., Argos, P. and Puigdomenech"), 
                "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
            self.assertEqual(record.category, 'sec_struct', 
                "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
            self.assertEqual(record.pmid, '7118409', 
                "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
            self.assertEqual(record.correlation_coefficients, 
                {'AURR980112': '0.817', 'CHOP780201': '0.814', 
                'CRAJ730101': '0.811', 'GEIM800101': '0.816', 'GEIM800104': '0.937', 'ISOY800101': '0.874', 
                'KANM800101': '0.849', 'LEVM780101': '0.898', 'LEVM780104': '0.819', 'MAXF760101': '0.876', 
                'PALJ810102': '0.864', 'PRAM900102': '0.898', 'ROBB760101': '0.805'}, 
                "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
            self.assertEqual(record.values, expected_index_code2_vals, 
                "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
#3.)
            record = aaindex1[index_code3]

            self.assertEqual(record.description, 'Information measure for coil (Robson-Suzuki, 1976)',
                "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
            self.assertEqual(record.notes, '',
                "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
            self.assertTrue(record.references.startswith("Robson, B. and Suzuki, E"),
                "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
            self.assertEqual(record.category, 'sec_struct', 
                "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
            self.assertEqual(record.pmid, '1003471', 
                "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
            self.assertEqual(record.correlation_coefficients, 
                {'CHOP780211': '0.841', 'ISOY800103': '0.807', 'PALJ810115': '0.885', 
                'QIAN880132': '0.800', 'QIAN880133': '0.814'}, 
                "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
            self.assertEqual(record.values, expected_index_code3_vals, 
                "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
#4.)
            record = aaindex1[index_code4]

            self.assertEqual(record.description, 'Normalized frequency of extended structure (Tanaka-Scheraga, 1977)',
                "Description from AAi1 record does not match the expected value, got {}.".format(record['description']))
            self.assertEqual(record.notes, '', 
                "Notes from AAi1 record does not match the expected value, got {}.".format(record['notes']))
            self.assertTrue(record.references.startswith("Tanaka, S. and Scheraga, H.A."),
                "Reference from AAi1 record do not match the expected value, got {}.".format(record['references']))
            self.assertEqual(record.category, 'sec_struct', 
                "Category from AAi1 record does not match the expected value, got {}.".format(record['category']))
            self.assertEqual(record.pmid, '557155', 
                "PMID from AAi1 record does not match the expected value, got {}.".format(record['pmid']))
            self.assertEqual(record.correlation_coefficients, 
                {'GEIM800105': '0.850', 'ISOY800102': '0.929', 'MAXF760102': '0.891', 'PALJ810103': '0.824', 
                'RACS820111': '0.841', 'ROBB760105': '0.871', 'WOEC730101': '-0.806'}, 
                "Correlation Coefficients from AAi1 record do not match the expected value, got {}.".format(record['correlation_coefficients']))
            self.assertEqual(record.values, expected_index_code4_vals, 
                "Values for individual amino acids do not match expected, got\n{}.".format(record['values']))
#5.)
            #testing value error raised when erroneous indices sought from object
            with self.assertRaises(ValueError):
                aaindex1[index_code5]
                aaindex1[index_code6]
                aaindex1[index_code7]
                aaindex1[index_code8]

    def test_search(self):
        """ Testing search functionality where 1 or more aaindex1 records will be returned 
            if their description contains user-inputted keywords. """ 
        description1 = "Gibbs Energy"
        description2 = 'Polarity'
        description3 = 'Hydrophobic'
        description4 = ['pi-helices', 'Retention coefficient', 'p-Values']
        description5 = 'blahblahblah'
        description6 = 'not a description'
        description7 = 1234
        description8 = 1.24
        description9 = False
#1.)
        description1_search = aaindex1.search(description1)
        expected_description1_indices = ['YUTK870101', 'YUTK870102', 'YUTK870103', 'YUTK870104']

        self.assertEqual(len(description1_search), 4, 
            "Expected there to be 4 records returned from search, got {}.".format(len(description1_search)))
        for index, val in description1_search.items():
            self.assertIn(index, expected_description1_indices, 
                "Index record {} expected to be found in search results.".format(index))
            self.assertTrue(description1.lower() in description1_search[index]['description'].lower(), 
                "Expected description to be in record of returned search results, got {}".format(description1_search[index]))
#2.)
        description2_search = aaindex1.search(description2)
        expected_description2_indices = ['GRAR740102', 'RADA880108', 'ZIMJ680103']
      
        self.assertEqual(len(description2_search), 3, 
            "Expected there to be 3 records returned from search, got {}.".format(len(description2_search)))
        for index, val in description2_search.items():
            self.assertIn(index, expected_description2_indices,
                "Index record {} expected to be found in search results.".format(index))
            self.assertTrue(description2.lower() in description2_search[index]['description'].lower(),
                "Expected description to be in record of returned search results, got {}.".format(description2_search[index]))
#3.)
        description3_search = aaindex1.search(description3)
        expected_description3_indices = ['ARGP820101', 'BLAS910101', 'CASG920101', 'CIDH920101', 'CIDH920102', 'CIDH920103', 
            'CIDH920104', 'CIDH920105', 'COWR900101', 'EISD840101', 'EISD860102', 'EISD860103', 'ENGD860101', 'FASG890101', 
            'FAUJ830101', 'GOLD730101', 'JOND750101', 'JURD980101', 'KIDA850101', 'LEVM760101', 'MANP780101', 'PONP800101', 
            'PONP800102', 'PONP800103', 'PONP800104', 'PONP800105', 'PONP800106', 'PONP930101', 'PRAM900101', 'SWER830101', 
            'WILM950101', 'WILM950102', 'WILM950103', 'WILM950104', 'WOLR790101', 'ZIMJ680101']
 
        self.assertEqual(len(description3_search), 36, 
            "Expected there to be 36 records returned from search, got {}.".format(len(description3_search)))
        for index, val in description3_search.items():
            self.assertIn(index, expected_description3_indices, 
                "Index record {} expected to be found in search results.".format(index))
            self.assertTrue(description3.lower() in description3_search[index]['description'].lower(),
                "Expected description to be in record of returned search results, got {}.".format(description3_search[index]))
#4.)
        description4_search = aaindex1.search(description4)
        expected_description4_indices = ['FODM020101', 'BROC820101', 'BROC820102', 'GUOD860101', 'MEEJ800101', 'MEEJ800102', \
                                         'MEEJ810101', 'MEEJ810102', 'PARS000101', 'PARS000102']

        self.assertEqual(len(description4_search), 10, 
            "Expected there to be 10 records returned from search, got {}.".format(len(description4_search)))
        for index, val in description4_search.items():
            self.assertIn(index, expected_description4_indices, 
                "Index record {} expected to be found in search results.".format(index))
#5.)
        description5_search = aaindex1.search(description5)
        self.assertEqual(len(description5_search), 0, 
            "Expected there to be 0 records returned from search, got {}.".format(len(description5_search)))
#6.)
        description6_search = aaindex1.search(description6)
        self.assertEqual(len(description6_search), 0, 
            "Expected there to be 0 records returned from search, got {}.".format(len(description6_search)))
#7.)    
        with (self.assertRaises(TypeError)):
            aaindex1.search(description7)
            aaindex1.search(description8)
            aaindex1.search(description9)

    def test_record_codes(self):
        """ Test Case to check that correct feature/record codes are in the parsed JSON
            of all AAi1 records. Also testing that closely named erroneous records codes 
            are not present. """
        #testing actual index codes
        index_code1 = 'VHEG790101'
        index_code2 = 'PONP800107'
        index_code3 = 'OOBM770102'
        index_code4 = 'NADH010101'
#1.)
        #testing index codes that are in the AAi1
        self.assertIn(index_code1, aaindex1.record_codes(), 'Expected record {} to be in list of available indices.'.format(index_code1))
        self.assertIn(index_code2, aaindex1.record_codes(), 'Expected record {} to be in list of available indices.'.format(index_code2))
        self.assertIn(index_code3, aaindex1.record_codes(), 'Expected record {} to be in list of available indices.'.format(index_code3))
        self.assertIn(index_code4, aaindex1.record_codes(), 'Expected record {} to be in list of available indices.'.format(index_code4))
#2.)
        #testing closely named index codes
        index_code5 = 'VHEG790500'
        index_code6 = 'P0NP800107'
        index_code7 = 'OObm770102'
        index_code8 = 'NADW210101'

        #testing errenous index codes are not in the AAi1
        self.assertNotIn(index_code5, aaindex1.record_codes(), 'Expected record {} to not be in list of available indices.'.format(index_code5))
        self.assertNotIn(index_code6, aaindex1.record_codes(), 'Expected record {} to not be in list of available indices.'.format(index_code6))
        self.assertNotIn(index_code7, aaindex1.record_codes(), 'Expected record {} to not be in list of available indices.'.format(index_code7))
        self.assertNotIn(index_code8, aaindex1.record_codes(), 'Expected record {} to not be in list of available indices.'.format(index_code8))

    def test_record_names(self):
        """ Test Case to check that the correct names/description are returned for each record. """
        record_names = aaindex1.record_names()
        record_name1 = record_names[50]
        record_name2 = record_names[140]
        record_name3 = record_names[368]
        record_name4 = record_names[560]
#1.)
        self.assertEqual(len(record_names), aaindex1.num_records(), 
            'Total number of names in the AAi1 database should equal the number of records, got {}.'.format(len(record_names)))
#2.)
        self.assertEqual(record_name1, 'alpha-NH chemical shifts (Bundi-Wuthrich, 1979)', 
            'Incorrect record name returned, expected {} got {}.'.format('alpha-NH chemical shifts (Bundi-Wuthrich, 1979).', record_name1))
#3.)
        self.assertTrue(record_name2.startswith('Number of full nonbonding'), 
            'Incorrect record name returned, expected {} got {}.'.format('Number of full nonbonding', record_name2))
#4.)
        self.assertIn('alpha-helix in alpha/beta class', record_name3, 
            'Expected string {} to be found in record name: {}.'.format('alpha-helix in alpha/beta class', record_name3))
#5.)
        self.assertEqual(record_name4, 'Buriability (Zhou-Zhou, 2004)', 
            'Expected record name to be {}, got {}.'.format('Buriability (Zhou-Zhou, 2004)', record_name4))

    def test_last_updated(self):
        """ Testing the last updated class attribute which is the latest version of the database, 
            according to https://www.genome.jp/aaindex/. """
        self.assertEqual(aaindex1.last_updated, "February 13, 2017", 
            "Last updated value does not match expected, got {}.".format(aaindex1.last_updated))

    def tearDown(self):
        """ Remove any test data or directories. """
        os.rmdir('test_data')

if __name__ == '__main__':
    #run all unit tests
    unittest.main(verbosity=2)