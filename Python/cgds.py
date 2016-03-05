import requests

API_ROOT = "http://www.cbioportal.org/api/"

# Function for getting all the Cancer Types
def getCancerTypes():
	response = requests.get(API_ROOT+"cancertypes")
	return response.text


# Function for getting Clinical Data Sample
# Function parameters are studyId and attributeId
def getSampleClinicalData(studyId, attributeId, sampleId=None):
	payload = {}
	if sampleId:
		payload = {'study_id': studyId, 'attribute_ids': attributeId, 'sample_ids': sampleId}
	else:
		payload = {'study_id': studyId, 'attribute_ids': attributeId}
	response = requests.get(API_ROOT+"clinicaldata/samples", params=payload)
	return response.text


# Function for getting Patient Clinical Data
def getPatientClinicalData(studyId, attributeId, patientId=None):
	payload = {}
	if sampleId:
		payload = {'study_id': studyId, 'attribute_ids': attributeId, 'patient_ids': sampleId}
	else:
		payload = {'study_id': studyId, 'attribute_ids': attributeId}
	response = requests.get(API_ROOT+"clinicaldata/patients", params=payload)
	return response.text

# Fucntion for getting Sample Clinical Attributes
def getSampleClinicalAttributes(studyId=None, sampleId=None):
	payload = {}
	if studyId and sampleId:
		payload = {'study_id': studyId, 'sample_ids': sampleId}

	response = requests.get(API_ROOT+"clinicalattributes/samples", params=payload)
	return response.text

# Fucntion for getting Patient Clinical Attributes
def getPatientClinicalAttributes(studyId=None, patientId=None):
	payload = {}
	if studyId and patientId:
		payload = {'study_id': studyId, 'patient_ids': sampleId}

	response = requests.get(API_ROOT+"clinicalattributes/patients", params=payload)
	return response.text

# Fucntion for getting Genes
def getGenes(hugoGeneSymbols=None):
	payload = {}
	if hugoGeneSymbols:
		payload = {'hugo_gene_symbols': hugoGeneSymbols}

	response = requests.get(API_ROOT+"genes", params=payload)
	return response.text

# Fucntion for getting Genetic Profile
def getGeneticProfile(studyId=None, genticProfileId=None):
	payload = {}
	if genticProfileId:
		payload.update({'genetic_profile_ids': genticProfileId})
	if studyId:
		payload.update({'studyId': study_id})

	response = requests.get(API_ROOT+"geneticprofiles", params=payload)
	return response.text

# Function for getting Sample List
def getSampleList(studyId=None, sampleListId=None):	
	payload = {}
	if sampleListId:
		payload.update({'sample_list_ids': sampleListId})
	if studyId:
		payload.update({'studyId': study_id})

	response = requests.get(API_ROOT+"samplelists", params=payload)
	return response.text

# Function for getting Patient List
def getPatients(studyId, patientId=None):	
	payload = {'studyId': studyId}
	if patientId:
		payload.update({'patient_ids': patientId})

	response = requests.get(API_ROOT+"patients", params=payload)
	return response.text

# Function for getting Genetic Profile Data
def getGeneticProfileData(geneticProfileId, genes, sampleId=None):	
	payload = {'genetic_profile_ids':geneticProfileId, 'genes':genes}
	if sampleId:
		payload.update({'sample_ids': sampleId})

	response = requests.get(API_ROOT+"geneticprofiledata", params=payload)
	return response.text

# Function for getting Samples
def getSamples(studyId, sampleId=None):	
	payload = {'studyId':studyId}
	if sampleId:
		payload.update({'sample_ids': sampleId})

	response = requests.get(API_ROOT+"samples", params=payload)
	return response.text

# Function for getting Studies
def getStudies(studyId=None):	
	if studyId:
		payload.update({'studyId':studyId})

	response = requests.get(API_ROOT+"studies", params=payload)
	return response.text