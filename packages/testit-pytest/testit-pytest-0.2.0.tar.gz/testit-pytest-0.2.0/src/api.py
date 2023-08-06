import requests
import os
import mimetypes


class Api(object):

	def __init__(self, url, private_token):
		self.url = url
		self.headers = {'Authorization': 'PrivateToken ' + private_token}

	# AutoTests
	def create_autotest(self, json):
		response = requests.post(self.url + '/api/v2/autoTests', headers=self.headers, json=json)
		print(f"Autotest: {json['name']}")
		if response.status_code == 201:
			print('Create autotest passed!')
			return response.json()['id']
		elif response.status_code == 400:
			print("Create autotest error:\nName can't be empty or white space\nNamespace can't be empty or white space\nClassname can't be empty or white space\nDepth of nested steps more than AutoTestStepDepth (defaultAutoTestStepDepth = 15)\nStep can't be null\nInvalid Uri\nProjectId must be set\nExternalId must be set\nDepth of steps more than 15.")
		elif response.status_code == 401:
			print('Create autotest error: Unauthorized.')
		elif response.status_code == 403:
			print('Create autotest error: Update permission for auto test required.')
		elif response.status_code == 404:
			print("Create autotest error:\nCan't find Project with projectId\nLabels with listed globalId not found in the project.")
		elif response.status_code == 409:
			print('Create autotest error: AutoTest with ExternalId and ProjectId already exists.')
		elif response.status_code == 422:
			print('Create autotest error:\nLabels have duplicates\nLabel must not start with ::\nLabels with the same base have different values.')
		else:
			print('Create autotest error: ', response.status_code)

	def link_autotest(self, autotest_id, workitem_id):
		response = requests.post(f'{self.url}/api/v2/autoTests/{autotest_id}/workItems', headers=self.headers, json={'id': workitem_id})
		if response.status_code == 204:
			print('Link autoTest with workItems passed!')
		elif response.status_code == 400:
			print("Link autoTest with workItems error:\nCan't link AutoTest to SharedSteps\nCan't link AutoTest to WorkItem from different Project\nworkItemId must be uuid or global Id.")
		elif response.status_code == 401:
			print('Link autoTest with workItems error: Unauthorized.')
		elif response.status_code == 403:
			print('Link autoTest with workItems error: Update permission for auto test required.')
		elif response.status_code == 404:
			print("Link autoTest with workItems error:\nCan't find an AutoTest with autoTestId\nCan't find a WorkItem with workItemId.")
		else:
			print('Link autoTest with workItems error: ', response.status_code)

	def get_autotest(self, external_id, project_id):
		response = requests.get(f'{self.url}/api/v2/autoTests?projectId={project_id}&externalId={external_id}', headers=self.headers)
		if response.status_code == 200:
			print('Get autoTest passed!')
			return response
		elif response.status_code == 400:
			print('Get autoTest error: Not valid autoTestId.')
		elif response.status_code == 401:
			print('Get autoTest error: Unauthorized.')
		elif response.status_code == 403:
			print('Get autoTest error: Read permission for autoTest required.')
		else:
			print('Get autoTest error: ', response.status_code)

	def update_autotest(self, json):
		response = requests.put(self.url + '/api/v2/autoTests', headers=self.headers, json=json)
		print('AutoTest: {}\n'.format(json['name']))
		if response.status_code == 204:
			print('Update passed!')
		elif response.status_code == 400:
			print("Update error:\nName can't be empty or white space\nNamespace can't be empty or white space\nClassname can't be empty or white space\nDepth of steps more than {AutoTestStepDepth} (default nesting depth level constraint is 15)\nInvalid Uri\nProjectId must be set\nAutoTestExternalId must be set\nDepth of steps more than 15.")
		elif response.status_code == 401:
			print('Update error: Unauthorized.')
		elif response.status_code == 403:
			print('Update error: Update permission for auto test required.')
		elif response.status_code == 404:
			print("Update error:\nCan't find an AutoTest with Id\nCan't find Project with projectId\nCan't find links.id\nLabels with listed globalId not found in the project.")
		elif response.status_code == 409:
			print('Update error: AutoTest with ExternalId and ProjectId already exists.')
		elif response.status_code == 422:
			print('Update error:\nProjectId cannot be changed\nLabels have duplicates\nLabel must not start with ::\nLabels with the same base have different values.')
		else:
			print('Update error: ', response.status_code)

	# TestRuns
	def create_testrun(self, json):
		response = requests.post(self.url + '/api/v2/testRuns', headers=self.headers, json=json)
		if response.status_code == 201:
			print('Create testRun passed!')
			return response.json()['id']
		elif response.status_code == 400:
			print('Create testRun error: Field is required\nTestRun must be automated\nProjectId is not a valid.')
		elif response.status_code == 401:
			print('Create testRun error: TestRunTesterRequirement permission required.')
		elif response.status_code == 403:
			print('Create testRun error: Update permission for test result required.')
		elif response.status_code == 404:
			print("Create testRun error: Can't find a TestRun with id = testRunId.")
		else:
			print('Create testRun error: ', response.status_code)

	def set_results_for_testrun(self, testrun_id, json):
		response = requests.post(f'{self.url}/api/v2/testRuns/{testrun_id}/testResults', headers=self.headers, json=json)
		if response.status_code == 200:
			print('Set results passed!')
			return response.json()
		elif response.status_code == 400:
			print('Set results error:\nField is required\nAutoTestResultsShortModel is not valid\nTestPoints required\nTestPoints required cor Configuration and AutoTestExternalId\nDuration should be a positive number!\nDuration of step should be a positive number!\noutcome is not defined\nTestRun is stopped.')
		elif response.status_code == 401:
			print('Set results error: Unauthorized.')
		elif response.status_code == 403:
			print('Set results error: Update permission for test result required.')
		elif response.status_code == 404:
			print("Set results error:\nCan't find a TestRun with id!\nNot found TestPoint check input fields\nCan't find an AutoTest with AutoTestExternalId\nCan't find any TestPoint with autoTestExternalId and configurationId.")
		else:
			print('Set results error: ', response.status_code)

	def testrun_activity(self, testrun_id, to_do):
		response = requests.post(f'{self.url}/api/v2/testRuns/{testrun_id}/{to_do}', headers=self.headers)
		if response.status_code == 204:
			print(f'TestRun {to_do} passed!')
		elif response.status_code == 400:
			print(f'TestRun {to_do} error:\nField is required\nthe StateName is already NotStarted\nthe StateName is already Stopped\nthe StateName is already Stopped\nState is unknown.')
		elif response.status_code == 401:
			print(f'TestRun {to_do} error: Unauthorized.')
		elif response.status_code == 403:
			print(f'TestRun {to_do} error: Update permission for test result required.')
		elif response.status_code == 404:
			print(f"TestRun {to_do} error: Can't find a TestRun with id.")
		else:
			print(f'TestRun {to_do} error: {response.status_code}')

	def link_attachment(self, test_result_id, file):
		response = requests.post(f'{self.url}/api/v2/testResults/{test_result_id}/attachments', headers=self.headers, files={'file': (os.path.basename(file.name), file, mimetypes.guess_type(file.name)[0])})
		if response.status_code == 200:
			print('Link attachment passed!')
		elif response.status_code == 400:
			print('Link attachment error: Bad request.')
		elif response.status_code == 401:
			print('Link attachment error: Unauthorized.')
		elif response.status_code == 413:
			print('Link attachment error: Multipart body length limit exceeded.')
		else:
			print('Link attachment error: ', response.status_code)
