from qgis.PyQt.QtCore import QVariant

"""
/*****************
Tick box values
*****************/
"""
# Authoritative lists of threatened species available in the ALA
threatenedLists = {
    "ACT": "dr649",
    "EPBC": "dr656",
    "NSW": "dr650",
    "NT": "dr651",
    "QLD": "dr652",
    "SA": "dr653",
    "TAS": "dr654",
    "VIC": "dr655",
    "WA": "dr2201",
}

# Authoritative lists of sensitive species available in the ALA
sensitiveLists = {
    "ACT": "dr2627",
    "NSW": "dr487",
    "NT": "dr492",
    "QLD": "dr493",
    "SA": "dr884",
    "TAS": "dr491",
    "VIC": "dr490",
    "WA": "dr467",
}

# Authoritative lists of migratory species available in the ALA
migratoryLists = {
    "Bonn": "dr18987",
    "CAMBA": "dr18989",
    "JAMBA": "dr18988",
    "ROKAMBA": "dr18990",
}

# Authoritative lists of non-native species available in the ALA
nonNativeLists = {"NonNative All": "dr32213"}

# taxon selections
taxon_selections = [
    "scientificName",
    "kingdom",
    "phylum",
    "class",
    "order",
    "family",
    "genus",
    "vernacularName",
]

"""
/*****************
Attribute values
*****************/
"""

# declare dictionary of all possible attributes to add to the layer
attributes_dict = {
    "decimalLatitude": QVariant.Double,
    "decimalLongitude": QVariant.Double,
    "eventDate": QVariant.String,
    "scientificName": QVariant.String,
    "taxonConceptID": QVariant.String,
    "recordID": QVariant.String,
    "dataResourceName": QVariant.String,
    "occurrenceStatus": QVariant.String,
    "dataProviderName": QVariant.String,
    "stateConservation": QVariant.String,
    "countryConservation": QVariant.String,
    "latitude": QVariant.Double,
    "longitude": QVariant.Double,
    "occurrence_date": QVariant.String,
    "taxon_name": QVariant.String,
    "taxon_concept_lsid": QVariant.String,
    "id": QVariant.String,
    "data_resource": QVariant.String,
    "occurrence_status": QVariant.String,
    "data_provider": QVariant.String,
    "gbifID": QVariant.String,
    "datasetKey": QVariant.String,
    "occurrenceID": QVariant.String,
    "kingdom": QVariant.String,
    "phylum": QVariant.String,
    "class": QVariant.String,
    "order": QVariant.String,
    "family": QVariant.String,
    "genus": QVariant.String,
    "species": QVariant.String,
    "infraspecificEpithet": QVariant.String,
    "taxonRank": QVariant.String,
    "verbatimScientificName": QVariant.String,
    "verbatimScientificNameAuthorship": QVariant.String,
    "countryCode": QVariant.String,
    "locality": QVariant.String,
    "stateProvince": QVariant.String,
    "individualCount": QVariant.String,
    "publishingOrgKey": QVariant.String,
    "coordinateUncertaintyInMeters": QVariant.String,
    "coordinatePrecision": QVariant.String,
    "elevation": QVariant.String,
    "elevationAccuracy": QVariant.String,
    "depth": QVariant.String,
    "depthAccuracy": QVariant.String,
    "day": QVariant.String,
    "month": QVariant.String,
    "year": QVariant.String,
    "taxonKey": QVariant.String,
    "speciesKey": QVariant.String,
    "basisOfRecord": QVariant.String,
    "institutionCode": QVariant.String,
    "collectionCode": QVariant.String,
    "catalogNumber": QVariant.String,
    "recordNumber": QVariant.String,
    "identifiedBy": QVariant.String,
    "dateIdentified": QVariant.String,
    "license": QVariant.String,
    "rightsHolder": QVariant.String,
    "recordedBy": QVariant.String,
    "typeStatus": QVariant.String,
    "establishmentMeans": QVariant.String,
    "lastInterpreted": QVariant.String,
    "mediaType": QVariant.String,
    "issue": QVariant.String,
}

"""
/**********************************
Lat/long values for each atlas
**********************************/
"""
latitude_dict = {
    "Australia": "decimalLatitude",
    "Austria": "decimalLatitude",  # "latitude",
    "Brazil": "latitude",
    "France": "latitude",
    "Flanders": "decimalLatitude",
    "Global": "decimalLatitude",
    "Guatemala": "latitude",
    "Kew": "decimalLatitude",
    "Spain": "decimalLatitude",
    "Sweden": "decimalLatitude",
    "United Kingdom": "decimalLatitude",
}

longitude_dict = {
    "Australia": "decimalLongitude",
    "Austria": "decimalLongitude",  # "longitude",
    "Brazil": "longitude",
    "Flanders": "decimalLongitude",
    "Global": "decimalLongitude",
    "Kew": "decimalLongitude",
    "Spain": "decimalLongitude",
    "Sweden": "decimalLongitude",
    "United Kingdom": "decimalLongitude",
}

eventdate_dict = {
    "Australia": "eventDate",
    "Austria": "occurrence_date",
    "Brazil": "occurrence_date",
    "Flanders": "eventDate",
    "Global": "eventDate",
    "Kew": "eventDate",
    "Spain": "eventDate",
    "Sweden": "eventDate",
    "United Kingdom": "eventDate",
}

bor_dict = {
    "Australia": "basisOfRecord",
    "Austria": "basis_of_record",
    "Brazil": "basis_of_record",
    "Flanders": "basisOfRecord",
    "Global": "basisOfRecord",
    "Kew": "basisOfRecord",
    "Spain": "basisOfRecord",
    "Sweden": "basisOfRecord",
    "United Kingdom": "basisOfRecord",
}

occstatus_dict = {
    "Australia": "occurrenceStatus",
    "Austria": "occurrence_status",
    "Brazil": "occurrence_status",
    "Flanders": "occurrenceStatus",
    "Global": "occurrenceStatus",
    "Kew": "occurrenceStatus",
    "Spain": "occurrenceStatus",
    "Sweden": "occurrenceStatus",
    "United Kingdom": "occurrenceStatus",
}

occ_fields = {
    "Australia": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
    "Austria": ["basic", "data_resource", "data_provider"],
    "Brazil": [
        "latitude",
        "longitude",
        "occurrence_date",
        "taxon_name",
        "taxon_concept_lsid",
        "id",
        "data_resource",
        "occurrence_status",
        "data_provider",
    ],
    "Flanders": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
    "Global": ["basic"],
    "Kew": ["basic"],
    "Spain": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
    "Sweden": ["basic", "dataProviderName"],
    "United Kingdom": ["basic", "dataProviderName", "stateConservation", "countryConservation"],
}

taxon_fields_dict = {
    "Australia": taxon_selections + ["identifiers"],
    "Austria": [
        "taxon_name",
        "kingdom",
        "phylum",
        "class",
        "order",
        "family",
        "genus",
        "common_name",
    ],
    "Brazil": [
        "taxon_name",
        "kingdom",
        "phylum",
        "class",
        "order",
        "family",
        "genus",
        "common_name",
    ],
    "Flanders": taxon_selections,
    "Global": taxon_selections,
    "Kew": taxon_selections,
    "Spain": taxon_selections,
    "Sweden": taxon_selections,
    "United Kingdom": taxon_selections,
}


ATLAS_DICT = {
    "atlas": ["Australia", "Austria", "Brazil", "Flanders", "Global", "Kew", "Spain", "Sweden", "United Kingdom"],
    "institution": [
        "Atlas of Living Australia",
        "Biodiversitäts-Atlas Österreich",
        "Sistemas de Informações sobre a Biodiversidade Brasileira",
        "Vlaams Biodiversiteitsportaal",
        "Global Biodiversity Information Facility",
        "Kew Data Portal",
        "GBIF Spain",
        "Swedish Biodiversity Data Infrastructure",
        "National Biodiversity Network",
    ],
    "acronym": ["ALA", "BAO", "SiBBr", "VBP", "GBIF", "KDP", "GBIF.es", "SDBI", "NBN"],
    "url": [
        " https://www.ala.org.au",
        "https://biodiversityatlas.at",
        "https://sibbr.gov.br",
        "https://natuurdata.inbo.be",
        "https://gbif.org",
        "https://data.kew.org",
        "https://www.gbif.es",
        "https://biodiversitydata.se",
        "https://nbn.org.uk",
    ],
}

PROFILES_DICT = {
    "id": [
        "92",
        "124",
        "133",
        "224",
        "252",
    ],
    "name": [
        "ALA General",
        "Species Distribution Modelling (CSDM)",
        "Data licensed for all uses",
        "AVH",
        "ALA General Test",
    ],
    "shortName": [
        "ALA",
        "CSDM",
        "re-usable",
        "AVH",
        "ALA-test",
    ],
    "description": [
        "The default ALA profile filters out records based on the filter groups outlined below.  This is a moderately restricted set of data.",
        "Base filters for the Collaborative Species Distribution Modelling program",
        'Data licensed for re-use, including commercial uses. This profile only filters on license, no "quality" filters are applied.',
        "AVH data quality profile",
        "A test version of the default ALA profile filters out records based on the filter groups outlined below.  This is a moderately restricted set of data.",
    ],
}

default_reasons = {
    "id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "name": [
        "conservation management/planning",
        "biosecurity management/planning",
        "environmental assessment",
        "education",
        "scientific research",
        "collection management",
        "other",
        "ecological research",
        "systematic research/taxonomy",
        "other scientific research",
        "testing",
        "citizen science",
        "restoration/remediation",
        "species modelling",
    ],
}

REASONS_DICT = {
    "ALA": default_reasons,
    "Austria": default_reasons,
    "Brazil": None,
    "Flanders": None,
    "Global": None,
    "Kew": default_reasons,
    "Spain": {
        "id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "name": [
            "conservation management/planning",
            "Gestión de bioseguridad",
            "Evaluación ambiental",
            "Educación",
            "Investigación científica",
            "Gestión de colecciones",
            "Otros",
            "Investigación en ecología",
            "Investigación sistemática/taxonomía",
            "Otro tipo de investigación científica",
            "testing",
            "Ciencia ciudadana",
            "Restauración/remediación",
        ],
    },
    "Sweden": {
        "id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "name": [
            "conservation management/planning",
            "biosecurity management/planning",
            "environmental assessment",
            "education",
            "scientific research",
            "collection management",
            "other",
            "ecological research",
            "systematic research/taxonomy",
            "other scientific research",
            "testing",
            "citizen science",
            "restoration/remediation",
        ],
    },
    "United Kingdom": {
        "id": [0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        "name": [
            "conservation management/planning",
            "biosecurity management/planning",
            "environmental assessment",
            "education|Download is for primary, secondary or tertiary educational purposes",
            "scientific research",
            "collection management",
            "ecological research",
            "systematic research/taxonomy",
            "testing|Testing",
            "citizen science",
            "restoration/remediation",
            "statutory|Download is by a government-linked body or local authority for their statutory wor",
            "LERC work|Download is for use by a local environmental records centre to support the provision of its services",
            "public|Download is for personal use only",
            "volunteer researcher/publisher|Download may lead to amateur (non-funded) publication, which could include National or Local scheme collators and verifiers",
            "professional researcher/publisher|Download may lead to professional publication (including universities, NGOs etc. where people are being paid to research and publish)",
            "commercial|Download is for the purposes of fulfilling a commercial contract",
        ],
    },
}
